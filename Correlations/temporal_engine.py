#!/usr/bin/env python3
"""
Temporal Correlation Engine
===========================
Computes the lag between state data-center legislation (trigger dates) and
federal funding actions (action dates) to determine whether federal
targeting is proactive (negative lag) or reactive (positive lag).

Input files:
  - Correlations/data_center_legislation_tracker.csv  (6 core states)
  - 02_CSVs_and_Datasets/Copilot_Agent/expanded_state_legislation_tracker.csv
  - Correlations/Federal_Funding_Withholding_2025-2026.csv
  - 02_CSVs_and_Datasets/Copilot_Agent/state_posture_lookup.csv  (27 states)

Output:
  - Correlations/temporal_analysis_final.csv
  - Correlations/temporal_summary.md
"""

import pandas as pd
import re
import os
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
COPILOT_DIR = os.path.join(REPO_ROOT, "02_CSVs_and_Datasets", "Copilot_Agent")

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
# Core legislation tracker (6 states: AR, TX, OK, NY, VA, CA)
leg_core = pd.read_csv(
    os.path.join(SCRIPT_DIR, "data_center_legislation_tracker.csv")
)

# Expanded legislation tracker (additional states incl. Neutral/Mixed)
leg_expanded = pd.read_csv(
    os.path.join(COPILOT_DIR, "expanded_state_legislation_tracker.csv")
)

# Combine both trackers, drop exact duplicates
legislation = pd.concat([leg_core, leg_expanded], ignore_index=True)
legislation = legislation.drop_duplicates(
    subset=["state_code", "bill"], keep="first"
)
print(
    f"Loaded legislation: {len(leg_core)} core + {len(leg_expanded)} expanded "
    f"= {len(legislation)} unique bills"
)

# Federal funding tracker
funding = pd.read_csv(
    os.path.join(SCRIPT_DIR, "Federal_Funding_Withholding_2025-2026.csv")
)
print(f"Loaded federal funding: {len(funding)} actions")

# 27-state posture lookup (includes Neutral/Mixed)
posture = pd.read_csv(os.path.join(COPILOT_DIR, "state_posture_lookup.csv"))

# Supplement with ANALYSIS posture file for any states not in the 27-state file
analysis_posture_path = os.path.join(REPO_ROOT, "ANALYSIS", "state_posture_lookup.csv")
if os.path.exists(analysis_posture_path):
    posture_analysis = pd.read_csv(analysis_posture_path)
    # Add states present in ANALYSIS but missing from the comprehensive file
    missing = posture_analysis[
        ~posture_analysis["state_code"].isin(posture["state_code"])
    ]
    if len(missing) > 0:
        # Align columns: keep only the columns present in the primary file
        shared_cols = [c for c in posture.columns if c in missing.columns]
        posture = pd.concat(
            [posture, missing[shared_cols]], ignore_index=True
        )
        print(f"  Added {len(missing)} states from ANALYSIS posture file: "
              f"{missing['state_code'].tolist()}")

print(f"Loaded posture: {len(posture)} states")
print(f"  Posture breakdown: {posture['posture'].value_counts().to_dict()}")

# ---------------------------------------------------------------------------
# 2. Parse trigger dates from legislation
# ---------------------------------------------------------------------------
MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def _parse_month(s):
    return MONTH_MAP.get(s[:3].lower())


def _is_vetoed(status):
    if not isinstance(status, str):
        return False
    return "veto" in status.lower()


def _extract_status_date(status):
    """Extract the most specific date hidden inside a status string."""
    if not isinstance(status, str):
        return None

    # Pattern 1 (most specific): Month DD YYYY  /  Month DD, YYYY
    m = re.search(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*"
        r"\s+(\d{1,2}),?\s+(\d{4})",
        status,
    )
    if m:
        month = _parse_month(m.group(1))
        day = int(m.group(2))
        year = int(m.group(3))
        try:
            return datetime(year, month, day)
        except ValueError:
            pass

    # Pattern 2: Month YYYY
    m = re.search(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+(\d{4})",
        status,
    )
    if m:
        month = _parse_month(m.group(1))
        year = int(m.group(2))
        try:
            return datetime(year, month, 1)
        except ValueError:
            pass

    # Pattern 3: bare year (2024–2029)
    m = re.search(r"\b(202[4-9])\b", status)
    if m:
        return datetime(int(m.group(1)), 1, 1)

    return None


def _extract_effective_date(eff):
    """Extract an ISO-style date from the effective_date field."""
    if not isinstance(eff, str) or eff.strip() in ("N/A", "", "nan"):
        return None
    m = re.search(r"(\d{4}-\d{2}-\d{2})", eff)
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y-%m-%d")
        except ValueError:
            pass
    return None


# Build per-bill trigger dates (excluding vetoed bills)
trigger_rows = []
for _, row in legislation.iterrows():
    if _is_vetoed(str(row.get("status", ""))):
        continue

    # Prioritize status date, fall back to effective_date
    date = _extract_status_date(str(row.get("status", "")))
    if date is None:
        date = _extract_effective_date(str(row.get("effective_date", "")))

    if date is not None:
        trigger_rows.append(
            {
                "state": row["state"],
                "state_code": row["state_code"],
                "bill": row["bill"],
                "trigger_date": date,
            }
        )

trigger_df = pd.DataFrame(trigger_rows)

# Earliest trigger date per state
state_triggers = (
    trigger_df.groupby("state_code")["trigger_date"].min().reset_index()
)

print("\nEarliest trigger date per state:")
for _, r in state_triggers.iterrows():
    print(f"  {r['state_code']}: {r['trigger_date'].strftime('%Y-%m-%d')}")

# ---------------------------------------------------------------------------
# 3. Parse federal action dates
# ---------------------------------------------------------------------------
funding["action_date"] = pd.to_datetime(
    funding["date"], format="%Y-%m-%d", errors="coerce"
)

# ---------------------------------------------------------------------------
# 4. Map federal actions → affected states
# ---------------------------------------------------------------------------
trigger_state_set = set(state_triggers["state_code"].tolist())

records = []
for _, fed in funding.iterrows():
    if pd.isna(fed["action_date"]):
        continue

    jurisdiction = str(fed.get("state_jurisdiction", ""))
    sc_raw = str(fed.get("state_code", "")).strip()

    # Determine which states are affected
    if sc_raw and sc_raw != "nan":
        affected = [s.strip() for s in sc_raw.split(",") if s.strip()]
    elif "all states" in jurisdiction.lower():
        # "All States" actions apply to every state in the dataset
        affected = list(trigger_state_set)
    else:
        # Fallback: treat as "All States"
        affected = list(trigger_state_set)

    for sc in affected:
        if sc in trigger_state_set:
            records.append(
                {
                    "state_code": sc,
                    "federal_action": fed.get("program_name", ""),
                    "action_type": fed.get("action_type", ""),
                    "action_date": fed["action_date"],
                }
            )

pairs = pd.DataFrame(records)
print(f"\nGenerated {len(pairs)} state–action pair records")

# ---------------------------------------------------------------------------
# 5. Merge trigger dates & calculate lag
# ---------------------------------------------------------------------------
pairs = pairs.merge(state_triggers, on="state_code", how="inner")
pairs["lag_days"] = (pairs["action_date"] - pairs["trigger_date"]).dt.days

# ---------------------------------------------------------------------------
# 6. Merge posture
# ---------------------------------------------------------------------------
posture_map = posture[["state_code", "state", "posture"]].drop_duplicates()
pairs = pairs.merge(posture_map, on="state_code", how="left", suffixes=("", "_pos"))
# Use posture-sourced state name where available
if "state_pos" in pairs.columns:
    pairs["state"] = pairs["state_pos"].combine_first(pairs["state"])
    pairs.drop(columns=["state_pos"], inplace=True)

# ---------------------------------------------------------------------------
# 7. Write temporal_analysis_final.csv
# ---------------------------------------------------------------------------
output_cols = [
    "state",
    "state_code",
    "posture",
    "federal_action",
    "action_type",
    "action_date",
    "trigger_date",
    "lag_days",
]
pairs["action_date"] = pairs["action_date"].dt.strftime("%Y-%m-%d")
pairs["trigger_date"] = pairs["trigger_date"].dt.strftime("%Y-%m-%d")

output = pairs[output_cols].sort_values(["posture", "state_code", "lag_days"])

csv_path = os.path.join(SCRIPT_DIR, "temporal_analysis_final.csv")
output.to_csv(csv_path, index=False)
print(f"\nWrote {len(output)} records to {csv_path}")

# ---------------------------------------------------------------------------
# 8. Compute summary statistics
# ---------------------------------------------------------------------------
# Convert lag_days back to numeric for statistics
output["lag_days"] = pd.to_numeric(output["lag_days"])

posture_groups = output.groupby("posture")["lag_days"]

summary_lines = []
summary_lines.append("# Temporal Correlation Analysis — Summary Report")
summary_lines.append("")
summary_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
summary_lines.append(f"**Total records:** {len(output)} state–federal-action pairs")
summary_lines.append("")
summary_lines.append("---")
summary_lines.append("")
summary_lines.append("## 1. Median Lag by Posture")
summary_lines.append("")
summary_lines.append(
    "| Posture | n (pairs) | Median Lag (days) | Mean Lag (days) | Min | Max |"
)
summary_lines.append(
    "|---------|-----------|-------------------|-----------------|-----|-----|"
)

for posture_name in ["Accommodate", "Push back", "Neutral/Mixed"]:
    subset = output[output["posture"] == posture_name]["lag_days"]
    if len(subset) > 0:
        summary_lines.append(
            f"| {posture_name} | {len(subset)} | {subset.median():.0f} | "
            f"{subset.mean():.1f} | {subset.min():.0f} | {subset.max():.0f} |"
        )
    else:
        summary_lines.append(f"| {posture_name} | 0 | — | — | — | — |")

summary_lines.append("")
summary_lines.append("---")
summary_lines.append("")
summary_lines.append("## 2. Proactive vs Reactive Freezes")
summary_lines.append("")
summary_lines.append(
    "A **negative lag** means the federal government acted *before* the state "
    "introduced legislation (proactive/preemptive). A **positive lag** means the "
    "federal action came *after* state legislation (reactive/retaliatory)."
)
summary_lines.append("")
summary_lines.append(
    "| Posture | Proactive (lag < 0) | Reactive (lag > 0) | Same-day (lag = 0) "
    "| % Proactive |"
)
summary_lines.append(
    "|---------|---------------------|--------------------|--------------------"
    "|-------------|"
)

for posture_name in ["Accommodate", "Push back", "Neutral/Mixed"]:
    subset = output[output["posture"] == posture_name]["lag_days"]
    if len(subset) > 0:
        n_neg = int((subset < 0).sum())
        n_pos = int((subset > 0).sum())
        n_zero = int((subset == 0).sum())
        pct = n_neg / len(subset) * 100
        summary_lines.append(
            f"| {posture_name} | {n_neg} | {n_pos} | {n_zero} | {pct:.1f}% |"
        )
    else:
        summary_lines.append(f"| {posture_name} | 0 | 0 | 0 | — |")

summary_lines.append("")
summary_lines.append("---")
summary_lines.append("")
summary_lines.append("## 3. State-Level Breakdown")
summary_lines.append("")
summary_lines.append(
    "| State | Code | Posture | Pairs | Median Lag | Proactive | Reactive |"
)
summary_lines.append(
    "|-------|------|---------|-------|------------|-----------|----------|"
)

state_summary = (
    output.groupby(["state", "state_code", "posture"])
    .agg(
        pairs=("lag_days", "count"),
        median_lag=("lag_days", "median"),
        proactive=("lag_days", lambda x: int((x < 0).sum())),
        reactive=("lag_days", lambda x: int((x > 0).sum())),
    )
    .reset_index()
    .sort_values(["posture", "state_code"])
)

for _, row in state_summary.iterrows():
    summary_lines.append(
        f"| {row['state']} | {row['state_code']} | {row['posture']} | "
        f"{row['pairs']} | {row['median_lag']:.0f} | "
        f"{row['proactive']} | {row['reactive']} |"
    )

summary_lines.append("")
summary_lines.append("---")
summary_lines.append("")
summary_lines.append("## 4. Interpretation")
summary_lines.append("")

# Compute key stats for the interpretation section
neutral_subset = output[output["posture"] == "Neutral/Mixed"]["lag_days"]
pushback_subset = output[output["posture"] == "Push back"]["lag_days"]
accommodate_subset = output[output["posture"] == "Accommodate"]["lag_days"]

neutral_median = neutral_subset.median() if len(neutral_subset) > 0 else None
pushback_median = pushback_subset.median() if len(pushback_subset) > 0 else None
accommodate_median = accommodate_subset.median() if len(accommodate_subset) > 0 else None

neutral_pct_proactive = (
    (neutral_subset < 0).mean() * 100 if len(neutral_subset) > 0 else 0
)
pushback_pct_proactive = (
    (pushback_subset < 0).mean() * 100 if len(pushback_subset) > 0 else 0
)

if neutral_median is not None and pushback_median is not None:
    summary_lines.append(
        f"- **Neutral/Mixed states** show a median lag of **{neutral_median:.0f} days**, "
        f"compared to **{pushback_median:.0f} days** for Push back states"
        + (
            f" and **{accommodate_median:.0f} days** for Accommodate states."
            if accommodate_median is not None
            else "."
        )
    )

if neutral_median is not None and neutral_median < 0:
    summary_lines.append(
        f"- The negative median lag for Neutral/Mixed states indicates that "
        f"federal funding actions **preceded** state legislation on average — "
        f"consistent with a **proactive pressure** strategy on undecided states."
    )
elif neutral_median is not None and neutral_median > 0:
    summary_lines.append(
        f"- The positive median lag for Neutral/Mixed states indicates that "
        f"federal funding actions followed state legislation on average — "
        f"consistent with a **reactive retaliation** strategy."
    )

summary_lines.append(
    f"- **{neutral_pct_proactive:.1f}%** of federal actions on Neutral/Mixed "
    f"states were proactive (negative lag) vs **{pushback_pct_proactive:.1f}%** "
    f"for Push back states."
)

summary_lines.append("")
summary_lines.append("### What the temporal data shows")
summary_lines.append("")
summary_lines.append(
    "The temporal lag analysis provides a timeline dimension to the statistical "
    "finding that Neutral/Mixed states face a 100% federal targeting rate on "
    "energy-specific withholding. By measuring whether federal actions came "
    "before or after state legislation:"
)
summary_lines.append("")
summary_lines.append(
    "1. **Negative lags (proactive freezes)** suggest the federal government "
    "applied pressure *before* states began legislating — consistent with a "
    "strategy of preemptive coercion aimed at influencing legislative outcomes."
)
summary_lines.append(
    "2. **Positive lags (reactive freezes)** suggest federal retaliation *after* "
    "states introduced restrictive or protective legislation — consistent with "
    "punitive action against states that did not fall in line."
)
summary_lines.append(
    "3. The **ratio of proactive to reactive** actions across posture groups "
    "reveals whether the federal approach is predominantly about prevention "
    "(freezing funds to discourage legislation) or punishment (freezing funds "
    "after legislation passes)."
)
summary_lines.append("")
summary_lines.append("---")
summary_lines.append("")
summary_lines.append(
    "*Analysis generated by `temporal_engine.py`. "
    "Data sources: Correlations/ and ANALYSIS/ folders.*"
)
summary_lines.append("")

# ---------------------------------------------------------------------------
# 9. Write temporal_summary.md
# ---------------------------------------------------------------------------
md_path = os.path.join(SCRIPT_DIR, "temporal_summary.md")
with open(md_path, "w") as f:
    f.write("\n".join(summary_lines))
print(f"Wrote summary to {md_path}")

# ---------------------------------------------------------------------------
# 10. Print quick console summary
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("QUICK SUMMARY")
print("=" * 60)
for posture_name in ["Accommodate", "Push back", "Neutral/Mixed"]:
    subset = output[output["posture"] == posture_name]["lag_days"]
    if len(subset) > 0:
        n_neg = int((subset < 0).sum())
        n_pos = int((subset > 0).sum())
        print(
            f"\n{posture_name} ({len(subset)} pairs):"
            f"\n  Median lag: {subset.median():.0f} days"
            f"\n  Proactive: {n_neg} ({n_neg/len(subset)*100:.1f}%)"
            f"\n  Reactive:  {n_pos} ({n_pos/len(subset)*100:.1f}%)"
        )
print("\nDone.")

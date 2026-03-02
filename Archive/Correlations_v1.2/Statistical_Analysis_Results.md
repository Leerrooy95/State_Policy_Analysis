# Statistical Analysis: Federal Funding Withholding vs State Data Center Policy Posture

**Analysis Date:** 2026-03-02  
**Analyst:** Claude (verified by Austin)  
**Data Sources:** Federal_Funding_Withholding_2025-2026.csv (30 events), state_posture_lookup.csv (26 states)

---

## Executive Summary

**Primary Finding:** No statistically significant correlation between federal funding withholding and state data center policy posture when examining ALL withholding events (p > 0.05 across multiple tests).

**Secondary Finding:** A notable pattern emerges when filtering to ENERGY/CLIMATE-SPECIFIC withholding — Neutral/Mixed states are targeted at 100%, suggesting a "pressure on the undecided" dynamic rather than direct punishment of resistance.

---

## State Posture Classifications

| Posture | Count | States |
|---------|-------|--------|
| Accommodate | 4 | AR, MS, NH, TX |
| Push back | 18 | AL, AZ, CT, DE, GA, ID, IL, MA, MD, NY, OH, OK, OR, SD, VA, VT, WA, WI |
| Neutral/Mixed | 4 | CO, MN, NJ, NM |

---

## Overall Targeting Results

### Federal Targeting Events by Posture

| Posture | n | Total Events | Mean Hits/State | Std Dev |
|---------|---|--------------|-----------------|---------|
| Accommodate | 4 | 6 | 1.50 | 1.12 |
| Push back | 18 | 40 | 2.22 | 2.12 |
| Neutral/Mixed | 4 | 15 | 3.75 | 1.48 |

### Statistical Tests (All Targeting)

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| t-test (Push back vs Accommodate) | t = 0.630 | 0.5360 | NO |
| Mann-Whitney U | U = 39.5 | 0.7923 | NO |
| One-way ANOVA (all 3 groups) | F = 1.336 | 0.2824 | NO |
| Chi-square (any targeting) | χ² = 1.034 | 0.5963 | NO |
| Point-biserial r | r = 0.139 | 0.5360 | NO |

**Conclusion:** No significant relationship between posture and overall federal targeting.

---

## Energy/Climate-Specific Targeting

When filtering to ENERGY-SPECIFIC withholding events (DOE grants, EPA climate programs, clean energy terminations), a pattern emerges:

### Energy Targeting Rate by Posture

| Posture | Energy Targeted | Not Targeted | Total | % Targeted |
|---------|-----------------|--------------|-------|------------|
| Accommodate | 1 (NH only) | 3 | 4 | 25.0% |
| Push back | 9 | 9 | 18 | 50.0% |
| Neutral/Mixed | 4 | 0 | 4 | **100.0%** |

### Statistical Tests (Energy-Specific)

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| Chi-square (all 3 groups) | χ² = 4.875 | **0.0874** | NO (but approaching) |
| Fisher's exact (Accommodate vs Push back) | OR = 0.333 | 0.5940 | NO |
| Fisher's exact (Accommodate vs non-Accommodate) | OR = 0.231 | 0.3061 | NO |

---

## Key Insight: "Pressure on the Undecided"

The energy-specific data suggests a possible **"swing state" targeting strategy**:

1. **Neutral/Mixed states** (CO, MN, NJ, NM) — **100% energy-targeted**
   - These states have competing legislation (incentives vs. restrictions)
   - Federal pressure may be aimed at tipping them toward accommodation

2. **Push back states** — **50% energy-targeted**
   - States actively resisting get hit, but not comprehensively
   - May be "cost of resistance" rather than targeted coercion

3. **Accommodate states** — **25% energy-targeted** (only NH)
   - States that comply largely avoided
   - NH exception is notable: HB 672 off-grid model bypasses federal infrastructure

### The NH Exception

New Hampshire is the only Accommodate state hit by energy withholding (DOE terminated Brayton Energy $5M grant, $43M Solar for All at risk).

**Hypothesis:** NH's HB 672 off-grid electricity provider law creates a model that **decouples from federal grid infrastructure entirely**. This may have drawn federal attention precisely because it offers an alternative path that doesn't require federal funding at all.

---

## Program Category Breakdown

| Category | Accommodate | Push back | Neutral/Mixed |
|----------|-------------|-----------|---------------|
| Energy/Climate | 2 | 10 | 4 |
| Immigration/Sanctuary | 0 | 12 | 6 |
| Disaster/FEMA | 0 | 5 | 3 |
| Education | 3 | 2 | 0 |
| Infrastructure | 0 | 0 | 0 |
| Other | 1 | 11 | 2 |

**Note:** Immigration/Sanctuary targeting correlates with Push back states, but this is a **confounding variable** — states that push back on data centers tend to be the same states with sanctuary policies.

---

## Limitations

1. **Small sample size** — Only 4 Accommodate states limits statistical power
2. **Confounding variables** — Political alignment correlates with both data center posture AND immigration/DEI policies
3. **Temporal analysis not performed** — Does targeting precede or follow policy decisions?
4. **Blanket freezes** — Many events hit "All States," diluting targeted analysis

---

## Recommendations for Further Analysis

1. **Expand Accommodate state classification** — Identify more states with pro-data center postures
2. **Temporal correlation** — Test lag between federal pressure and state legislation
3. **Control for political alignment** — Separate data center posture from broader state politics
4. **Track outcomes** — Which targeted states changed their posture afterward?

---

## Statistical Note

With the current effect size (2x higher targeting rate for Push back vs Accommodate), approximately **30 states per group** would be needed to achieve p < 0.05 significance. The current sample (4 Accommodate, 18 Push back) is underpowered.

However, the **100% targeting rate of Neutral/Mixed states** is directionally striking and warrants monitoring as more data accumulates.

---

*Analysis performed using Python (pandas, scipy.stats). Full code available in repository.*

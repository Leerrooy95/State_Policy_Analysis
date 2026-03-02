# Statistical Analysis Results — v1.4 (N=42 Recalculation)

**Generated:** March 2026  
**Dataset:** 42 federal funding withholding events (Jan 2025 – Feb 2026)  
**States Classified:** 27 (4 Accommodate, 19 Push back, 4 Neutral/Mixed)  
**Tools:** Python (pandas, scipy.stats, DoWhy causal inference)

---

## 1. Overall Targeting by Posture

| Posture | n (states) | Mean Events/State | Std Dev | Median | Min | Max |
|---------|------------|-------------------|---------|--------|-----|-----|
| Accommodate | 4 | 23.25 | 0.96 | 23.5 | 22 | 24 |
| Push back | 19 | 24.11 | 2.79 | 23.0 | 21 | 30 |
| Neutral/Mixed | 4 | 25.25 | 1.26 | 25.0 | 24 | 27 |

## 2. Statistical Tests — All Events

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| t-test (Push back vs Accommodate) | t = 1.071 | 0.3010 | **NO** |
| Mann-Whitney U (Push back vs Accommodate) | U = 36.5 | 0.9336 | **NO** |
| One-way ANOVA (all 3 groups) | F = 0.661 | 0.5253 | **NO** |
| Kruskal-Wallis (all 3 groups) | H = 2.564 | 0.2774 | **NO** |
| Chi-square (any targeting) | χ² = 0.909 | 0.6346 | **NO** |
| Point-biserial r (Push back vs Accommodate) | r = 0.129 | 0.5571 | **NO** |

**Result:** No statistically significant relationship between data center policy posture and overall federal funding targeting at any conventional significance level.

## 3. Energy-Specific Targeting

| Posture | States Hit | Total | % Targeted |
|---------|------------|-------|------------|
| Accommodate | 4 | 4 | **100%** |
| Push back | 19 | 19 | **100%** |
| Neutral/Mixed | 4 | 4 | **100%** |

| Test | Statistic | p-value |
|------|-----------|---------|
| ANOVA (energy events by posture) | F = 0.741 | 0.4873 |
| Kruskal-Wallis (energy events) | H = 1.689 | 0.4299 |

**Result:** ALL 27 classified states (100% of every posture group) experienced energy-related federal funding impacts. No statistically significant difference in energy targeting by posture.

**v1.2 Correction:** The previous finding that "100% of Neutral/Mixed states were hit by energy targeting vs 50% of Push back and 25% of Accommodate" was an artifact of the smaller N=30 dataset. With N=42, this distinction no longer exists.

## 4. Targeted (Non-Blanket) Events by Posture

| Posture | Mean Targeted Events | Median | Std Dev |
|---------|---------------------|--------|---------|
| Accommodate | 2.25 | 2.5 | 0.96 |
| Push back | 3.05 | 2.0 | 2.68 |
| Neutral/Mixed | 4.25 | 4.0 | 1.26 |

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| ANOVA | F = 0.723 | 0.4956 | **NO** |
| Kruskal-Wallis | H = 2.565 | 0.2773 | **NO** |

**Result:** Neutral/Mixed states do show a slightly higher mean of targeted events (4.25 vs 2.25–3.05), but this difference is **not statistically significant**. The variation within the Push back group (std=2.68) is larger than the between-group differences.

## 5. Effect Sizes

| Metric | Eta-squared | Interpretation |
|--------|------------|----------------|
| Total events | 0.0522 | Small |
| Energy events | 0.0582 | Small |

Both effect sizes fall below the conventional threshold for "medium" effects (0.06), indicating that data center posture explains very little of the variance in federal targeting.

## 6. Blanket vs. Targeted Events

| Type | Count | % of Total |
|------|-------|------------|
| Blanket ("All States") | 22 | 52.4% |
| Targeted (specific states) | 20 | 47.6% |

The majority of federal funding actions are blanket actions that affect all states equally, which is the primary driver of the high and uniform event counts across all posture groups.

## 7. Cross-Party Impact Summary

| State | Code | Posture | Political Alignment | Total Events | Targeted | Energy |
|-------|------|---------|-------------------|--------------|----------|--------|
| Arkansas | AR | Accommodate | Red | 23 | 2 | 9 |
| Texas | TX | Accommodate | Red | 24 | 3 | 10 |
| Oklahoma | OK | Push back | Red | 23 | 2 | 9 |
| New Hampshire | NH | Accommodate | Purple | 24 | 3 | 11 |
| Mississippi | MS | Accommodate | Red | 22 | 1 | 9 |
| Alabama | AL | Push back | Red | 21 | 0 | 9 |
| South Dakota | SD | Push back | Red | 22 | 1 | 10 |
| Idaho | ID | Push back | Red | 22 | 1 | 9 |

**Result:** Politically aligned states experience the same types and rates of federal funding actions as politically opposing states. The data does not support a purely partisan targeting interpretation.

## 8. Temporal Lag Analysis — Updated with Methodological Correction

### Raw Results (N=42)

| Posture | n (pairs) | Median Lag (days) | % Proactive |
|---------|-----------|-------------------|-------------|
| Accommodate | 47 | −18 | 53.2% |
| Push back | 326 | −74 | 53.7% |
| Neutral/Mixed | 101 | +92 | 12.9% |

### Critical Methodological Finding

The apparent difference in lag times between posture groups is **entirely driven by when states introduced their data center legislation**, not by differential federal behavior.

**Evidence:**

1. **Trigger date confound:** All 4 Neutral/Mixed states (CO, MN, NJ, NM) have early trigger dates (Jan–Jun 2025). Push back states are split between early (2025) and late (Jan–Feb 2026) trigger dates. This mechanically produces positive lags for Neutral/Mixed and negative lags for late-legislating Push back states.

2. **Controlled comparison:** When comparing only states with the same trigger date (2025-01-01), Push back and Neutral/Mixed states show **identical** median lags of 113 days (Mann-Whitney U p = 0.7677).

3. **DoWhy causal model with trigger date control:** When trigger_date is added as a confounder, the estimated causal effect drops from **+148 days (p < 0.0001)** to **0.00 days (p = 1.000)** — exactly zero effect.

| Model | Causal Effect | p-value | Significant? |
|-------|--------------|---------|--------------|
| Original (no trigger date control) | +148.02 days | < 0.0001 | YES |
| **Corrected (with trigger date control)** | **0.00 days** | **1.000** | **NO** |

**v1.2/v1.3 Correction:** The previous finding of a +151-day causal effect (p < 0.0001) was a confounded result. The temporal lag difference between posture groups is a methodological artifact, not evidence of differential federal behavior.

## 9. Summary of Findings

### What the data supports

1. **No significant correlation** between data center policy posture and federal funding targeting (all tests non-significant, all p > 0.27)
2. **Universal impact** — All states regardless of posture experience energy-related federal funding actions
3. **Cross-party impact** — Politically aligned states are hit at comparable rates to opposing states
4. **Blanket actions dominate** — 52% of events affect all states equally
5. **Small effect sizes** — Posture explains less than 6% of the variance in targeting

### What the data does NOT support

1. ~~"Pressure on the undecided"~~ — The apparent higher targeting of Neutral/Mixed states is not statistically significant
2. ~~"100% energy targeting of Neutral/Mixed vs 25-50% of others"~~ — Artifact of smaller N=30 dataset; all groups are 100% hit
3. ~~"Reactive retaliation" temporal pattern~~ — Entirely driven by trigger date differences, not federal behavior
4. ~~"+151-day causal effect"~~ — Confounded by trigger dates; corrected estimate is zero

### What remains open

1. The **5 most-targeted states** (CA=30, IL=29, OR=28, CO/MA/WA=27, NY=26) are primarily targeted for immigration/sanctuary policy positions, not data center posture — this correlation deserves further analysis
2. Small group sizes (n=4) in Accommodate and Neutral/Mixed groups limit statistical power; effects too small to detect with current data cannot be ruled out
3. The five-stage escalation timeline is a reasonable descriptive framework but should not be interpreted as evidence of intentional targeting based on data center posture

---

*Statistical analysis performed with Python (pandas 3.0, scipy 1.15, DoWhy 0.14). All code and data available in the `Correlations/` directory.*

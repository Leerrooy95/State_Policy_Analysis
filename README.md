# State Policy Analysis v1.3

**A data-driven examination of how U.S. states are responding to the data center and energy infrastructure boom — from regulatory accommodation to outright moratoriums — now including statistical correlation analysis of federal funding withholding patterns.**

---

## Overview

This repository documents the divergent state-level policy responses to the rapid expansion of data center infrastructure across the United States. The analysis focuses on the legislative, regulatory, and capital architecture that enables — or restricts — large-scale data center and energy projects, with a particular emphasis on Arkansas as a case study.

The core finding: **states are splitting into two camps** — those that actively reshape laws to accommodate data center and energy expansion (e.g., Arkansas, New Hampshire), and those that are pushing back through moratoriums, ratepayer protections, and tax incentive rollbacks (e.g., Virginia, Oklahoma, New York, Georgia, Vermont, Maryland).

**New in v1.3:** Expanded federal funding withholding dataset from N=30 to N=42 events — adding 12 new verified events covering DOE Loan Programs Office freeze ($41.2B), DOE hydrogen hub terminations (all 7 hubs, $7B), FEMA disaster declaration denials (AR, WV, WA), FEMA hazard mitigation denials (IA, MS, MO, OK), EPA Environmental Finance Center cancellations, DOT formula funding delays ($38.5B), IRA clean energy tax credit phase-out (OBBBA), and more. Legacy v1.2 analysis outputs archived. Previous v1.2 statistical findings (N=30) require recalculation against expanded dataset.

## What's in This Repository

| Folder | Contents |
|--------|----------|
| [`01_The_Baseline/`](01_The_Baseline/) | Original research files documenting Arkansas's legislative architecture (Act 373, Act 548), the DATA Act of 2026, NH HB 672, AVAIO Digital, and capital flows |
| [`02_CSVs_and_Datasets/`](02_CSVs_and_Datasets/) | Structured CSV data organized by state — legislation, energy statistics, capital investments, cross-state comparisons, and expanded 27-state posture classifications |
| [`ANALYSIS/`](ANALYSIS/) | Consolidated analysis CSVs for 6 target states (AR, TX, OK, NY, VA, CA) — energy profiles, legislation tracker, capital flows, federal impact summaries, and posture lookup |
| [`Correlations/`](Correlations/) | Federal funding withholding data (42 events), temporal lag engine, independent causal verification scripts |
| [`Archive/`](Archive/) | Legacy v1.2 analysis outputs (N=30 statistical results, temporal summaries, intermediate working files) archived during v1.3 upgrade |
| [`Report.md`](Report.md) | Full detailed findings report with verification status, multi-source citations, correlation analysis, and structural pattern analysis |

## Key Findings

### Verified Claims

- **Arkansas Act 373 (SB 307)** — Creates an iterative resubmission mechanism where the PSC cannot permanently deny utility projects. Signed March 20, 2025 with emergency clause. *(Sources: Arkansas Legislature, BillTrack50, Talk Business & Politics)*

- **Arkansas Act 548 (HB 1444)** — Reduces data center investment threshold from $500M to $100M, creates a "Qualified Large Data Center" category requiring $2B across "two or more nonadjacent" locations. Signed April 10, 2025. *(Sources: Kutak Rock, BillTrack50, Arkansas Legislature)*

- **DATA Act of 2026 (S. 3585)** — Sen. Tom Cotton's bill creating "Consumer-Regulated Electric Utility" (CREU) category exempt from FERC/FPA/PURPA/PUHCA oversight for physically islanded systems. *(Sources: Cotton.senate.gov, Reason, NWA Democrat-Gazette)*

- **ALEC Model Legislation** — ALEC released model CREU legislation for states to adopt, directly mirroring the DATA Act. *(Source: ALEC.org)*

- **NH HB 672** — Created "off-grid electricity provider" category exempt from state utility regulation. Effective August 1, 2025. *(Sources: BillTrack50, NH Legislature)*

- **AVAIO Digital Leo** — $6B phase one / $21B total buildout in Little Rock, AR. 760 acres, 150MW initial power from Entergy Arkansas scaling to 1GW. *(Source: AVAIO Digital / PRNewswire)*

- **ADQ/ECP Partnership** — $25B (50-50), $5B initial capital, targeting 25+ GW of US power generation for data centers. Announced March 2025. *(Source: ADQ.ae official press release)*

### States Pushing Back (2026 Legislative Session)

By February 2026, **300+ data center bills** had been filed across **30+ states** in just six weeks (MultiState, Feb 2026):

| State | Action | Key Bills |
|-------|--------|-----------|
| **New York** | 3-year moratorium proposed | A 10141 / S9144 |
| **Oklahoma** | Moratorium + ratepayer protection | SB 1488, HB 2992 |
| **Virginia** | Moratorium + tax incentive rollback | HB 1515, HB 961, HB 897 |
| **Georgia** | 1-year moratorium + eliminate tax credits | SB 476 |
| **Vermont** | Moratorium until July 2030 | S.205 |
| **Maryland** | Emergency moratorium bill | HB 120 |
| **South Dakota** | 1-year moratorium on hyperscale | SB 232 |

### States Accommodating Expansion

| State | Action | Key Laws |
|-------|--------|----------|
| **Arkansas** | PSC bypass, tax incentives, expedited approval | Act 373, Act 548 |
| **New Hampshire** | Off-grid provider exemption from utility regulation | HB 672 |
| **Texas** | Pro-data-center, state preempts local moratoriums | HB 2559 |

## Correlation Analysis: Federal Funding Withholding vs. State Policy Posture

### Statistical Findings

Analysis of 42 federal funding withholding events (Jan 2025 – Feb 2026) against 26 states classified by data center policy posture (Accommodate, Push back, Neutral/Mixed). The v1.3 dataset expands coverage by 40%, adding DOE, EPA, FEMA, and DOT actions previously undocumented:

| Finding | Result |
|---------|--------|
| **Overall correlation (v1.2, N=30)** | No statistically significant relationship between posture and overall federal targeting (ANOVA F = 1.336, p = 0.2824) — **pending recalculation with N=42** |
| **Energy-specific targeting (v1.2)** | 100% of Neutral/Mixed states (CO, MN, NJ, NM) hit by energy-specific withholding vs. 50% of Push back and 25% of Accommodate states — **pending recalculation** |
| **"Pressure on the undecided"** | Neutral/Mixed states — those with competing incentive vs. restriction legislation — are targeted at the highest rate, suggesting a swing-state coercion dynamic |
| **New in v1.3: Cross-party FEMA denials** | FEMA denied disaster aid to AR (tornado) and OK (hazard mitigation) — both Accommodate/Push back states — alongside WA and WV, demonstrating FEMA policy shift affects all political alignments |
| **New in v1.3: DOE hydrogen hub terminations** | All 7 regional hydrogen hubs ($7B) terminated, including hubs in TX and LA (red states), suggesting energy policy cancellations extend beyond partisan targeting |

### Temporal Lag Analysis

Measuring the time gap between state legislation and federal funding actions across 346 state–federal-action pairs:

| Posture | Median Lag (days) | % Proactive (federal acted first) | Interpretation |
|---------|-------------------|-----------------------------------|----------------|
| Accommodate | −19 | 57.6% | Slight federal preemption |
| Push back | −74 | 53.4% | Mix of preemptive and reactive |
| Neutral/Mixed | +92 | 13.3% | Federal actions overwhelmingly follow state legislation — consistent with reactive retaliation |

### Causal Verification

An independent causal model (DoWhy framework) estimates that adopting a "Neutral/Mixed" posture changes the federal action lag by **+150.98 days** (p < 0.0001). Refutation tests confirm robustness: a random common cause barely shifts the estimate (150.77), and a placebo treatment reduces it to near-zero (4.87).

### Five-Stage Federal Targeting Pattern

| Stage | Timing | Action | Who's Hit |
|-------|--------|--------|-----------|
| 1. Blanket Freeze | Jan 2025 | EO-driven IIJA/IRA/OMB pauses | All 50 states |
| 2. Selective Enforcement | Feb–Apr 2025 | Sanctuary conditions, FEMA continued freeze | Blue states + sanctuary cities |
| 3. Compliance Ultimatums | Jun–Aug 2025 | PREP gender identity, education DEI | 40+ states warned; CA terminated first |
| 4. Targeted Terminations | Aug–Oct 2025 | NIH, DOE clean energy, MSI grants | CA (NIH), 16 blue states (DOE) |
| 5. Selective Release | Feb 2026 | FEMA disaster aid released to some, not others | CA, IL, MN, CO excluded |

**Critical insight:** Even politically aligned states suffered significant withholding — TX ($700M education), AR ($64M education + tornado aid denied), OK ($70M education + $6.3B Medicaid hospital cuts + hazard mitigation denied). The v1.3 dataset strengthens this finding: FEMA denied disaster declarations for AR (Accommodate) and WA/WV (non-data-center states), while DOE hydrogen hub terminations hit TX and LA alongside blue states. The difference appears at Stage 5 (selective release), where red/swing states are restored more quickly.

## For Deeper Context

This repository is a companion to [The Regulated Friction Project](https://github.com/Leerrooy95/The_Regulated_Friction_Project), which examines these dynamics at the geopolitical level — documenting how timed information disclosure regulates public attention to enable structural shifts in policy and capital flows.

## Data Sources

All findings are cross-referenced from multiple non-partisan sources:

- **Federal/State Legislature**: Cotton.senate.gov, Arkansas Legislature (arkleg.state.ar.us), NH Legislature, Oklahoma Legislature, Virginia LIS
- **Legal Analysis**: Kutak Rock, BillTrack50, LegiScan
- **Energy Data**: U.S. Energy Information Administration (EIA)
- **Industry**: Data Center Dynamics, Utility Dive, ALEC
- **Press**: PRNewswire (AVAIO), ADQ.ae, Reason, NWA Democrat-Gazette, Arkansas Advocate, Talk Business & Politics
- **Policy**: MultiState Policy Watch, Pew Research Center, Built In, KERA News
- **Federal Funding Data**: OMB, EPA, DOE, DOJ, DOT, FEMA, HHS, NTIA official releases; court filings; GAO reports; NACo Federal Funds Tracker; CBPP withholding analysis; Heatmap News; Utility Dive; Semafor
- **Correlation Analysis**: Python (pandas, scipy.stats, DoWhy causal inference); all statistical code available in `Correlations/`
- **Infrastructure Tracking**: Georgetown Climate Center transportation funding explainer; Eno Center for Transportation; Federal Highway Administration

## Methodology

- Claims are verified against primary legislative text, official press releases, and government data where possible
- Secondary sources (news coverage, legal analysis) are used for context and confirmation
- Where verification is partial or unavailable, the claim is explicitly marked
- No single partisan source is treated as authoritative; findings require multi-source confirmation
- Analysis distinguishes between **verified facts** (legislation text, official data), **structural observations** (pattern analysis), and **unconfirmed hypotheses**

---

*Repository maintained by Austin ([Leerrooy95](https://github.com/Leerrooy95))*
*Last updated: March 2026 — v1.3*

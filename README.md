# State Policy Analysis v1.4

**A data-driven examination of how U.S. states are responding to the data center and energy infrastructure boom — from regulatory accommodation to outright moratoriums — with rigorous statistical analysis of federal funding withholding patterns.**

---

## Overview

This repository documents the divergent state-level policy responses to the rapid expansion of data center infrastructure across the United States. The analysis focuses on the legislative, regulatory, and capital architecture that enables — or restricts — large-scale data center and energy projects, with a particular emphasis on Arkansas as a case study.

The core finding: **states are splitting into two camps** — those that actively reshape laws to accommodate data center and energy expansion (e.g., Arkansas, New Hampshire), and those that are pushing back through moratoriums, ratepayer protections, and tax incentive rollbacks (e.g., Virginia, Oklahoma, New York, Georgia, Vermont, Maryland).

**New in v1.4:** All statistical tests recalculated against the expanded N=42 federal funding dataset (42 events, 27 states). Key corrections from v1.2/v1.3: (1) No significant correlation between data center posture and federal targeting — confirmed with 6 statistical tests, all p > 0.27; (2) The "100% Neutral/Mixed energy targeting" finding was an artifact of the smaller N=30 dataset — with N=42, 100% of ALL posture groups are hit equally; (3) The temporal lag "reactive retaliation" finding was a methodological artifact driven by when states introduced legislation, not federal behavior — DoWhy causal effect drops from +148 days to 0.00 when trigger dates are controlled; (4) Cross-party impact is the strongest confirmed finding — AR, TX, OK, NH all experienced significant federal withholding alongside opposing states.

## What's in This Repository

| Folder | Contents |
|--------|----------|
| [`01_The_Baseline/`](01_The_Baseline/) | Original research files documenting Arkansas's legislative architecture (Act 373, Act 548), the DATA Act of 2026, NH HB 672, AVAIO Digital, and capital flows |
| [`02_CSVs_and_Datasets/`](02_CSVs_and_Datasets/) | Structured CSV data organized by state — legislation, energy statistics, capital investments, cross-state comparisons, and expanded 27-state posture classifications |
| [`ANALYSIS/`](ANALYSIS/) | Consolidated analysis CSVs for 6 target states (AR, TX, OK, NY, VA, CA) — energy profiles, legislation tracker, capital flows, federal impact summaries, and posture lookup |
| [`Correlations/`](Correlations/) | Federal funding withholding data (42 events), v1.4 statistical analysis results, temporal lag engine, causal verification scripts |
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

### Statistical Findings (v1.4 — Recalculated, N=42)

Analysis of 42 federal funding withholding events (Jan 2025 – Feb 2026) against 27 states classified by data center policy posture (Accommodate, Push back, Neutral/Mixed):

| Finding | Result |
|---------|--------|
| **Overall correlation** | No statistically significant relationship — ANOVA F=0.661, p=0.5253; Kruskal-Wallis H=2.564, p=0.2774; all 6 tests non-significant (all p > 0.27) |
| **Effect sizes** | Small — eta-squared = 0.052 (total events), 0.058 (energy events); posture explains less than 6% of variance |
| **Energy-specific targeting** | 100% of ALL posture groups hit equally — the v1.2 finding of differential energy targeting was an artifact of the smaller N=30 dataset |
| **Blanket vs. targeted** | 22 of 42 events (52%) are blanket "All States" actions — this is the dominant pattern |
| **Cross-party impact** | Both politically aligned and opposing states are hit at comparable rates — AR, TX, OK, NH all experienced significant withholding |
| **Most-targeted states** | CA (30), IL (29), OR (28), CO/MA/WA (27), NY (26) — primarily targeted for immigration/sanctuary/DEI policies, not data center posture |

### v1.2/v1.3 Corrections

| Previous Finding | v1.4 Status |
|-----------------|-------------|
| "100% of Neutral/Mixed states hit by energy targeting vs 25-50% of others" | **CORRECTED** — All groups are 100% hit with N=42 |
| "Temporal lag shows reactive retaliation on Neutral/Mixed states (+92 days)" | **CORRECTED** — Driven by legislation timing, not federal behavior; controlled DoWhy effect = 0.00 days, p=1.000 |
| "+151-day causal effect (p < 0.0001)" | **CORRECTED** — Confounded by trigger dates; corrected estimate is zero |
| "Pressure on the undecided" | **NOT SUPPORTED** — Differences are not statistically significant |

### Temporal Lag Analysis (Corrected)

The v1.4 analysis identified a critical methodological issue in the temporal lag calculations: the apparent difference in federal response timing between posture groups was entirely driven by when states introduced their data center legislation (trigger dates), not by differential federal behavior. When controlling for trigger dates:

- States with the same trigger date show **identical** lag patterns regardless of posture (Mann-Whitney U p=0.768)
- DoWhy causal effect drops from +148 days to **0.00 days** when trigger date is included as a confounder

### Five-Stage Federal Action Timeline

| Stage | Timing | Action | Who's Hit |
|-------|--------|--------|-----------|
| 1. Blanket Freeze | Jan 2025 | EO-driven IIJA/IRA/OMB pauses | All 50 states |
| 2. Selective Enforcement | Feb–Apr 2025 | Sanctuary conditions, FEMA continued freeze | Blue states + sanctuary cities |
| 3. Compliance Ultimatums | Jun–Aug 2025 | PREP gender identity, education DEI | 40+ states warned; CA terminated first |
| 4. Targeted Terminations | Aug–Oct 2025 | NIH, DOE clean energy, MSI grants | CA (NIH), 16 blue states (DOE) |
| 5. Selective Release | Feb 2026 | FEMA disaster aid released to some, not others | CA, IL, MN, CO excluded |

**Key finding:** The selective enforcement (Stages 2–5) correlates with immigration/sanctuary and DEI policy positions, not with data center policy posture. Even politically aligned states suffered significant withholding — TX ($700M education), AR ($64M education + tornado aid denied), OK ($70M education + hazard mitigation denied). The difference appears at Stage 5, where red/swing states tend to be restored more quickly — but this correlates with political alignment broadly, not data center posture specifically.

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
- **Correlation Analysis**: Python (pandas 3.0, scipy 1.15, DoWhy 0.14 causal inference); all statistical code and results available in `Correlations/`
- **Infrastructure Tracking**: Georgetown Climate Center transportation funding explainer; Eno Center for Transportation; Federal Highway Administration

## Methodology

- Claims are verified against primary legislative text, official press releases, and government data where possible
- Secondary sources (news coverage, legal analysis) are used for context and confirmation
- Where verification is partial or unavailable, the claim is explicitly marked
- No single partisan source is treated as authoritative; findings require multi-source confirmation
- Analysis distinguishes between **verified facts** (legislation text, official data), **structural observations** (pattern analysis), and **unconfirmed hypotheses**
- Statistical findings are reported with full test statistics, p-values, and effect sizes; corrections to prior findings are explicitly documented
- Prior findings that were artifacts of methodology or small samples are transparently corrected, not hidden

---

*Repository maintained by Austin ([Leerrooy95](https://github.com/Leerrooy95))*
*Last updated: March 2026 — v1.4*

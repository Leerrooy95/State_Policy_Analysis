# State Policy Analysis — Full Findings Report (v1.4)

**Date:** March 2026
**Version:** 1.4
**Scope:** State-level policy responses to data center and energy infrastructure expansion across the United States, with federal funding withholding correlation analysis
**Methodology:** Multi-source web research, legislative text analysis, EIA energy data, statistical correlation (scipy.stats), temporal lag analysis, and causal inference (DoWhy)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Arkansas: The Accommodation Model](#2-arkansas-the-accommodation-model)
3. [The DATA Act of 2026 and Federal Framework](#3-the-data-act-of-2026-and-federal-framework)
4. [New Hampshire HB 672: The State Precedent](#4-new-hampshire-hb-672-the-state-precedent)
5. [Capital Architecture: Who Is Funding the Buildout](#5-capital-architecture-who-is-funding-the-buildout)
6. [States Pushing Back: Moratoriums and Ratepayer Protections](#6-states-pushing-back-moratoriums-and-ratepayer-protections)
7. [States Accommodating Expansion](#7-states-accommodating-expansion)
8. [Energy Data and Cost Comparisons](#8-energy-data-and-cost-comparisons)
9. [The Two-Camp Split: Structural Analysis](#9-the-two-camp-split-structural-analysis)
10. [Federal Funding Withholding: Correlation Analysis](#10-federal-funding-withholding-correlation-analysis)
11. [State-by-State Federal Impact Assessment](#11-state-by-state-federal-impact-assessment)
12. [Open Questions and Unresolved Threads](#12-open-questions-and-unresolved-threads)
13. [Sources](#13-sources)

---

## 1. Executive Summary

The United States is experiencing a historic divergence in state-level energy and technology infrastructure policy. Driven by surging data center demand — fueled by AI, cloud computing, and hyperscale operations — states are splitting into two distinct camps:

**Camp A — Accommodation:** States actively reshaping laws to attract and enable data center expansion through regulatory streamlining, tax incentives, and utility bypass mechanisms. Arkansas and New Hampshire are the clearest examples.

**Camp B — Pushback:** States introducing moratoriums, ratepayer protections, tax incentive rollbacks, and environmental reviews to slow or regulate data center expansion. Virginia, Oklahoma, New York, Georgia, Vermont, and Maryland lead this group.

By February 2026, **more than 300 state data center bills** had been filed across **30+ states** in just six weeks, according to MultiState Policy Watch — a dramatic shift from the incentive-focused policies of prior years toward regulatory oversight.

At the federal level, the DATA Act of 2026 (Sen. Tom Cotton) and ALEC model legislation are creating a framework for "Consumer-Regulated Electric Utilities" (CREUs) — physically islanded power systems exempt from federal regulation — that could fundamentally restructure how large energy consumers interact with the grid.

**New in v1.4 — Recalculated Statistical Analysis (N=42):** All statistical tests from v1.2 (N=30) have been recalculated against the expanded N=42 dataset (42 federal funding events, 27 classified states). Key corrections:

1. **No significant correlation confirmed** — ANOVA (F=0.661, p=0.5253), Kruskal-Wallis (H=2.564, p=0.2774), t-tests, chi-square, and Mann-Whitney U all remain non-significant. Data center policy posture does not predict federal funding targeting.
2. **"100% Neutral/Mixed energy targeting" finding corrected** — With N=42, 100% of ALL posture groups (Accommodate, Push back, and Neutral/Mixed) are hit by energy-related federal actions. The v1.2 finding was an artifact of the smaller dataset.
3. **Temporal lag finding corrected** — The v1.2 apparent difference in federal response timing between posture groups was entirely driven by when states introduced their legislation, not by differential federal behavior. When controlling for trigger dates, the DoWhy causal effect drops from +148 days (p < 0.0001) to **0.00 days (p = 1.000)**.
4. **Cross-party impact verified** — AR ($64M education + tornado denial), TX ($700M education + hydrogen hub), OK ($70M education + hazard mitigation denied), NH ($27M education + DOE grant terminated) — politically aligned states are hit at comparable rates to opposing states. 52% of all events are blanket "All States" actions.

The v1.2 narrative of "pressure on the undecided" is not supported by the recalculated data. The dominant pattern is one of broad federal austerity and policy realignment affecting all states, with targeted actions driven primarily by immigration/sanctuary policy positions rather than data center posture.

---

## 2. Arkansas: The Accommodation Model

### 2.1 Act 373 — The "Generating Arkansas Jobs Act of 2025"

**Status: ✅ VERIFIED**

Act 373 (originally SB 307), sponsored by Sen. Jonathan Dismang (R-Searcy), was signed into law on **March 20, 2025** with an emergency clause making it effective immediately.

**Key Provisions (verified via BillTrack50, Arkansas Legislature, Talk Business & Politics):**

| Feature | Detail |
|---------|--------|
| **Rider mechanism** | Creates a "rider" allowing utilities to recover construction costs incrementally during construction |
| **Strategic investments** | Broadly defined to include new generation, transmission, energy storage, nuclear license extensions, and feasibility studies for advanced technologies |
| **Iterative resubmission** | If PSC denies a certificate, the utility may resubmit with additional evidence; PSC must rule within 30 days. Process "may continue until" approval, withdrawal, or appeal — no provision for final denial |
| **Auto-approval** | If PSC fails to act within statutory deadlines, filing becomes effective by operation of law |
| **6-month timeline** | PSC must act within 6 months on certificate applications |
| **Rate cap** | Rates cannot exceed 10% below national average, with economic development exceptions |
| **Wind exclusion** | Wind resources in Arkansas explicitly excluded from "strategic investments" |
| **Emergency clause** | Effective immediately upon signing (March 20, 2025) |

**Legislative History:** SB 307 initially **failed** on the Senate floor on March 5, 2025, falling one vote short (17-11). Sen. Dismang moved to expunge the vote, amended the bill, and it passed March 12 (23-9). The House passed it 77-13 on March 18.

Sen. Reginald Murdock (D), a co-sponsor, stated the bill "was pushed through too fast." Industrial manufacturers (Arkansas Electric Energy Consumers) and forestry/paper processors opposed the bill.

**Sources:**
- BillTrack50: AR SB307 / Act 373 — billtrack50.com/billdetail/1845892
- Talk Business & Politics: "Power generation bill fails in senate by one vote" — talkbusiness.net (March 2025)
- Arkansas Legislature: arkleg.state.ar.us

### 2.2 Act 548 — Data Center Tax Incentive Framework

**Status: ✅ VERIFIED**

Act 548 (HB 1444), signed **April 10, 2025**, amends Arkansas's data center sales and use tax exemption.

**Key Provisions (verified via Kutak Rock legal analysis, BillTrack50):**

| Feature | Detail |
|---------|--------|
| **Reduced threshold** | Qualified Data Center investment reduced from $500M to $100M |
| **New "Large" category** | "Qualified Large Data Center" requires $2B investment within 10 years across "two or more nonadjacent physical locations" connected by fiber |
| **Fiber tax exemption** | Connecting fiber infrastructure between sites is itself tax-exempt |
| **Crypto exclusion** | Cryptocurrency mining operations explicitly excluded |
| **Compliance shift** | Oversight moves from AEDC to Department of Finance and Administration |
| **Fallback provision** | Individual sites that meet $100M threshold retain exemption even if aggregate $2B threshold is not met |

Kutak Rock's legal analysis confirms: "A 'qualified large data center' essentially is an interconnected data center comprised of two or more nonadjacent locations." Rep. Aaron Pilkington (R-Knoxville), the sponsor, acknowledged having "a couple projects in mind" when crafting the bill.

**Sources:**
- Kutak Rock: "Expansion of the Sales and Use Tax Data Center Exemption" — kutakrock.com (April 2025)
- BillTrack50: AR HB1444 / Act 548 — billtrack50.com/billdetail/1826317

### 2.3 Jefferson Power Station (PSC Docket 25-047-U)

**Status: ✅ VERIFIED (via baseline files, corroborated by multiple Arkansas press sources)**

The Arkansas PSC approved Entergy Arkansas's $1.5B Jefferson Power Station on January 28, 2026, **despite finding the cost "not reasonable."** Expert witnesses for both the Attorney General and PSC staff recommended denial. The approval illustrates Act 373's structural effect — the iterative resubmission mechanism made permanent denial procedurally impractical.

### 2.4 AVAIO Digital Leo — Little Rock Campus

**Status: ✅ VERIFIED**

| Detail | Verified Finding |
|--------|-----------------|
| **Project** | AVAIO Digital Leo |
| **Location** | 760-acre site, Pulaski County, south of Little Rock |
| **Phase 1 investment** | $6 billion (AVAIO + customers) |
| **Total buildout** | $21 billion |
| **Initial power** | 150 MW from Entergy Arkansas |
| **Target capacity** | Up to 1 GW |
| **Construction start** | Q1 2026 |
| **Phase 1 completion** | June 2027 |
| **Jobs** | 500+ permanent operations; thousands during construction |

Gov. Sanders called it "the largest economic investment in Arkansas' history." AVAIO CEO Mark McComiskey confirmed the $21B total buildout figure.

**Source:** AVAIO Digital / PRNewswire official release (January 2026)

### 2.5 League of Women Voters v. Jester

**Status: ✅ VERIFIED (via baseline files)**

Case No. 25-3389 in the 8th Circuit challenges Arkansas laws restricting the citizen ballot initiative process. The district court issued a 77-page opinion enjoining enforcement of multiple 2025 acts. The 8th Circuit denied the emergency stay on December 12, 2025. The case is relevant because the ballot initiative is the democratic mechanism that could override Acts 373 and 548. Trial is set for July 20, 2026 — after the July 3 signature submission deadline.

---

## 3. The DATA Act of 2026 and Federal Framework

### 3.1 The DATA Act (S. 3585)

**Status: ✅ VERIFIED**

Sen. Tom Cotton (R-AR) introduced the Decentralized Access to Technology Alternatives (DATA) Act on January 7, 2026. The bill creates a **Consumer-Regulated Electric Utility (CREU)** category — physically islanded power systems exempt from federal regulation.

**Key Provisions (verified via Cotton.senate.gov, Reason, ALEC):**

| Feature | Detail |
|---------|--------|
| **CREU definition** | Electric generation/supply system for new nonresidential loads, physically islanded from the bulk power grid |
| **FERC exemption** | CREUs exempt from FERC, FPA, PURPA, PUHCA oversight |
| **Islanding requirement** | Must be completely physically isolated from the grid |
| **Loss of exemption** | Any grid connection immediately terminates CREU status |
| **Environmental laws** | Still subject to environmental, safety, and workplace regulations |
| **State laws** | Still subject to state utility laws |

Cotton's office stated: "American dominance in artificial intelligence and other crucial emerging industries should not come at the expense of Arkansans paying higher energy costs."

Travis Fisher (Cato Institute) noted the bill would let companies avoid "the studies that you would need to do to interconnect to the system. Those are on notorious backlogs...in some areas, they're more like four to six years."

**Sources:**
- Cotton.senate.gov: Official press release and bill text (January 8, 2026)
- Reason: "Data centers use lots of electricity. This bill would let them go off the grid" (January 9, 2026)
- NWA Democrat-Gazette: Alex Thomas reporting (January 7, 2026)

### 3.2 ALEC Model Legislation

**Status: ✅ VERIFIED**

The American Legislative Exchange Council (ALEC) released model legislation titled "Act to Allow for Consumer Regulated Electric Utilities" in January 2026, directly mirroring the DATA Act's CREU framework. The model legislation provides a template for states to adopt the same exempt utility category.

Key language from the ALEC model: "A CREU shall not be considered a public utility for purposes of public utility regulation." And: "If a CREU elects to interconnect with a system subject to public utility regulation...it shall cease to be a CREU."

**Source:** ALEC.org — alec.org/model-policy/act-to-allow-for-consumer-regulated-electric-utilities/

---

## 4. New Hampshire HB 672: The State Precedent

**Status: ✅ VERIFIED**

New Hampshire HB 672 created a new legal category of "off-grid electricity provider" — entities that generate, transmit, distribute, or sell electricity but are not connected to the existing grid. Effective **August 1, 2025** — five months before the DATA Act was introduced.

**Structural Comparison with DATA Act:**

| Feature | NH HB 672 (2025) | DATA Act CREU (2026) |
|---------|------------------|---------------------|
| Islanding requirement | Complete physical isolation | Complete physical isolation |
| Utility exemption | Not a public utility under state law | Exempt from FERC/FPA/PURPA/PUHCA |
| Loss of exemption trigger | Connection to regulated grid | Connection to broader grid |
| Scope | State-level | Federal |
| Timeline | Effective Aug 2025 | Introduced Jan 2026 |

The pattern — state pilot followed by federal expansion — is consistent with how legislative frameworks are typically tested before scaling nationally.

**Sources:** BillTrack50, NH Legislature, The Dartmouth

---

## 5. Capital Architecture: Who Is Funding the Buildout

### 5.1 ADQ / Energy Capital Partners — $25B Partnership

**Status: ✅ VERIFIED**

| Detail | Verified Finding |
|--------|-----------------|
| **Partners** | ADQ (Abu Dhabi sovereign wealth fund) + Energy Capital Partners (US private equity) |
| **Value** | USD $25 billion total capital investments |
| **Structure** | 50-50 partnership, $5B initial combined capital |
| **Target** | 25+ GW of new US power generation for data centers |
| **Focus** | Primarily US; new build natural gas-fired generation |
| **Announced** | March 2025 |

ADQ's Managing Director Mohamed Hassan Alsuwaidi stated: "The acceleration of AI and its societal adoption presents attractive opportunities to serve the power and infrastructure needs of data centers."

ECP's founder Doug Kimmelman noted: "Our focus in this partnership will therefore primarily be on new build natural gas fired power generation assets in scale."

**Source:** ADQ.ae official press release — confirmed verbatim from adq.ae/newsroom/

### 5.2 AVAIO Digital Partners — Undisclosed Investor

**Status: ⚠️ PARTIALLY VERIFIED**

AVAIO Digital launched in February 2021 with a $375M equity commitment (later $750M) from "a large investment manager with more than $25 billion of assets under management." The investor's identity has not been publicly disclosed in five years of operation. AVAIO has zero public SEC filings. The deliberate, sustained anonymity is itself noteworthy — typical institutional investors (pension funds, endowments) generally disclose infrastructure holdings.

**Source:** PRNewswire (February 2021), baseline research files

---

## 6. States Pushing Back: Moratoriums and Ratepayer Protections

### 6.1 The Scale of Pushback

By February 2026, **more than 300 state data center legislation bills** had been filed across **30+ states** in just six weeks, according to MultiState Policy Watch. This represents a dramatic shift from the incentive-focused policies of 2023-2025 toward regulatory oversight.

**Source:** MultiState: "State Data Center Legislation in 2026 Tackles Energy and Tax Issues" (February 20, 2026)

### 6.2 Data Center Moratorium Bills

| State | Bill | Proposed Duration | Key Provisions |
|-------|------|-------------------|----------------|
| **New York** | A 10141 / S9144 | 3 years | Halt all data center construction; DEC and PSC to adopt impact rules |
| **Oklahoma** | SB 1488 | Until Nov 2029 | Moratorium on >100MW facilities; PUC study of water, rates, property |
| **Virginia** | HB 1515 | Until July 2028 | Halt all new data center site applications including rezoning and special use permits |
| **Georgia** | (Senate bill) | 1 year (from July 2026) | Ban new data center development |
| **Vermont** | S.205 | Until July 2030 | Freeze construction; PUC investigation of environmental and economic impacts |
| **Maryland** | HB 120 | Until co-location legislation passes | Emergency moratorium; data centers must be built with co-located power |
| **South Dakota** | SB 232 | 1 year | Moratorium on hyperscale data centers |

**Sources:** MultiState (Feb 2026), Built In (Feb 2026), individual state legislature websites

### 6.3 Ratepayer Protection Measures

| State | Bill | Key Provision |
|-------|------|--------------|
| **Oklahoma** | HB 2992 | "Data Center Consumer Ratepayer Protection Act of 2026" — data centers pay proportional share of infrastructure costs |
| **Arizona** | HB 2756 | PUC rules ensuring grid connection costs not shifted to other customers |
| **Alabama** | SB 270 | PSC to condition permits on infrastructure cost coverage and statewide ratepayer benefit |
| **18+ states** | 30+ bills | Special rate classes for large load customers |

Rep. Brad Boles (R-OK), sponsor of HB 2992 and Chair of the Energy & Natural Resources Oversight Committee, stated: "With more than a dozen potential new data centers planning to locate in Oklahoma...we have to make sure everyday Oklahomans are not stuck paying the price."

**Sources:** Oklahoma House press release (January 8, 2026), MultiState (Feb 2026)

### 6.4 Tax Incentive Rollbacks

| State | Action | Detail |
|-------|--------|--------|
| **Virginia** | HB 961, HB 897 | Reduce tax incentives to replacement/repair equipment; require emission-free backup generators for incentive eligibility |
| **Georgia** | SB 476 | Eliminate all corporate tax credits (including data center) to fund income tax reduction |
| **Oklahoma** | HB 4424 | End tax incentives for data centers not operating by Jan 1, 2027 |

Virginia, which has the most data centers of any U.S. state (~643 facilities per Pew Research), is now under Democratic trifecta control and actively reconsidering its pro-data-center stance.

**Source:** MultiState (Feb 2026)

### 6.5 Local-Level Pushback

Local moratorium efforts have emerged in multiple states:
- **Hood County, Texas** — County commissioners debated a moratorium on data centers, but Texas HB 2559 may preempt local authority. State Sen. Paul Bettencourt (R) warned counties "don't have the right" to impose moratoriums.
- **Minnesota** (Eagan) and **Michigan** (19+ municipalities) have enacted local pauses.

Residents cite water use (up to 1 million gallons/day per facility), noise, air quality from backup generators, and minimal permanent job creation as concerns.

**Sources:** KERA News (Feb 24, 2026), Built In

---

## 7. States Accommodating Expansion

### 7.1 Arkansas

As detailed in Section 2, Arkansas has created a comprehensive legislative architecture:
- **Act 373** — PSC bypass via iterative resubmission and auto-approval defaults
- **Act 548** — Tailored data center tax incentives with $100M reduced threshold
- **Gov. Sanders** — Described AVAIO as "the largest economic investment in Arkansas' history" and actively promoted the state's "pro-business, pro-growth environment"

Arkansas's average retail electricity price is **9.59 cents/kWh** (EIA, 2024) — approximately 26% below the national average of 12.94 cents/kWh — providing substantial headroom under Act 373's rate cap.

### 7.2 New Hampshire

HB 672 created the off-grid provider exemption framework that the DATA Act later mirrors at the federal level. New Hampshire's electricity costs are high (20.61 cents/kWh), which may make islanded generation more economically attractive relative to grid power.

### 7.3 Texas

Texas operates ERCOT — a grid deliberately isolated from the national grid to avoid FERC regulation. The state actively preempts local moratorium efforts (HB 2559) while data center demand is projected at 40-50 GW of new demand within a decade.

Texas's average retail price is **9.79 cents/kWh** — similar to Arkansas. Its deregulated market structure makes it the "end state" model that other accommodation states appear to be moving toward.

---

## 8. Energy Data and Cost Comparisons

**Source: U.S. Energy Information Administration (EIA), 2024 data**

| State | Avg. Retail Price (¢/kWh) | National Rank | Net Summer Capacity (MW) | Primary Source | Policy Posture |
|-------|---------------------------|---------------|--------------------------|----------------|----------------|
| Arkansas | 9.59 | 43 (low) | 15,907 | Natural gas | Accommodate |
| Texas | 9.79 | 42 | 168,317 | Natural gas | Accommodate |
| Oklahoma | 9.09 | 48 (low) | 31,907 | Natural gas | Push back |
| Mississippi | 10.93 | 33 | 15,961 | Natural gas | Accommodate |
| Virginia | 10.62 | 38 | 29,147 | Natural gas | Push back |
| Georgia | 11.40 | 26 | 39,746 | Natural gas | Push back |
| New Hampshire | 20.61 | 7 (high) | 4,470 | Nuclear | Accommodate (off-grid) |
| New York | 19.66 | 10 (high) | 41,288 | Natural gas | Push back |
| **National Avg.** | **12.94** | — | — | — | — |

**Key observation:** Low-cost energy states are split — some accommodate (Arkansas, Texas, Mississippi) while others with similar costs push back (Oklahoma). High-cost states tend to push back (New York) or create off-grid exemptions (New Hampshire). Virginia — the epicenter of U.S. data centers — is pushing back despite moderate costs, suggesting that volume, not just price, drives opposition.

---

## 9. The Two-Camp Split: Structural Analysis

### 9.1 The Pattern

The state-level split is not purely partisan or regional. It reflects a structural tension between:
- **Economic development incentives** (jobs, tax revenue, "largest investment in state history")
- **Consumer/environmental concerns** (rate increases, water use, grid strain, minimal permanent jobs)

States in **Camp A (Accommodate)** tend to have:
- Strong executive-level support for data center development
- Utility companies actively lobbying for infrastructure investment
- Legislative architectures that streamline regulatory approval
- Lower electricity costs with headroom for increases

States in **Camp B (Push Back)** tend to have:
- Visible constituent opposition (rate hikes, water concerns, noise)
- Legislative awareness that data centers create relatively few permanent jobs for their footprint
- Prior experience with data center development revealing costs (Virginia's 643+ facilities)
- Political incentives to protect residential ratepayers

### 9.2 The Federal Overlay

The DATA Act and ALEC model legislation create a third path: **exemption from the entire framework**. If data centers can build physically islanded power systems exempt from both federal and state utility regulation, the moratorium vs. incentive debate becomes moot for those facilities.

This creates a potential trajectory:
1. State accommodates → passes incentives → data centers arrive
2. Ratepayer costs become visible → pushback emerges → moratoriums proposed
3. Federal/ALEC framework offers exit → islanded CREUs bypass both state incentives and state regulation

### 9.3 What This Means for Ratepayers

The fundamental question across all 50 states: **Who pays for the infrastructure that data centers require?**

- In **Arkansas**, Act 373's rider mechanism allows utilities to pass construction costs to ratepayers incrementally, with a cap at 10% below national average
- In **Oklahoma**, HB 2992 would require data centers to pay their own infrastructure costs
- In **Virginia**, moratorium legislation would halt new approvals until existing grid commitments are fulfilled
- Under the **DATA Act / ALEC model**, islanded facilities would theoretically not impact ratepayers at all — but would also not contribute to grid reliability

---

## 10. Federal Funding Withholding: Correlation Analysis

### 10.1 Dataset Overview

The correlation analysis examines **42 documented federal funding withholding events** (January 2025 – February 2026) tracked in `Correlations/Federal_Funding_Withholding_2025-2026.csv` against state data center policy postures classified across 27 states. The dataset includes blanket "All States" actions (22 events, 52%) and state-specific targeted actions (20 events, 48%).

**State Posture Classifications (27 states):**

| Posture | Count | States |
|---------|-------|--------|
| Accommodate | 4 | AR, MS, NH, TX |
| Push back | 19 | AL, AZ, CA, CT, DE, GA, ID, IL, MA, MD, NY, OH, OK, OR, SD, VA, VT, WA, WI |
| Neutral/Mixed | 4 | CO, MN, NJ, NM |

### 10.2 Statistical Results — All Targeting Events (v1.4, Recalculated N=42)

**Status: ✅ RECALCULATED (v1.4 — full results in `Correlations/Statistical_Analysis_Results.md`)**

| Posture | n (states) | Mean Events/State | Std Dev | Median |
|---------|------------|-------------------|---------|--------|
| Accommodate | 4 | 23.25 | 0.96 | 23.5 |
| Push back | 19 | 24.11 | 2.79 | 23.0 |
| Neutral/Mixed | 4 | 25.25 | 1.26 | 25.0 |

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| t-test (Push back vs Accommodate) | t = 1.071 | 0.3010 | **NO** |
| Mann-Whitney U (Push back vs Accommodate) | U = 36.5 | 0.9336 | **NO** |
| One-way ANOVA (all 3 groups) | F = 0.661 | 0.5253 | **NO** |
| Kruskal-Wallis (all 3 groups) | H = 2.564 | 0.2774 | **NO** |
| Chi-square (any targeting) | χ² = 0.909 | 0.6346 | **NO** |
| Point-biserial r (Push back vs Accommodate) | r = 0.129 | 0.5571 | **NO** |

**Effect Sizes:** Eta-squared = 0.052 (total events), 0.058 (energy events) — both small effects, meaning data center posture explains less than 6% of the variance in federal targeting.

**Conclusion:** No statistically significant relationship between data center policy posture and federal funding targeting. All six statistical tests are non-significant (all p > 0.27). The small differences in mean event counts across groups are within normal variation and not distinguishable from chance.

### 10.3 Energy/Climate-Specific Targeting (v1.4 Correction)

**v1.2 Finding (CORRECTED):** The v1.2 analysis (N=30) reported that 100% of Neutral/Mixed states were hit by energy-specific withholding vs. 50% of Push back and 25% of Accommodate states. **This finding no longer holds with the expanded N=42 dataset.**

With N=42, **100% of all posture groups** are affected by energy-related federal actions:

| Posture | States Hit | Total | % Targeted | Mean Energy Events |
|---------|------------|-------|------------|-------------------|
| Accommodate | 4 | 4 | **100%** | 9.75 |
| Push back | 19 | 19 | **100%** | 10.05 |
| Neutral/Mixed | 4 | 4 | **100%** | 10.50 |

| Test | Statistic | p-value | Significant? |
|------|-----------|---------|--------------|
| ANOVA (energy events by posture) | F = 0.741 | 0.4873 | **NO** |
| Kruskal-Wallis (energy events) | H = 1.689 | 0.4299 | **NO** |

**Why the v1.2 finding was misleading:** The original N=30 dataset counted only events that specifically named a state. Many blanket actions (e.g., DOE Loan Programs Office freeze, DOT formula funding delay, IRA tax credit phase-out) were added in v1.3, and these affect all states equally. When the full event set is analyzed, energy-related federal actions impact every classified state regardless of posture.

### 10.4 Temporal Lag Analysis (v1.4 — Recalculated with Methodological Correction)

**Status: ✅ RECALCULATED AND CORRECTED (v1.4)**

The temporal analysis measures the lag between state data center legislation (trigger dates) and federal funding actions across 474 state–federal-action pairs. A negative lag means the federal government acted before the state legislated; a positive lag means federal action came after.

**Raw Results (N=42):**

| Posture | n (pairs) | Median Lag (days) | % Proactive |
|---------|-----------|-------------------|-------------|
| Accommodate | 47 | −18 | 53.2% |
| Push back | 326 | −74 | 53.7% |
| Neutral/Mixed | 101 | +92 | 12.9% |

**⚠️ Critical Methodological Finding:** The apparent difference in lag times between posture groups is **driven by when states introduced their data center legislation**, not by differential federal behavior. This was identified in the v1.4 analysis and confirmed through three independent checks:

1. **Trigger date confound:** All 4 Neutral/Mixed states (CO, MN, NJ, NM) have early legislation dates (Jan–Jun 2025). Many Push back states have late dates (Jan–Feb 2026). Since most federal actions occurred throughout 2025, Neutral/Mixed states mechanically show positive lags (federal actions came after their early legislation) while late-legislating Push back states show negative lags (federal actions came before their 2026 legislation).

2. **Controlled comparison:** When comparing only states with the same trigger date (2025-01-01), Push back and Neutral/Mixed states show **identical** median lags of 113 days (Mann-Whitney U, p = 0.768). The posture difference vanishes when the trigger date is held constant.

3. **DoWhy causal model with correction:** When trigger_date is added as a confounder alongside the original confounders (federal_action, action_type), the estimated causal effect drops from +148 days (p < 0.0001) to **0.00 days (p = 1.000)**.

| DoWhy Model | Causal Effect | p-value | Significant? |
|-------------|--------------|---------|--------------|
| Original (no trigger date control) | +148.02 days | < 0.0001 | YES |
| **Corrected (with trigger date control)** | **0.00 days** | **1.000** | **NO** |

**Conclusion:** The v1.2 temporal lag findings — including the "reactive retaliation" interpretation for Neutral/Mixed states and the +151-day causal effect — were confounded by trigger date differences between posture groups. When properly controlled, there is **no evidence** that federal funding actions respond differently to states based on their data center policy posture.

### 10.5 Five-Stage Federal Action Timeline

Analysis of the 42 documented federal funding events reveals a five-stage chronological pattern. **Note:** This is presented as a descriptive timeline of how federal actions unfolded, not as evidence of targeting based on data center posture.

| Stage | Timing | Action | Who's Hit | Evidence |
|-------|--------|--------|-----------|----------|
| 1. Blanket Freeze | Jan 2025 | EO-driven IIJA/IRA/OMB pauses | All 50 states | EO 'Unleashing American Energy' |
| 2. Selective Enforcement | Feb–Apr 2025 | Sanctuary conditions, FEMA continued freeze | Blue states + sanctuary cities (CA, IL, NY, OR, WA, CO, MA) | Byrne JAG conditions, DHS sanctuary list |
| 3. Compliance Ultimatums | Jun–Aug 2025 | PREP gender identity, education DEI | 40+ states warned; CA terminated first | HHS.gov press releases |
| 4. Targeted Terminations | Aug–Oct 2025 | NIH grants, DOE clean energy, MSI grants | CA (NIH), 16 blue states (DOE), 167+ CA institutions (MSI) | DOE.gov, Ed.gov, EdSource |
| 5. Selective Release | Feb 2026 | FEMA disaster aid released to some, not others | CA, IL, MN, CO, VI excluded while NY, NC get aid | The Hill, CNN |

**Cross-party findings:** Politically aligned states suffered significant withholding across all stages. Texas ($700M education), Arkansas ($64M education + tornado disaster declaration denied), Oklahoma ($70M education + $6.3B in Medicaid hospital cuts + hazard mitigation denied), New Hampshire ($27M education + $5M DOE grant terminated) — all were hit. FEMA denied disaster declarations for AR (Accommodate state), WV, and WA. DOE hydrogen hub terminations ($7B) affected TX and LA alongside blue states. The selective release at Stage 5 is the primary point where political alignment appears to influence outcomes — but this correlates with immigration/sanctuary policy, not data center posture.

### 10.6 What the Data Actually Shows

Based on the complete v1.4 analysis, the federal funding withholding data supports the following conclusions:

**Supported by data:**
1. Federal funding actions during this period affected all states broadly, regardless of data center policy posture
2. 52% of documented events are blanket "All States" actions — this is the dominant pattern
3. The 5 most-targeted states (CA=30, IL=29, OR=28, CO/MA/WA=27, NY=26 events) are primarily targeted for immigration/sanctuary and DEI policy positions, not data center posture
4. Both politically aligned and opposing states experience comparable rates of federal withholding
5. There is no statistically significant relationship between data center posture and federal targeting (all tests p > 0.27)

**Not supported by data:**
1. ~~"Pressure on the undecided"~~ — Not significant; the small differences are within normal variation
2. ~~"100% energy targeting of Neutral/Mixed vs 25-50% of others"~~ — Artifact of smaller dataset; all groups are 100% hit
3. ~~"Reactive retaliation" temporal pattern~~ — Driven by legislation timing, not federal behavior
4. ~~"+151-day causal effect"~~ — Confounded by trigger dates; corrected estimate is zero

**Open questions:**
1. The correlation between immigration/sanctuary policy and federal targeting warrants further study as a separate analysis
2. Small group sizes (n=4 for Accommodate and Neutral/Mixed) limit statistical power — effects too small to detect cannot be ruled out
3. Whether the Stage 5 selective release pattern is related to political alignment vs. administrative factors remains unclear

### 10.7 Limitations

1. **Small group sizes** — Only 4 Accommodate and 4 Neutral/Mixed states limits statistical power; approximately 20+ states per group would be needed for reliable medium-effect detection at α=0.05
2. **Confounding variables** — Political alignment correlates with both data center posture AND immigration/DEI policy; isolating the effect of posture alone is difficult
3. **Blanket dominance** — 52% of events hit all states, creating high and uniform event counts that dilute any targeted signal
4. **Trigger date imprecision** — Many state legislation dates are approximate (e.g., "Introduced 2025" parsed as Jan 1), which limits the precision of temporal lag calculations
5. **Selection bias in states classified** — Only 27 of 50 states are classified by posture; the remaining 23 states may have different patterns
6. **Effect sizes are small** — Eta-squared values of 0.05–0.06 indicate that data center posture explains very little of the observed variation in federal targeting

---

## 11. State-by-State Federal Impact Assessment

### 11.1 Arkansas — Accommodate State, HIGH Federal Dependency

| Category | Federal Action | State Impact |
|----------|---------------|-------------|
| Education | K-12 funding withheld ($6.9B national) | $64M withheld from AR schools; Little Rock SD paused programs |
| Medicaid | Budget reconciliation ($900B–$1T cut) | 27–34% projected enrollment decline; 18,000 lost coverage in 2018 pilot |
| IIJA/IRA | Blanket $125B freeze (Jan 2025) | Infrastructure projects paused; BEAD broadband delayed |
| FEMA BRIC | $4.5B hazard mitigation canceled | AR mitigation projects in pipeline halted |
| **FEMA Tornado (v1.3)** | **Disaster declaration denied Apr 2025** | **$8.8M damage estimate; Gov. Sanders appealed; 63 of 75 counties affected; 3 deaths; no federal funds obligated** |
| **Data Center Nexus** | AVAIO Leo $6B campus needs grid upgrades | Act 373 enables PSC bypass — but if IIJA grid funding stays frozen, 1GW campus grid upgrades may be delayed |

### 11.2 Texas — Accommodate State, CRITICAL Federal Dependency (ERCOT Isolation)

| Category | Federal Action | State Impact |
|----------|---------------|-------------|
| Education | K-12 funding withheld ($6.9B national) | $700M withheld — TX AFT + 13 agencies sued; released after 25 days |
| FEMA | Disaster Relief Fund $11B delayed | Gulf Coast flooding recovery delayed; hazard mitigation halted |
| IIJA/IRA | Blanket $125B freeze + NEVI $5B frozen | TX DOT paused projects; EV charging infrastructure delayed |
| CHIPS | CHIPS Act renegotiations ($50B total) | Samsung Austin fab and TI Dallas timelines extended |
| **DOE Hydrogen Hub (v1.3)** | **HyVelocity Hub terminated ($7B total)** | **TX/LA Gulf Coast hydrogen hub canceled; bipartisan alarm; clean hydrogen competitiveness at risk** |
| **Data Center Nexus** | 40–50 GW projected demand growth | ERCOT grid isolation means TX cannot rely on interstate backup if federal grid funding stays frozen |

### 11.3 Oklahoma — Push Back State, HIGH Federal Vulnerability (Medicaid)

| Category | Federal Action | State Impact |
|----------|---------------|-------------|
| Education | K-12 funding withheld ($6.9B national) | $70M+ withheld from OK schools |
| Medicaid | Budget reconciliation ($900B–$1T cut) | $6.3–6.7B in hospital cuts over 10 years; 171,000 projected to lose coverage; 53% of rural hospitals at risk |
| FEMA BRIC | $4.5B hazard mitigation canceled | Stillwater stormwater drainage and water infrastructure projects halted |
| **FEMA Hazard Mitigation (v1.3)** | **Hazard mitigation grants denied (Jun 2025)** | **OK wildfire recovery hampered; tornado safe rooms and warning sirens unfunded despite approved major disaster declaration** |
| **Data Center Nexus** | Federal grid/clean energy funding frozen | SB 1488 moratorium + HB 2992 ratepayer protection — push back posture may be reinforced by federal uncertainty |

### 11.4 Virginia — Push Back State, HIGH Federal Dependency (Data Center Capital)

| Category | Federal Action | State Impact |
|----------|---------------|-------------|
| Education | K-12 funding withheld ($6.9B national) | $108–113M withheld; ~1,100 teaching positions affected |
| DOE Clean Energy | DOE terminated 223 projects ($7.56B) | VA included in 16-state cancellation; data center decarbonization projects directly affected |
| IIJA/IRA | Blanket $125B freeze | Grid modernization delayed at critical time for data center demand |
| **Data Center Nexus** | ~643 data centers (most in US) | DOE clean energy cuts kill decarbonization pathway for existing facilities; HB 1515 moratorium reflects pushback |

### 11.5 New Hampshire — Accommodate (Off-Grid) State, LOW Federal Dependency

| Category | Federal Action | State Impact |
|----------|---------------|-------------|
| Education | K-12 funding withheld ($6.9B national) | $27M withheld from NH schools |
| DOE Clean Energy | DOE terminated 223 projects ($7.56B) | Brayton Energy lost ~$5M; $43M Solar for All grant at risk |
| IIJA/IRA | Blanket $125B freeze | NH infrastructure projects paused |
| **Data Center Nexus** | HB 672 off-grid provider exemption | Off-grid model is structurally insulated from federal grid funding chaos — most resilient by design |

### 11.6 Cross-State Vulnerability Summary

| State | Data Center Posture | Federal Grid Dependency | Vulnerability |
|-------|--------------------|---------------------------------|---------------|
| Arkansas | Accommodate (PSC bypass) | HIGH — needs grid upgrades for AVAIO 1GW campus | Federal freeze threatens flagship project infrastructure |
| Texas | Accommodate (preempt moratoriums) | CRITICAL — ERCOT isolation, no interstate backup | 40–50 GW demand growth requires massive internal investment |
| Oklahoma | Push Back (moratorium + ratepayer protection) | MODERATE — moratorium buys time | Medicaid crisis ($6.3B hospital cuts) may dominate state bandwidth |
| Virginia | Push Back (moratorium + tax rollback) | HIGH — 643 data centers need grid + decarbonization | DOE clean energy cuts kill decarbonization pathway |
| New Hampshire | Accommodate (off-grid) | LOW — HB 672 off-grid model is self-sufficient | Most resilient to federal funding chaos by design |

---

## 12. Open Questions and Unresolved Threads

1. **Who is AVAIO's $25B anchor investor?** Still undisclosed after 5+ years. The ADQ/ECP partnership is a verified $25B vehicle — but no confirmed link to AVAIO.

2. **Does the DATA Act's CREU exemption apply to AVAIO's 1GW target?** If AVAIO builds islanded generation at the Little Rock campus, it could potentially qualify as a CREU.

3. **How will the DATA Act interact with state-level moratoriums?** Federal preemption questions are unresolved — can a state moratorium block a facility that qualifies for federal CREU exemption?

4. **Is the coordinated timing of ratepayer protection bills (Jan-Feb 2026, multiple states) organic or coordinated?** MultiState reports 300+ bills in 30+ states in 6 weeks. This may reflect independent responses to the same problem, ALEC/industry model legislation influence, or both.

5. **Will local-level pushback (Hood County, TX; Eagan, MN; Michigan municipalities) force state-level responses?** Texas is already preempting local moratoriums via HB 2559.

6. **What happens to accommodation states if data center demand doesn't materialize at projected levels?** The "AI bubble" scenario raised by Travis Fisher (Cato) — if facilities are not needed, private investors bear the loss under the CREU model, but ratepayers bear the loss under the traditional utility model (Act 373).

7. **What drives the variation in targeted (non-blanket) events?** The 5 most-targeted states (CA, IL, OR, CO, MA/WA) are primarily targeted for immigration/sanctuary and DEI policy positions. A separate analysis of whether sanctuary/immigration policy positions predict federal targeting — independent of data center posture — would clarify the dominant driver.

8. **Can future data distinguish posture effects from political alignment?** With larger sample sizes (more states classified, more events documented), it may become possible to detect small effects that the current dataset lacks power to identify. The current effect sizes (eta-squared ~0.05) are below conventional detection thresholds.

---

## 13. Sources

### Federal Legislation
- Cotton.senate.gov: DATA Act press release and bill text (January 8, 2026)
- ALEC: Model CREU legislation — alec.org/model-policy/act-to-allow-for-consumer-regulated-electric-utilities/

### Arkansas
- Arkansas Legislature: Act 373 (SB 307) and Act 548 (HB 1444) — arkleg.state.ar.us
- BillTrack50: SB 307 — billtrack50.com/billdetail/1845892
- BillTrack50: HB 1444 — billtrack50.com/billdetail/1826317
- Kutak Rock: "Expansion of the Sales and Use Tax Data Center Exemption" (April 2025) — kutakrock.com
- Talk Business & Politics: "Power generation bill fails in senate by one vote" (March 2025)
- AVAIO Digital / PRNewswire: Little Rock campus announcement (January 2026)

### New Hampshire
- BillTrack50 / NH Legislature: HB 672

### Oklahoma
- Oklahoma House: HB 2992 press release (January 8, 2026) — okhouse.gov
- Oklahoma Legislature: SB 1488 (moratorium bill)

### Virginia
- Virginia LIS: HB 1515, HB 961, HB 897
- VPM: "Virginia lawmakers propose a bevy of data center reform bills" (January 2026)

### Multi-State Analysis
- MultiState Policy Watch: "State Data Center Legislation in 2026 Tackles Energy and Tax Issues" (February 20, 2026)
- Built In: "States Push Data Center Moratoriums as AI Growth Surges" (February 2026)
- KERA News: "Hood County to consider another data center moratorium" (February 24, 2026)

### Energy Data
- U.S. Energy Information Administration: State electricity profiles — eia.gov/electricity/state/

### Capital
- ADQ.ae: Official partnership announcement with Energy Capital Partners (March 2025)
- Reason: "Data centers use lots of electricity. This bill would let them go off the grid" (January 9, 2026)
- NWA Democrat-Gazette: Alex Thomas reporting on DATA Act (January 7, 2026)
- Pew Research Center: Data center energy use report (October 2025)

### Industry / Policy
- Data Center Dynamics (various articles)
- North American Electric Reliability Corporation (NERC): Long-Term Reliability Assessment (2025)

### Correlation Analysis
- Statistical methodology: Python (pandas 3.0, scipy 1.15, DoWhy 0.14) — `Correlations/Statistical_Analysis_Results.md`
- Temporal lag engine: `Correlations/temporal_engine.py` — `Correlations/temporal_summary.md`
- Causal inference: DoWhy framework — `Correlations/Independent_Verification.py` — `Correlations/causal_summary.md`
- Federal funding data: `Correlations/Federal_Funding_Withholding_2025-2026.csv` (42 events, 2025–2026)
- State posture data: `02_CSVs_and_Datasets/Copilot_Agent/state_posture_lookup.csv` (27 states) + `ANALYSIS/state_posture_lookup.csv` (6 target states)
- Federal impact by state: `ANALYSIS/state_federal_impact_summary.csv`

---

*This report was compiled using multi-source verification. All claims are cross-referenced against primary sources where available. Where verification is partial, the claim is explicitly marked. This analysis does not make causal claims beyond what the evidence supports — structural observations are identified as such. Statistical analysis (Sections 10–11) uses standard frequentist methods with documented limitations. v1.4 corrects methodological issues in v1.2 temporal lag and causal analyses identified through trigger-date confound analysis.*

*For the geopolitical context behind these state-level dynamics, see [The Regulated Friction Project](https://github.com/Leerrooy95/The_Regulated_Friction_Project).*

*v1.4 — March 2026*

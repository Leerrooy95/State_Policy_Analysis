# State Policy Analysis

**A data-driven examination of how U.S. states are responding to the data center and energy infrastructure boom — from regulatory accommodation to outright moratoriums.**

---

## Overview

This repository documents the divergent state-level policy responses to the rapid expansion of data center infrastructure across the United States. The analysis focuses on the legislative, regulatory, and capital architecture that enables — or restricts — large-scale data center and energy projects, with a particular emphasis on Arkansas as a case study.

The core finding: **states are splitting into two camps** — those that actively reshape laws to accommodate data center and energy expansion (e.g., Arkansas, New Hampshire), and those that are pushing back through moratoriums, ratepayer protections, and tax incentive rollbacks (e.g., Virginia, Oklahoma, New York, Georgia, Vermont, Maryland).

## What's in This Repository

| Folder | Contents |
|--------|----------|
| [`01_The_Baseline/`](01_The_Baseline/) | Original research files documenting Arkansas's legislative architecture (Act 373, Act 548), the DATA Act of 2026, NH HB 672, AVAIO Digital, and capital flows |
| [`02_CSVs_and_Datasets/`](02_CSVs_and_Datasets/) | Structured CSV data organized by state — legislation, energy statistics, capital investments, and cross-state comparisons |
| [`Report.md`](Report.md) | Full detailed findings report with verification status, multi-source citations, and analysis |

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

## Methodology

- Claims are verified against primary legislative text, official press releases, and government data where possible
- Secondary sources (news coverage, legal analysis) are used for context and confirmation
- Where verification is partial or unavailable, the claim is explicitly marked
- No single partisan source is treated as authoritative; findings require multi-source confirmation
- Analysis distinguishes between **verified facts** (legislation text, official data), **structural observations** (pattern analysis), and **unconfirmed hypotheses**

---

*Repository maintained by Austin ([Leerrooy95](https://github.com/Leerrooy95))*
*Last updated: March 2026*

# Archive — Legacy Files

**Archived:** March 2026 (v1.3 / v1.4 upgrades)

This folder contains analysis outputs, intermediate files, and redundant CSVs from earlier dataset versions. These files were archived as the dataset expanded from N=30 to N=42 events and the analysis was recalculated.

## Why Archived

- **Statistical analysis outputs** (`Correlations_v1.2/`) were generated from the original 30-event dataset and are now underpowered relative to the expanded 42-event dataset
- **Copilot Agent intermediate files** (`Copilot_Agent_v1.2/`) contain working analysis that has been superseded by updated analysis in the main workspace
- **Gemini-Code outputs** (`Gemini-Code_v1.2/`) used a 13-state posture subset and covered only 32 of 41 master federal actions; superseded by the authoritative Copilot temporal engine (39/41 actions, 26 states, 630 pairs)

## Contents

### `Correlations_v1.2/`
| File | Reason |
|------|--------|
| `Statistical_Analysis_Results.md` | ANOVA/chi-square results based on N=30; need recalculation with N=42 |
| `temporal_analysis_final.csv` | 346 state-federal pairs from N=30; incomplete coverage of new events |
| `temporal_summary.md` | Median lag and proactive/reactive analysis from N=30 dataset |
| `Independent_Verification.md` | DoWhy causal model results from N=30; require re-estimation |

### `Copilot_Agent_v1.2/`
| File | Reason |
|------|--------|
| `profiled_state_federal_impact_summary.csv` | Superseded by `ANALYSIS/state_federal_impact_summary.csv` |
| `federal_withholding_five_stage_pattern.csv` | Five-stage pattern based on N=30; needs expansion |
| `state_posture_lookup.csv` | Intermediate copy without source/confidence columns |
| `Federal_Withholding_State_Correlation_Analysis.md` | Correlation analysis based on N=30 dataset |

### `Gemini-Code_v1.2/`
| File | Reason |
|------|--------|
| `temporal_analysis.py` | Used 13-state `expanded_state_posture_lookup.csv`; output path bug (`Gemini/` vs `Gemini-Code/`) |
| `temporal_analysis_final.csv` | 325 pairs, 32 of 41 actions — missing 9 federal actions covered by Copilot engine |
| `temporal_summary.md` | Summary from incomplete 13-state run |
| `causal_analysis.py` | DoWhy causal model from incomplete dataset |
| `causal_summary.md` | Causal results from incomplete dataset |
| `final_report.md` | Report from incomplete dataset |

## Reuse

These files retain historical value and can be used to compare earlier findings against v1.4 results.

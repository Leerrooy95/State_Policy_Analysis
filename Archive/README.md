# Archive — v1.2 Legacy Files

**Archived:** March 2026 (v1.3 upgrade)

This folder contains analysis outputs, intermediate files, and redundant CSVs from the v1.2 dataset (N=30 federal funding withholding events). These files were archived during the v1.3 intelligence upgrade, which expanded the dataset to N=42 events.

## Why Archived

- **Statistical analysis outputs** (`Correlations_v1.2/`) were generated from the original 30-event dataset and are now underpowered relative to the expanded 42-event dataset
- **Copilot Agent intermediate files** (`Copilot_Agent_v1.2/`) contain working analysis that has been superseded by updated analysis in the main workspace

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

## Reuse

These files retain historical value and can be used to compare v1.2 findings against v1.3 results once the expanded dataset is fully analyzed.

## 02_CSVs_and_Datasets

Structured data files organized by state. All data is sourced from official government records, EIA statistics, legislative text, and verified press releases.

### Folder Structure

```
02_CSVs_and_Datasets/
├── Arkansas/
│   ├── arkansas_legislation.csv          — Key laws (Act 373, Act 548, DATA Act)
│   ├── arkansas_infrastructure_investments.csv  — Major projects (AVAIO, Jefferson PS, L3Harris, R2S, Pine Bluff)
│   └── arkansas_energy_profile.csv       — EIA energy data and rate headroom
├── Oklahoma/
│   ├── oklahoma_data_center_legislation.csv  — HB 2992 (ratepayer protection), SB 1488 (moratorium)
│   └── oklahoma_energy_profile.csv       — EIA energy data
├── Virginia/
│   ├── virginia_data_center_legislation.csv  — HB 1515 (moratorium), HB 961, HB 897
│   └── virginia_energy_and_data_center_profile.csv  — EIA data + data center counts
├── New_Hampshire/
│   ├── new_hampshire_hb672.csv           — HB 672 off-grid provider details
│   └── new_hampshire_energy_profile.csv  — EIA energy data
├── Texas/
│   └── texas_energy_and_grid_profile.csv — ERCOT data, HB 2559, projections
└── Multi_State/
    ├── state_energy_and_policy_comparison.csv  — Side-by-side comparison of 13 states
    ├── data_center_legislation_tracker.csv     — All tracked legislation across states
    └── capital_flows_data_center_energy.csv    — Major capital investments
```

### Data Sources

- **EIA**: U.S. Energy Information Administration 2024 state electricity profiles (eia.gov/electricity/state/)
- **Legislation**: BillTrack50, LegiScan, state legislature websites, Kutak Rock legal analysis
- **Policy Analysis**: MultiState Policy Watch (February 2026)
- **Press**: Official press releases (AVAIO/PRNewswire, ADQ.ae, Oklahoma House, Cotton.senate.gov)

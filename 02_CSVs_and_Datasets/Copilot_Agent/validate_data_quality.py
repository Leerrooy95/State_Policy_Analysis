#!/usr/bin/env python3
"""
Data Quality Validation Script for State Policy Analysis Repository.

Validates:
1. CSV parsability — all rows properly formatted, no malformed quotes or commas
2. Amount standardization — amount_usd column contains valid numbers or empty (NULL)
3. State name consistency — state names match across datasets and folders
4. Date parsing — all dates in ISO 8601 format (YYYY-MM-DD)
5. Category labels — posture labels consistent with lookup table
"""

import csv
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}")


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def ok(msg):
    print(f"  OK:    {msg}")


# ── 1. CSV Parsability ──────────────────────────────────────────────────────

def validate_csv_parsability():
    print("\n=== 1. CSV PARSABILITY ===")
    csv_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f.endswith('.csv'):
                csv_files.append(os.path.join(root, f))

    for fp in sorted(csv_files):
        rel = os.path.relpath(fp, REPO_ROOT)
        try:
            with open(fp, 'r', encoding='utf-8') as fh:
                reader = csv.reader(fh)
                rows = list(reader)
                header = rows[0] if rows else []
                issues = []
                for i, row in enumerate(rows[1:], 2):
                    if len(row) != len(header):
                        issues.append(
                            f"Row {i}: expected {len(header)} columns, got {len(row)}"
                        )
                if issues:
                    for iss in issues:
                        error(f"{rel}: {iss}")
                else:
                    ok(f"{rel} ({len(header)} cols, {len(rows)-1} rows)")
        except Exception as e:
            error(f"{rel}: parse error — {e}")


# ── 2. Amount Standardization ────────────────────────────────────────────────

def validate_amounts():
    print("\n=== 2. AMOUNT STANDARDIZATION ===")
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "Federal_Funding_Withholding_2025-2026.csv"
    )
    with open(fp) as f:
        reader = csv.DictReader(f)
        if 'amount_usd' not in reader.fieldnames:
            error("Missing 'amount_usd' column in withholding CSV")
            return
        ok("'amount_usd' column present")

        null_count = 0
        valid_count = 0
        for i, row in enumerate(reader, 1):
            val = row['amount_usd'].strip()
            if val == '':
                null_count += 1
            elif val.isdigit():
                valid_count += 1
            else:
                error(f"Row {i}: invalid amount_usd value: {val!r}")

        ok(f"{valid_count} numeric values, {null_count} NULL values")


# ── 3. State Name Consistency ────────────────────────────────────────────────

def validate_state_names():
    print("\n=== 3. STATE NAME CONSISTENCY ===")

    # Collect state names from each dataset
    datasets = {}

    # state_energy_and_policy_comparison.csv
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "state_energy_and_policy_comparison.csv"
    )
    with open(fp) as f:
        datasets['energy_comparison'] = [r['state'] for r in csv.DictReader(f)]

    # state_federal_impact_summary.csv (ANALYSIS folder at repo root)
    # REPO_ROOT = 02_CSVs_and_Datasets/; dirname gives the actual repo root
    analysis_root = os.path.join(os.path.dirname(REPO_ROOT), "ANALYSIS")
    fp = os.path.join(analysis_root, "state_federal_impact_summary.csv")
    with open(fp) as f:
        datasets['impact_summary'] = [r['state'] for r in csv.DictReader(f)]

    # state_posture_lookup.csv (ANALYSIS folder)
    fp = os.path.join(analysis_root, "state_posture_lookup.csv")
    with open(fp) as f:
        datasets['posture_lookup'] = [r['state'] for r in csv.DictReader(f)]

    # State folders
    folder_states = []
    for d in sorted(os.listdir(REPO_ROOT)):
        full = os.path.join(REPO_ROOT, d)
        if os.path.isdir(full) and d not in ('Copilot_Agent', 'Multi_State'):
            folder_states.append(d.replace('_', ' '))
    datasets['folders'] = folder_states

    # Check: impact_summary states should be in energy_comparison
    impact_set = set(datasets['impact_summary'])
    energy_set = set(datasets['energy_comparison'])
    missing = impact_set - energy_set
    if missing:
        error(f"States in impact_summary but not energy_comparison: {missing}")
    else:
        ok("Impact summary states are subset of energy comparison states")

    # Check: folder states should be in energy_comparison
    folder_set = set(datasets['folders'])
    missing = folder_set - energy_set
    if missing:
        error(f"Folder states not in energy_comparison: {missing}")
    else:
        ok("Folder states match energy comparison states")

    # Check: no underscores in state names
    for name, states in datasets.items():
        for s in states:
            if '_' in s:
                error(f"Underscore in state name '{s}' in {name}")
    ok("No underscores in state names across CSV datasets")

    # Check state_code column in withholding CSV
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "Federal_Funding_Withholding_2025-2026.csv"
    )
    with open(fp) as f:
        reader = csv.DictReader(f)
        if 'state_code' not in reader.fieldnames:
            error("Missing 'state_code' column in withholding CSV")
            return
        ok("'state_code' column present in withholding CSV")

        valid_codes = {
            'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID',
            'IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS',
            'MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK',
            'OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV',
            'WI','WY','DC','VI','PR','GU','AS','MP',
        }
        for i, row in enumerate(reader, 1):
            codes = row['state_code'].strip()
            if codes:
                for code in codes.split(','):
                    if code not in valid_codes:
                        error(f"Row {i}: invalid state code '{code}'")
        ok("All state_code values are valid 2-letter abbreviations")


# ── 4. Date Parsing ──────────────────────────────────────────────────────────

def validate_dates():
    print("\n=== 4. DATE PARSING ===")
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "Federal_Funding_Withholding_2025-2026.csv"
    )
    with open(fp) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            date_str = row['date'].strip()
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                error(f"Row {i}: invalid ISO date: {date_str!r}")
    ok("All dates in ISO 8601 format (YYYY-MM-DD)")


# ── 5. Category Labels (Posture Consistency) ─────────────────────────────────

def validate_posture_labels():
    print("\n=== 5. POSTURE LABEL CONSISTENCY ===")

    # Load canonical postures from lookup table (ANALYSIS folder at repo root)
    # REPO_ROOT = 02_CSVs_and_Datasets/; dirname gives the actual repo root
    analysis_root = os.path.join(os.path.dirname(REPO_ROOT), "ANALYSIS")
    fp = os.path.join(analysis_root, "state_posture_lookup.csv")
    canonical = {}
    with open(fp) as f:
        for row in csv.DictReader(f):
            canonical[row['state']] = row['posture']

    valid_postures = set(canonical.values())
    ok(f"Canonical posture values: {sorted(valid_postures)}")

    # Verify energy comparison postures resolve to canonical base
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "state_energy_and_policy_comparison.csv"
    )
    with open(fp) as f:
        for row in csv.DictReader(f):
            raw = row['policy_posture']
            base = raw.split('(')[0].strip()
            if base not in valid_postures:
                error(
                    f"'{raw}' in energy_comparison for {row['state']} "
                    f"does not match canonical postures"
                )
    ok("Energy comparison postures consistent with lookup table")

    # Verify impact summary postures resolve to canonical base (ANALYSIS folder)
    fp = os.path.join(analysis_root, "state_federal_impact_summary.csv")
    with open(fp) as f:
        for row in csv.DictReader(f):
            raw = row['data_center_posture']
            base = raw.split('(')[0].strip()
            if base not in valid_postures:
                error(
                    f"'{raw}' in impact_summary for {row['state']} "
                    f"does not match canonical postures"
                )
    ok("Impact summary postures consistent with lookup table")

    # Check targeted column
    fp = os.path.join(
        REPO_ROOT, "Multi_State", "Federal_Funding_Withholding_2025-2026.csv"
    )
    with open(fp) as f:
        reader = csv.DictReader(f)
        if 'targeted' not in reader.fieldnames:
            error("Missing 'targeted' column in withholding CSV")
            return
        for i, row in enumerate(reader, 1):
            val = row['targeted'].strip()
            if val not in ('0', '1'):
                error(f"Row {i}: targeted value must be 0 or 1, got {val!r}")
    ok("'targeted' column contains only binary 0/1 values")


# ── Run All ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    validate_csv_parsability()
    validate_amounts()
    validate_state_names()
    validate_dates()
    validate_posture_labels()

    print("\n" + "=" * 60)
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        sys.exit(1)
    else:
        print(f"PASSED: 0 errors, {len(WARNINGS)} warning(s)")
        sys.exit(0)

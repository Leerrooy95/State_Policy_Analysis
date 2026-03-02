
import pandas as pd
import numpy as np
from dowhy import CausalModel
import dowhy.datasets
import os

# Stop printing verbose causal model status messages
import logging
logging.getLogger("dowhy.causal_model").setLevel(logging.CRITICAL)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GEMINI_DIR = SCRIPT_DIR

# STEP 1: DATA PREP
data = pd.read_csv(os.path.join(GEMINI_DIR, 'temporal_analysis_final.csv'))

# Create a binary treatment variable
data['is_neutral'] = np.where(data['posture'] == 'Neutral/Mixed', 1, 0)

# STEP 2: CAUSAL MODELING
model = CausalModel(
    data=data,
    treatment='is_neutral',
    outcome='lag_days',
    common_causes=['federal_action', 'action_type'] # Confounders
)

# Identify the causal effect
identified_estimand = model.identify_effect()

# Estimate the causal effect using linear regression
estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.linear_regression"
)

# STEP 3: REFUTATION
# Refutation test 1: Add a random common cause
refute_random = model.refute_estimate(
    identified_estimand,
    estimate,
    method_name="random_common_cause"
)

# Refutation test 2: Placebo treatment refuter
refute_placebo = model.refute_estimate(
    identified_estimand,
    estimate,
    method_name="placebo_treatment_refuter",
    placebo_type="permute"
)


# STEP 4: OUTPUT
causal_effect = estimate.value
p_value = estimate.test_stat_significance()['p_value'][0]

# Correctly interpret the p-value
if p_value < 0.05:
    significance_text = f"The result is statistically significant (p-value: {p_value:.4f}), suggesting the effect is not due to random chance."
    conclusion_text = "The analysis indicates a statistically significant causal link between a 'Neutral/Mixed' posture and lag times."
else:
    significance_text = f"The result is NOT statistically significant (p-value: {p_value:.4f}). This p-value is greater than the standard 0.05 threshold, meaning we cannot conclude the effect is different from zero. There is a high probability that the observed effect is due to random chance."
    conclusion_text = "The analysis did not find a statistically significant causal effect. While an effect size was estimated, its high p-value suggests it is not distinguishable from random noise. Therefore, we cannot claim a causal link based on this analysis."

report = f"""
# Causal Verification Summary (Corrected)

## Estimated Causal Effect

The causal model was run on the complete dataset to estimate the effect of a state's "Neutral/Mixed" posture on the resulting `lag_days`.

- **Estimated Causal Effect**: Adopting a "Neutral/Mixed" posture is estimated to change the lag time by **{causal_effect:.2f} days**.
- **Statistical Significance**: {significance_text}

## Refutation Test Results

Refutation tests challenge the validity of the causal estimate.

### 1. Random Common Cause Refutation

- **Purpose**: This test assesses if the model's estimate is sensitive to a random, unobserved confounding variable. A robust model should not change significantly.
- **Result**: The estimated effect after introducing a random common cause was {refute_random.new_effect:.2f}.

### 2. Placebo Treatment Refutation

- **Purpose**: This test replaces the actual treatment variable with a random placebo. If the original effect was genuine, the new effect should be close to zero.
- **Result**: The new effect calculated with the placebo treatment was {refute_placebo.new_effect:.2f}.

## Conclusion

{conclusion_text}
"""

with open(os.path.join(GEMINI_DIR, 'causal_summary.md'), 'w') as f:
    f.write(report)

print("Corrected causal analysis complete. `causal_analysis.py` executed and `causal_summary.md` has been regenerated.")

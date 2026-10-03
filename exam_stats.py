import pandas as pd
import numpy as np
from scipy import stats

scores = pd.Series([
    72, 65, 88, np.nan, 54,
    91, 76, np.nan, 83, 69
])
print("Exam Scores:")
print(scores)
print("\nDescriptive Statistics:")
print(scores.describe())

clean_scores = scores.dropna()
skewness = stats.skew(clean_scores)
kurtosis = stats.kurtosis(clean_scores)

print("\nDistribution Shape:")
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

missing_values = scores.isnull().sum()

print("\nMissing values:", missing_values)

mean_score = scores.mean()

filled_scores = scores.fillna(mean_score)

print("\nMean score:", mean_score)

print("\nFilled scores:")
print(filled_scores)
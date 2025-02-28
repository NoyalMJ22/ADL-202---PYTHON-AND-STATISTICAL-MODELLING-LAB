import pandas as pd
import numpy as np
data = {
    'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware'],
    'Population': [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934],
    'Murder Rate': [5.7, 5.6, 4.7, 5.6, 4.4, 2.8, 2.4, 5.8]
}

df = pd.DataFrame(data)
weightedmean = np.average(df['Murder Rate'], weights=df['Population'])

weightedvariance = np.average((df['Murder Rate'] - weightedmean)**2, weights=df['Population'])

stddev = np.sqrt(weightedvariance)

coeffofvariation = (stddev / weightedmean) * 100

print(f"Weighted Mean (μ): {weightedmean:.2f}")
print(f"Standard Deviation (σ): {stddev:.2f}")
print(f"Coefficient of Variation (C.V.): {coeffofvariation:.2f}")

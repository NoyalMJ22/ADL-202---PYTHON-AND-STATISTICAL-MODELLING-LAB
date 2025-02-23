import pandas as pd
from sklearn.model_selection import train_test_split

file_path = "train.csv"  
df = pd.read_csv(file_path)

df_filtered = df.dropna(subset=['Home Ownership'])

stratify_column = 'Home Ownership'

train, test = train_test_split(
    df_filtered, test_size=0.2, stratify=df_filtered[stratify_column], random_state=42
)

train_proportions = train[stratify_column].value_counts(normalize=True)
test_proportions = test[stratify_column].value_counts(normalize=True)

print("Training Set Proportions:")
print(train_proportions)

print("\nTesting Set Proportions:")
print(test_proportions)

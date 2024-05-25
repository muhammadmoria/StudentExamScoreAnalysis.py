import pandas as pd
import numpy as np

np.random.seed(0)
data = {
    'StudentID': np.arange(1, 101),
    'Math_Score': np.random.randint(50, 100, size=100),
    'Science_Score': np.random.randint(40, 95, size=100),
    'English_Score': np.random.randint(45, 90, size=100)
}
df = pd.DataFrame(data)

df['Average_Score'] = df[['Math_Score', 'Science_Score', 'English_Score']].mean(axis=1)

print("Top 5 rows of the dataset:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

correlation_matrix = df[['Math_Score', 'Science_Score', 'English_Score', 'Average_Score']].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)
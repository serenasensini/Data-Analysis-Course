# pandas introduction

import pandas as pd

# Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like DataFrames and Series, which allow for easy handling of structured data.
# Create a sample CSV file with some dummy data about salary and age of employees.

# Example 1: Load a CSV file into a DataFrame
df = pd.read_csv('data/employee_data.csv')

# Example 2: Display basic information about the DataFrame
print(df.head())          # Show first 5 rows
print(df.info())          # Show column types and non-null counts
print(df.describe())      # Show statistical summary of numerical columns
print(df.columns)         # List all column names
print(df.shape)           # Show (rows, columns)

# Example 3: Filter data based on conditions
filtered_df = df[df['Age'] > 30]                    # Single condition
filtered_df = df[(df['Age'] > 30) & (df['Salary'] > 50000)]  # Multiple conditions

# Example 4: Perform basic statistical operations
mean_value = df['Age'].mean()
max_value = df['Salary'].max()
min_value = df['Salary'].min()
sum_value = df['Sales'].sum()
#
# Example 5: Group data and calculate aggregates
grouped = df.groupby('Department')['Salary'].mean()
grouped_multi = df.groupby('Department').agg({'Salary': 'mean', 'Age': 'max'})

# Example 6: Handle missing data
df_cleaned = df.dropna()                    # Remove rows with any missing values
df_filled = df.fillna(0)                    # Fill missing values with 0
df_filled = df.fillna(df.mean())           # Fill with column mean

# Example 7: Save processed data to a new CSV file
df.to_csv('output.csv', index=False)

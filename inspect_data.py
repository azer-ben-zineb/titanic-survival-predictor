import pandas as pd
import numpy as np

df = pd.read_csv("/home/azer/Documents/minprojai/titanicall.csv")
print("=== SHAPE ===")
print(df.shape)
print("\n=== COLUMNS & DTYPES & MISSING ===")
summary = pd.DataFrame({
    'dtype': df.dtypes,
    'missing_count': df.isna().sum(),
    'missing_pct': (df.isna().sum() / len(df) * 100).round(2),
    'num_unique': df.nunique()
})
print(summary.to_string())

cols_to_check = ['Pclass', 'Person_Role', 'Class_Dept', 'Occupation', 'Job', 'Embarked', 'Title', 'Split', 'Survived']
for col in cols_to_check:
    print(f"\n=== UNIQUE VALUES OF {col} (Top 20) ===")
    print(df[col].value_counts(dropna=False).head(20))

print("\n=== PCLASS BREAKDOWN ===")
print(df['Pclass'].value_counts(dropna=False))

print("\n=== SEX vs Female / Male ===")
print("Sex counts:")
print(df['Sex'].value_counts(dropna=False))
print("Female col counts:")
print(df['Female'].value_counts(dropna=False))
print("Male col counts:")
print(df['Male'].value_counts(dropna=False))
if 'Female' in df.columns and 'Male' in df.columns:
    incon_f = df[(df['Sex'] == 'female') & (df['Female'] != 1)]
    incon_m = df[(df['Sex'] == 'male') & (df['Male'] != 1)]
    print(f"Female col mismatches: {len(incon_f)}, Male col mismatches: {len(incon_m)}")

print("\n=== CREW FLAGS vs Person_Role ===")
crew_cols = [c for c in ['Normal_Passenger', 'Engineering_Crew', 'Other_Crew'] if c in df.columns]
print(df.groupby('Person_Role')[crew_cols].mean())

print("\n=== SPLIT CHECK ===")
print(df['Split'].value_counts(dropna=False))
print("\nSurvived by Split:")
print(pd.crosstab(df['Split'], df['Survived'], normalize='index'))

print("\n=== OCCUPATION & JOB CHECK ===")
musicians = df[(df['Occupation'].astype(str).str.contains('Musician|music', case=False, na=False)) |
               (df['Job'].astype(str).str.contains('Musician|music', case=False, na=False))]
print(f"Found {len(musicians)} musician rows:")
print(musicians[['Name', 'Person_Role', 'Pclass', 'Occupation', 'Job', 'Survived']])

print("\n=== DUPLICATES CHECK ===")
print("Duplicate PassengerIds:", df['PassengerId'].duplicated().sum())
print("Duplicate Name:", df['Name'].duplicated().sum())
print("Exact duplicate rows across all cols:", df.duplicated().sum())

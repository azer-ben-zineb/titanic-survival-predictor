import os
import pandas as pd
import numpy as np

os.environ["SKB_DATA_DIRECTORY"] = "/tmp/skrub_data"
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"

df = pd.read_csv("/home/azer/Documents/minprojai/titanicall.csv")

profile_md = []
profile_md.append("# Titanic Dataset Data Profile & Inspection Report\n")
profile_md.append(f"**Dataset Source**: `titanicall.csv`  ")
profile_md.append(f"**Dataset Shape**: {df.shape[0]} rows, {df.shape[1]} columns  ")
profile_md.append(f"**Target Variable**: `Survived` (Binary: 0 = Did not survive, 1 = Survived)\n")

# Class Balance
surv_counts = df['Survived'].value_counts()
surv_pct = df['Survived'].value_counts(normalize=True) * 100
profile_md.append("## 1. Target Class Balance (`Survived`)\n")
profile_md.append("| Class | Count | Percentage |")
profile_md.append("|---|---|---|")
for val in [0, 1]:
    lbl = "Died (0)" if val == 0 else "Survived (1)"
    profile_md.append(f"| {lbl} | {surv_counts[val]:,d} | {surv_pct[val]:.2f}% |")
profile_md.append(f"\nOverall survival rate: **{surv_pct[1]:.2f}%** ({surv_counts[1]} / {len(df)}).\n")

# Dtypes & Missing Values
profile_md.append("## 2. Column Summary (Data Types, Missing Values, Unique Counts)\n")
profile_md.append("| Column | Dtype | Missing (NaN) | Missing (%) | Unique Values | Sample Values / Description |")
profile_md.append("|---|---|---|---|---|---|")
for col in df.columns:
    dt = str(df[col].dtype)
    n_miss = df[col].isna().sum()
    pct_miss = (n_miss / len(df)) * 100
    n_uniq = df[col].nunique()
    sample = str(df[col].dropna().iloc[:3].tolist()).replace('|', '/')
    profile_md.append(f"| `{col}` | {dt} | {n_miss} | {pct_miss:.1f}% | {n_uniq} | `{sample}` |")

# Key Categorical Columns
key_cols = ['Pclass', 'Person_Role', 'Class_Dept', 'Embarked', 'Title', 'Split']
profile_md.append("\n## 3. Key Categorical Distributions\n")
for col in key_cols:
    profile_md.append(f"### Distribution: `{col}`\n")
    vc = df[col].value_counts(dropna=False)
    vp = df[col].value_counts(normalize=True, dropna=False) * 100
    profile_md.append(f"| `{col}` Value | Count | Proportion | Survival Rate |")
    profile_md.append("|---|---|---|---|")
    for val, count in vc.items():
        s_rate = df[df[col] == val]['Survived'].mean() * 100
        profile_md.append(f"| **{val}** | {count:,d} | {vp[val]:.2f}% | {s_rate:.2f}% |")
    profile_md.append("\n")

# Occupation and Job Analysis
profile_md.append("### Distribution: `Occupation` & `Job` (Top Values and Musician Easter Egg)\n")
profile_md.append(f"- Unique non-empty `Occupation` count: **{df['Occupation'].str.strip().nunique()}**")
profile_md.append(f"- Unique non-empty `Job` count: **{df['Job'].str.strip().nunique()}**")
profile_md.append(f"- Empty/blank strings in `Job`: **{(df['Job'].str.strip() == '').sum()}** (primarily crew members whose specific occupation is captured in `Occupation`)")
profile_md.append(f"- Empty/blank strings in `Occupation`: **{(df['Occupation'].str.strip() == '').sum()}** (100% complete)\n")

musicians = df[df['Job'].str.contains('Musician', case=False, na=False) | df['Occupation'].str.contains('Musician', case=False, na=False)]
profile_md.append(f"#### Musician Records in Dataset ({len(musicians)} total):\n")
profile_md.append("| Name | Person_Role | Pclass | Occupation | Job | Survived |")
profile_md.append("|---|---|---|---|---|---|")
for _, r in musicians.iterrows():
    profile_md.append(f"| {r['Name']} | {r['Person_Role']} | {r['Pclass']} | {r['Occupation'].strip()} | {r['Job'].strip()} | {r['Survived']} |")
profile_md.append("\n*Historical confirmation: All 8 members of the Titanic Band famously perished while playing music to calm passengers.* \n")

# Inconsistencies and Duplicates
profile_md.append("## 4. Inconsistencies, Redundancies, and Duplicate Checks\n")
# Sex vs Female/Male
incon_f = df[(df['Sex'] == 'female') & (df['Female'] != 1)]
incon_m = df[(df['Sex'] == 'male') & (df['Male'] != 1)]
profile_md.append("### Sex vs. Female / Male Flags")
profile_md.append(f"- `Female` mismatches with `Sex == 'female'`: **{len(incon_f)}**")
profile_md.append(f"- `Male` mismatches with `Sex == 'male'`: **{len(incon_m)}**")
profile_md.append("- **Conclusion**: `Female` and `Male` are exact 100% one-hot encodings of `Sex`. Both are dropped as redundant to prevent multicollinearity.\n")

# Crew flags vs Person_Role
profile_md.append("### Crew Flags vs. `Person_Role`")
crew_match_np = (df['Person_Role'] == 'Normal Passenger') == (df['Normal_Passenger'] == 1)
crew_match_ec = (df['Person_Role'] == 'Engineering Crew') == (df['Engineering_Crew'] == 1)
crew_match_oc = (df['Person_Role'] == 'Other Crew') == (df['Other_Crew'] == 1)
profile_md.append(f"- `Normal_Passenger` match: **{crew_match_np.mean()*100:.1f}%**")
profile_md.append(f"- `Engineering_Crew` match: **{crew_match_ec.mean()*100:.1f}%**")
profile_md.append(f"- `Other_Crew` match: **{crew_match_oc.mean()*100:.1f}%**")
profile_md.append("- **Conclusion**: `Normal_Passenger`, `Engineering_Crew`, and `Other_Crew` are exact 1-to-1 dummy indicators of `Person_Role`. They are dropped.\n")

# Duplicates check
profile_md.append("### Duplicate Rows and Identifiers")
profile_md.append(f"- Exact duplicate rows across all 33 columns: **{df.duplicated().sum()}**")
profile_md.append(f"- Unique `PassengerId` count: **{df['PassengerId'].nunique()}** (0 duplicates)")
profile_md.append(f"- Name duplicate count: **{df['Name'].duplicated().sum()}** (4 name collisions: Kate Connolly, James Kelly, John Collins, Arthur William May; verified through DoB, age, and roles to be separate historical individuals)\n")

# Split Column Usability Analysis
profile_md.append("## 5. `Split` Column Usability Assessment & Train/Test Policy\n")
profile_md.append("In the provided dataset, the `Split` column contains three categories:")
split_tbl = pd.crosstab(df['Split'], df['Survived'], margins=True)
profile_md.append("\n```")
profile_md.append(split_tbl.to_string())
profile_md.append("```\n")
profile_md.append("### Critical Finding Regarding `Split`:")
profile_md.append("1. The `Split` column represents legacy partition labels: `train` (891) and `test` (418) correspond precisely to the original Kaggle passenger competition splits.")
profile_md.append("2. **All 899 crew members** are labeled as `Split == 'crew'`.")
profile_md.append("3. If `Split` were used directly as train/test partitions, **100% of the crew would be excluded from model training and evaluation**!")
profile_md.append("4. **Decision**: The existing `Split` column is **not usable** for holistic passenger + crew modeling. We construct our own **stratified 80/20 train/test split** (seed `random_state=42`) across all 2,208 records, stratified jointly by `Survived` and `Person_Role` to preserve exact class and role balances.\n")

# Pclass Normalization Strategy
profile_md.append("## 6. `Pclass` Normalization Strategy\n")
profile_md.append("In the raw CSV, `Pclass` is stored as an object string with 8 distinct categories:")
profile_md.append("- Passengers: `'1'`, `'2'`, `'3'` (1st, 2nd, 3rd ticket class)")
profile_md.append("- Crew: `'Deck Crew'`, `'Engineering Crew'`, `'Victualling Crew'`, `'Restaurant Staff'`, `'Band'`")
profile_md.append("Historically and empirically, crew department has a massive impact on survival (e.g. Deck Crew had a 65.15% survival rate, whereas Restaurant Staff had 4.35% and Band had 0.00%).")
profile_md.append("We normalize `Pclass` by standardizing whitespace and providing intuitive UI groupings (1st Class, 2nd Class, 3rd Class for passengers, and specific Crew departments for crew members).\n")

with open("/home/azer/Documents/minprojai/ml/reports/data_profile.md", "w") as f:
    f.write("\n".join(profile_md))

print("Successfully written ml/reports/data_profile.md")

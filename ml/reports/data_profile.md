# Titanic Dataset Data Profile & Inspection Report

**Dataset Source**: `titanicall.csv`  
**Dataset Shape**: 2208 rows, 33 columns  
**Target Variable**: `Survived` (Binary: 0 = Did not survive, 1 = Survived)

## 1. Target Class Balance (`Survived`)

| Class | Count | Percentage |
|---|---|---|
| Died (0) | 1,496 | 67.75% |
| Survived (1) | 712 | 32.25% |

Overall survival rate: **32.25%** (712 / 2208).

## 2. Column Summary (Data Types, Missing Values, Unique Counts)

| Column | Dtype | Missing (NaN) | Missing (%) | Unique Values | Sample Values / Description |
|---|---|---|---|---|---|
| `PassengerId` | int64 | 0 | 0.0% | 2208 | `[731, 306, 298]` |
| `Survived` | int64 | 0 | 0.0% | 2 | `[1, 1, 0]` |
| `Pclass` | str | 0 | 0.0% | 8 | `['1', '1', '1']` |
| `Name` | str | 0 | 0.0% | 2204 | `['Allen, Miss. Elisabeth Walton', 'Allison, Master. Hudson Trevor', 'Allison, Miss. Helen Loraine']` |
| `Sex` | str | 0 | 0.0% | 2 | `['female', 'male', 'female']` |
| `Age` | float64 | 0 | 0.0% | 102 | `[29.0, 0.9, 2.0]` |
| `Height_cm` | float64 | 0 | 0.0% | 313 | `[161.1, 74.0, 86.0]` |
| `Weight_kg` | float64 | 0 | 0.0% | 398 | `[58.5, 9.5, 12.5]` |
| `SibSp` | int64 | 0 | 0.0% | 7 | `[0, 1, 1]` |
| `Parch` | int64 | 0 | 0.0% | 8 | `[0, 2, 2]` |
| `Ticket` | str | 0 | 0.0% | 931 | `['24160', '113781', '113781']` |
| `Fare` | float64 | 0 | 0.0% | 281 | `[211.3375, 151.55, 151.55]` |
| `Cabin` | str | 0 | 0.0% | 188 | `['B5', 'C22 C26', 'C22 C26']` |
| `Embarked` | str | 0 | 0.0% | 4 | `['S', 'S', 'S']` |
| `Boat` | str | 0 | 0.0% | 29 | `['2', '11', 'No Boat']` |
| `Body` | str | 0 | 0.0% | 246 | `['No Body Recovered', 'No Body Recovered', 'No Body Recovered']` |
| `Home_Dest` | str | 0 | 0.0% | 372 | `['St Louis, MO', 'Montreal, PQ / Chesterville, ON', 'Montreal, PQ / Chesterville, ON']` |
| `LastName` | str | 0 | 0.0% | 1597 | `['Allen', 'Allison', 'Allison']` |
| `FirstName` | str | 0 | 0.0% | 1705 | `['Elisabeth Walton', 'Hudson Trevor', 'Helen Loraine']` |
| `Title` | str | 0 | 0.0% | 19 | `['Miss', 'Master', 'Miss']` |
| `Female` | int64 | 0 | 0.0% | 2 | `[1, 0, 1]` |
| `Male` | int64 | 0 | 0.0% | 2 | `[0, 1, 0]` |
| `Class_Dept` | str | 0 | 0.0% | 8 | `['1 Class Passenger', '1 Class Passenger', '1 Class Passenger']` |
| `Occupation` | str | 0 | 0.0% | 360 | `['Passenger', 'Passenger', 'Passenger']` |
| `Job` | str | 0 | 0.0% | 135 | `['Passenger', 'Passenger', 'Passenger']` |
| `URL` | str | 0 | 0.0% | 2208 | `['/titanic-survivor/elisabeth-walton-allen.html', '/titanic-survivor/trevor-allison.html', '/titanic-victim/loraine-allison.html']` |
| `DoB` | str | 0 | 0.0% | 1108 | `['1882-10-01', '1911-05-07 00:00:00', '1909-06-05 00:00:00']` |
| `Date_Death` | str | 0 | 0.0% | 479 | `['1967-12-15 00:00:00', '1929-08-07 00:00:00', '1912-04-15 00:00:00']` |
| `Split` | str | 0 | 0.0% | 3 | `['train', 'train', 'train']` |
| `Normal_Passenger` | int64 | 0 | 0.0% | 2 | `[1, 1, 1]` |
| `Engineering_Crew` | int64 | 0 | 0.0% | 2 | `[0, 0, 0]` |
| `Other_Crew` | int64 | 0 | 0.0% | 2 | `[0, 0, 0]` |
| `Person_Role` | str | 0 | 0.0% | 3 | `['Normal Passenger', 'Normal Passenger', 'Normal Passenger']` |

## 3. Key Categorical Distributions

### Distribution: `Pclass`

| `Pclass` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **3** | 709 | 32.11% | 25.53% |
| **Victualling Crew** | 431 | 19.52% | 21.81% |
| **Engineering Crew** | 325 | 14.72% | 22.15% |
| **1** | 323 | 14.63% | 61.92% |
| **2** | 277 | 12.55% | 42.96% |
| **Restaurant Staff** | 69 | 3.12% | 4.35% |
| **Deck Crew** | 66 | 2.99% | 65.15% |
| **Band** | 8 | 0.36% | 0.00% |


### Distribution: `Person_Role`

| `Person_Role` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **Normal Passenger** | 1,309 | 59.28% | 38.20% |
| **Other Crew** | 574 | 26.00% | 24.39% |
| **Engineering Crew** | 325 | 14.72% | 22.15% |


### Distribution: `Class_Dept`

| `Class_Dept` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **3 Class Passenger** | 709 | 32.11% | 25.53% |
| **Victualling Crew** | 431 | 19.52% | 21.81% |
| **Engineering Crew** | 325 | 14.72% | 22.15% |
| **1 Class Passenger** | 323 | 14.63% | 61.92% |
| **2 Class Passenger** | 277 | 12.55% | 42.96% |
| **Restaurant Staff** | 69 | 3.12% | 4.35% |
| **Deck Crew** | 66 | 2.99% | 65.15% |
| **Band** | 8 | 0.36% | 0.00% |


### Distribution: `Embarked`

| `Embarked` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **S** | 1,626 | 73.64% | 29.15% |
| **C** | 270 | 12.23% | 55.56% |
| **B** | 189 | 8.56% | 23.28% |
| **Q** | 123 | 5.57% | 35.77% |


### Distribution: `Title`

| `Title` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **Mr** | 1,585 | 71.78% | 19.81% |
| **Miss** | 273 | 12.36% | 68.50% |
| **Mrs** | 209 | 9.47% | 78.95% |
| **Master** | 61 | 2.76% | 50.82% |
| **Sig** | 42 | 1.90% | 0.00% |
| **Dr** | 10 | 0.45% | 40.00% |
| **Rev** | 8 | 0.36% | 0.00% |
| **Col** | 4 | 0.18% | 50.00% |
| **Major** | 4 | 0.18% | 50.00% |
| **Mlle** | 2 | 0.09% | 100.00% |
| **Ms** | 2 | 0.09% | 50.00% |
| **Mme** | 1 | 0.05% | 100.00% |
| **Capt** | 1 | 0.05% | 0.00% |
| **Lady** | 1 | 0.05% | 100.00% |
| **Sir** | 1 | 0.05% | 100.00% |
| **Dona** | 1 | 0.05% | 100.00% |
| **Jonkheer** | 1 | 0.05% | 0.00% |
| **Don** | 1 | 0.05% | 0.00% |
| **Sr** | 1 | 0.05% | 0.00% |


### Distribution: `Split`

| `Split` Value | Count | Proportion | Survival Rate |
|---|---|---|---|
| **crew** | 899 | 40.72% | 23.58% |
| **train** | 891 | 40.35% | 38.38% |
| **test** | 418 | 18.93% | 37.80% |


### Distribution: `Occupation` & `Job` (Top Values and Musician Easter Egg)

- Unique non-empty `Occupation` count: **360**
- Unique non-empty `Job` count: **133**
- Empty/blank strings in `Job`: **883** (primarily crew members whose specific occupation is captured in `Occupation`)
- Empty/blank strings in `Occupation`: **0** (100% complete)

#### Musician Records in Dataset (9 total):

| Name | Person_Role | Pclass | Occupation | Job | Survived |
|---|---|---|---|---|---|
| Corbett, Mrs. Walter H (Irene Colvin) | Normal Passenger | 2 | Musician | Musician | 0 |
| BRICOUX, Mr Roger Marie  | Other Crew | Band | Musician | Musician | 0 |
| HUME, Mr John Law  | Other Crew | Band | Musician | Musician | 0 |
| KRINS, Mr Georges Alexandre  | Other Crew | Band | Musician | Musician | 0 |
| BRAILEY, Mr William Theodore Ronald  | Other Crew | Band | Musician | Musician | 0 |
| CLARKE, Mr John Frederick Preston  | Other Crew | Band | Musician | Musician | 0 |
| TAYLOR, Mr Percy Cornelius  | Other Crew | Band | Musician | Musician | 0 |
| WOODWARD, Mr John Wesley  | Other Crew | Band | Musician | Musician | 0 |
| HARTLEY, Mr Wallace Henry  | Other Crew | Band | Musician | Musician | 0 |

*Historical confirmation: All 8 members of the Titanic Band famously perished while playing music to calm passengers.* 

## 4. Inconsistencies, Redundancies, and Duplicate Checks

### Sex vs. Female / Male Flags
- `Female` mismatches with `Sex == 'female'`: **0**
- `Male` mismatches with `Sex == 'male'`: **0**
- **Conclusion**: `Female` and `Male` are exact 100% one-hot encodings of `Sex`. Both are dropped as redundant to prevent multicollinearity.

### Crew Flags vs. `Person_Role`
- `Normal_Passenger` match: **100.0%**
- `Engineering_Crew` match: **100.0%**
- `Other_Crew` match: **100.0%**
- **Conclusion**: `Normal_Passenger`, `Engineering_Crew`, and `Other_Crew` are exact 1-to-1 dummy indicators of `Person_Role`. They are dropped.

### Duplicate Rows and Identifiers
- Exact duplicate rows across all 33 columns: **0**
- Unique `PassengerId` count: **2208** (0 duplicates)
- Name duplicate count: **4** (4 name collisions: Kate Connolly, James Kelly, John Collins, Arthur William May; verified through DoB, age, and roles to be separate historical individuals)

## 5. `Split` Column Usability Assessment & Train/Test Policy

In the provided dataset, the `Split` column contains three categories:

```
Survived     0    1   All
Split                    
crew       687  212   899
test       260  158   418
train      549  342   891
All       1496  712  2208
```

### Critical Finding Regarding `Split`:
1. The `Split` column represents legacy partition labels: `train` (891) and `test` (418) correspond precisely to the original Kaggle passenger competition splits.
2. **All 899 crew members** are labeled as `Split == 'crew'`.
3. If `Split` were used directly as train/test partitions, **100% of the crew would be excluded from model training and evaluation**!
4. **Decision**: The existing `Split` column is **not usable** for holistic passenger + crew modeling. We construct our own **stratified 80/20 train/test split** (seed `random_state=42`) across all 2,208 records, stratified jointly by `Survived` and `Person_Role` to preserve exact class and role balances.

## 6. `Pclass` Normalization Strategy

In the raw CSV, `Pclass` is stored as an object string with 8 distinct categories:
- Passengers: `'1'`, `'2'`, `'3'` (1st, 2nd, 3rd ticket class)
- Crew: `'Deck Crew'`, `'Engineering Crew'`, `'Victualling Crew'`, `'Restaurant Staff'`, `'Band'`
Historically and empirically, crew department has a massive impact on survival (e.g. Deck Crew had a 65.15% survival rate, whereas Restaurant Staff had 4.35% and Band had 0.00%).
We normalize `Pclass` by standardizing whitespace and providing intuitive UI groupings (1st Class, 2nd Class, 3rd Class for passengers, and specific Crew departments for crew members).

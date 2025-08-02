
 #  Medical Data Visualizer

This project is part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/). It involves processing and visualizing medical examination data to explore health indicators related to cardiovascular disease.

---

##  Dataset Description: `medical_examination_with_bmi.csv`

This dataset contains processed medical examination records for a group of patients. The data has been cleaned and enhanced to support analysis of health risk factors and their association with cardiovascular disease.

## Features (Columns):

| Column         | Description |
|----------------|-------------|
| `age`          | Age in days. |
| `sex`          | Gender (1 = female, 2 = male). |
| `height`       | Height in centimeters. |
| `weight`       | Weight in kilograms. |
| `ap_hi`        | Systolic blood pressure. |
| `ap_lo`        | Diastolic blood pressure. |
| `cholesterol`  | Cholesterol level (normalized: 0 = normal, 1 = above normal). |
| `gluc`         | Glucose level (normalized: 0 = normal, 1 = above normal). |
| `smoke`        | Smoking status (0 = no, 1 = yes). |
| `alco`         | Alcohol intake (0 = no, 1 = yes). |
| `active`       | Physical activity (0 = no, 1 = yes). |
| `cardio`       | Presence of cardiovascular disease (0 = no, 1 = yes). |
| `overweight`   | **New column**: Calculated using BMI (Body Mass Index). Value is 1 if BMI > 25, else 0. |

---

##  Preprocessing Steps

- Dropped the `id` column as it was not relevant for analysis.
- Added a new `overweight` column based on BMI calculation:  
  `BMI = weight (kg) / (height (m))²`
- Normalized `cholesterol` and `gluc` values:
  - 0 = normal
  - 1 = elevated (original values > 1)
- Cleaned outliers in height, weight, and incorrect blood pressure entries (for heatmap).

---

##  Visualizations

###  Categorical Plot

Shows the distribution of health risk factors (`cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`) for patients with and without cardiovascular disease.

###  Correlation Heatmap

Displays the correlations between all numerical variables after cleaning the data.

---

## Running the Project

```bash
# Run the visualization
python main.py


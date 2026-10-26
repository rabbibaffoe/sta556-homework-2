# STA 556 Homework 2: Sleep, Stress, and Sleep Quality

## Purpose
A small, reproducible data-analysis pipeline that reads an external CSV file, cleans it with reusable functions, answers three exploratory questions, and communicates the results with three saved figures.

## Data source
**Sleep Health and Lifestyle Dataset**, a CSV file distributed on Kaggle:
<https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset>

- Local copy: `data/Sleep_health_and_lifestyle_dataset.csv` 
- Variables used: `Sleep Duration` (hours), `Quality of Sleep` (reported score), `Stress Level` (reported score).
- Other columns (age, occupation, BMI category, blood pressure, heart rate, daily steps, sleep disorder) are loaded but not analyzed.
- Check the license and terms on the Kaggle page before redistributing the file. If you cannot redistribute it, download it from the link above and save it at the path shown.

## Questions
1. What is the distribution of nightly sleep duration?
2. How does sleep quality vary across reported stress levels?
3. How are sleep duration and sleep quality related?

## Main finding
- Sleep duration averages about **7.13 hours** (median 7.2; range 5.8 to 8.5).
- Mean sleep quality falls from **8.97** at stress level 3 to **5.86** at stress level 8. The decline is not strictly monotonic (7.67 at level 4 vs. 7.90 at level 5).
- Sleep duration and sleep quality are strongly positively correlated (**r = 0.883**).

These are descriptive associations in this file, not causal findings.

## Project structure
```text
data/        supplied CSV
src/         sleep_utils.py: reusable, documented functions
notebooks/   sleep_analysis.ipynb: analysis, figures, and explanations
figures/     three 300-dpi PNG figures written by the notebook
requirements.txt
.gitignore
```

Functions in `src/sleep_utils.py`:

| Function | Purpose |
|---|---|
| `load_data(path)` | Read the CSV from a relative path |
| `clean_columns(data)` | Return a copy with lowercase, underscore-separated column names |
| `filter_records(data)` | Keep rows with valid sleep duration (0 to 24 hours), sleep quality (1 to 10) and stress level (1 to 10); raises an error if required columns are missing |
| `summarize_group(data, group_col, value_col)` | Count, mean and median of a numeric variable by group |
| `prepare_analysis(data)` | Compose column cleaning and filtering without modifying the input |

## Data cleaning notes
- All 374 rows pass the validity checks, so none are dropped.
- The `Sleep Disorder` column uses the text value `None` for people with no recorded disorder (219 rows). pandas' default CSV reader converts `None` to a missing value, so it appears as `NaN` in the notebook. That column is not used in the analysis. Anyone who analyzes it should read the file with `keep_default_na=False` so that `None` stays a valid category.
- Many rows are identical apart from `Person ID` (242 of 374), which is unusual for survey data. Treat the results as illustrations of the methods and not as estimates for a real population. The sampling design is not documented here.
- Quality and stress are integer scores with few distinct values, so they are summarized descriptively and no model is fitted.

## Run locally or in GitHub Codespaces
Requires Python 3.10 or newer (the code uses `str | Path` type hints).

1. Open a terminal at the repository root.
2. Run `python -m pip install -r requirements.txt`.
3. Run `jupyter notebook notebooks/sleep_analysis.ipynb`, or open the notebook in VS Code.
4. Run all cells from top to bottom.

The notebook uses paths relative to its own folder (`../data/...`, `../figures/...`), so it must run with `notebooks/` as the working directory. Jupyter does this automatically. Figures are written to `figures/` when the notebook is run.

# STA 556 Homework 2 — Sleep Health and Lifestyle

## Purpose
A reproducible exploratory analysis of reported sleep duration, sleep quality, and stress levels using a CSV file, modular cleaning functions, and three visualizations.

## Data source
**Sleep Health and Lifestyle Dataset**, CSV supplied for this assignment (`data/Sleep_health_and_lifestyle_dataset.csv`), 374 rows and 13 original columns. This dataset is commonly distributed on Kaggle. **Before submitting:** add the exact original dataset page/download URL and confirm that your instructor has approved this source. The original file is included for reproducibility; verify redistribution permissions with the original source if needed.

## Questions
1. What is the distribution of nightly sleep duration?
2. How does sleep quality vary across reported stress levels?
3. How are sleep duration and sleep quality related?

## Main finding
The average sleep duration is approximately **7.13 hours**. Mean sleep quality is approximately **8.97** at stress level 3 versus **5.86** at stress level 8. Sleep duration and sleep quality have a strong positive Pearson correlation (**r ≈ 0.883**). These are descriptive associations, not causal findings.

## Folder structure
- `data/` — supplied CSV
- `src/sleep_utils.py` — reusable documented functions
- `notebooks/sleep_analysis.ipynb` — reproducible analysis and explanations
- `figures/` — three saved 300-dpi PNG charts

## Run locally or in GitHub Codespaces
1. Open a terminal at the **repository root**.
2. Run `python -m pip install -r requirements.txt`.
3. Run `jupyter notebook notebooks/sleep_analysis.ipynb` (or open it in VS Code).
4. Run all notebook cells from top to bottom. Relative paths are based on the repository root.

## Notes
219 entries in the original `Sleep Disorder` field are blank. This field is not used in the analysis and blanks are not interpreted as absence of a disorder. Reported stress and quality scales are treated descriptively. The dataset's sampling design is not established here.

## Submission
Create a **new, public GitHub repository** (for example `sta556-homework-2`), upload/commit/push this complete project, open its URL in a private/incognito window to verify public visibility, and submit the **repository main-page URL** in Canvas for Homework 2 by **October 26, 2026**. Do not submit a ZIP or notebook instead of the URL.

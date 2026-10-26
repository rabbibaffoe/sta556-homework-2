"""Reusable data preparation and summary functions"""
from pathlib import Path
import pandas as pd


def load_data(path):
    """Load the Sleep Health and Lifestyle dataset."""
    return pd.read_csv(path, keep_default_na=False)


def clean_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with lowercase, underscore-separated column names."""
    clean = data.copy()
    clean.columns = clean.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    return clean


def filter_records(data: pd.DataFrame) -> pd.DataFrame:
    """Keep records with valid sleep duration, quality, and stress measurements."""
    required = ["sleep_duration", "quality_of_sleep", "stress_level"]
    if not set(required).issubset(data.columns):
        raise ValueError(f"Missing required columns: {set(required) - set(data.columns)}")
    clean = data.dropna(subset=required).copy()
    clean = clean.loc[
        clean["sleep_duration"].between(0, 24)
        & clean["quality_of_sleep"].between(1, 10)
        & clean["stress_level"].between(1, 10)
    ].copy()
    return clean


def summarize_group(data: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Return sample sizes, means, and medians for a numeric variable by group."""
    if group_col not in data.columns or value_col not in data.columns:
        raise ValueError("Group and value columns must exist in the dataset")
    return data.groupby(group_col, as_index=False)[value_col].agg(
        count="count", mean="mean", median="median"
    )


def prepare_analysis(data: pd.DataFrame) -> pd.DataFrame:
    """Compose column cleaning and valid-record filtering without mutating input."""
    return filter_records(clean_columns(data))

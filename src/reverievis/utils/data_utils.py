"""Data processing utilities for ReverieVis package."""

from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from reverievis.core.constants import ValidationMessages


def create_data_structure(data: pd.DataFrame, category: str, values: List[str]) -> Dict[str, np.ndarray]:
    """Create data structure for radar chart visualization.

    Args:
        data (pd.DataFrame): Input data containing categories and values.
        category (str): Column name for categories.
        values (List[str]): Column names for values to plot.

    Returns:
        Dict[str, np.ndarray]: Dictionary mapping categories to value arrays.

    Raises:
        ValueError: If data is empty or required columns are missing.
    """
    if data.empty:
        raise ValueError(ValidationMessages.DATA_EMPTY)

    if category not in data.columns:
        raise ValueError(ValidationMessages.COLUMN_NOT_FOUND.format(category))

    for value_col in values:
        if value_col not in data.columns:
            raise ValueError(ValidationMessages.COLUMN_NOT_FOUND.format(value_col))

    data_radar = {}
    data_category = data[category].unique()
    data_values = data[values].to_numpy()

    for idx, val in enumerate(data_values):
        result = val.copy()
        # Append first value to close the polygon
        result = np.append(result, val[:1])
        data_radar[data_category[idx]] = result

    return data_radar


def normalize_minmax(
    data: pd.DataFrame, category: str, data_minmax: Optional[Dict] = None, vmin: float = 0, vmax: float = 1
) -> pd.DataFrame:
    """Normalize data using min-max scaling.

    Args:
        data (pd.DataFrame): Input data to normalize.
        category (str): Column name for categories (excluded from normalization).
        data_minmax (Optional[Dict]): Pre-computed min/max values. Defaults to None.
        vmin (float): Minimum value for scaling. Defaults to 0.
        vmax (float): Maximum value for scaling. Defaults to 1.

    Returns:
        pd.DataFrame: Normalized data with category column preserved.

    Raises:
        ValueError: If vmin >= vmax or if data contains non-numeric values.
    """
    if vmin >= vmax:
        raise ValueError(ValidationMessages.INVALID_VMIN_VMAX)

    # Create copies to avoid modifying original data
    value = data.copy()
    data_scaled = data.copy()

    # Separate category and value columns
    data_scaled = data_scaled[[category]]
    value_scaled = value.drop(category, axis=1)

    # Validate that value columns contain numeric data
    for column in value_scaled.columns:
        if not pd.api.types.is_numeric_dtype(value_scaled[column]):
            raise ValueError(ValidationMessages.NON_NUMERIC_COLUMN.format(column))

    # Apply normalization based on parameters
    if vmin != 0 or vmax != 1:
        # Custom range normalization
        for column in value_scaled.columns:
            value_scaled[column] = (value_scaled[column] - vmin) / (vmax - vmin)
    elif data_minmax is not None:
        # Use provided min/max values
        for column in value_scaled.columns:
            if column in data_minmax:
                col_min = data_minmax[column]["min"]
                col_max = data_minmax[column]["max"]
                if col_max > col_min:  # Avoid division by zero
                    value_scaled[column] = (value_scaled[column] - col_min) / (col_max - col_min)
                else:
                    value_scaled[column] = 0.5  # Set to middle value if all values are the same
    else:
        # Use column-wise min/max normalization
        for column in value_scaled.columns:
            col_min = value_scaled[column].min()
            col_max = value_scaled[column].max()
            if col_max > col_min:  # Avoid division by zero
                value_scaled[column] = (value_scaled[column] - col_min) / (col_max - col_min)
            else:
                value_scaled[column] = 0.5  # Set to middle value if all values are the same

    # Combine category and normalized values
    return pd.concat([data_scaled, value_scaled], axis=1)


def get_minmax(data: pd.DataFrame, columns: List[str]) -> Dict[str, Dict[str, float]]:
    """Get minimum and maximum values for specified columns.

    Args:
        data (pd.DataFrame): Input data.
        columns (List[str]): Column names to compute min/max for.

    Returns:
        Dict[str, Dict[str, float]]: Dictionary mapping column names to min/max values.

    Raises:
        ValueError: If data is empty or columns are not found.
    """
    if data.empty:
        raise ValueError(ValidationMessages.DATA_EMPTY)

    # Validate columns exist
    missing_columns = [col for col in columns if col not in data.columns]
    if missing_columns:
        raise ValueError(ValidationMessages.COLUMN_MISSING.format(missing_columns))

    # Validate columns contain numeric data
    non_numeric_columns = [col for col in columns if not pd.api.types.is_numeric_dtype(data[col])]
    if non_numeric_columns:
        raise ValueError(ValidationMessages.NON_NUMERIC_COLUMN.format(non_numeric_columns))

    data_subset = data[columns]
    data_minmax = {}

    for column in data_subset.columns:
        data_minmax[column] = {"max": float(data_subset[column].max()), "min": float(data_subset[column].min())}

    return data_minmax


def validate_data_structure(data: pd.DataFrame, required_columns: List[str]) -> bool:
    """Validate that data contains required columns and structure.

    Args:
        data (pd.DataFrame): Data to validate.
        required_columns (List[str]): List of required column names.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if data.empty:
        return False

    if not isinstance(data, pd.DataFrame):
        return False

    return all(column in data.columns for column in required_columns)


def get_data_info(data: pd.DataFrame) -> Dict[str, any]:
    """Get comprehensive information about the data.

    Args:
        data (pd.DataFrame): Data to analyze.

    Returns:
        Dict[str, any]: Dictionary containing data information.
    """
    info = {
        "shape": data.shape,
        "columns": list(data.columns),
        "dtypes": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "numeric_columns": list(data.select_dtypes(include=[np.number]).columns),
        "categorical_columns": list(data.select_dtypes(include=["object", "category"]).columns),
    }

    # Add basic statistics for numeric columns
    if info["numeric_columns"]:
        info["numeric_stats"] = data[info["numeric_columns"]].describe().to_dict()

    return info

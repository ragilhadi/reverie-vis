"""Radar chart implementation for ReverieVis package."""

from math import pi
from typing import Any, Dict, List, Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import axes

from reverievis.core.base import Chart
from reverievis.core.constants import DefaultValues, ValidationMessages
from reverievis.core.exceptions import DataValidationError
from reverievis.utils.chart_utils import create_angles, draw_radar, legend_styling, put_title
from reverievis.utils.data_utils import create_data_structure, normalize_minmax


class RadarChart(Chart):
    """Radar chart visualization class.

    This class implements radar chart functionality, migrating from the
    original function-based approach to a clean, object-oriented design.
    It provides methods for creating, customizing, and managing radar charts.

    Attributes:
        category_column (str): Column name for categories.
        value_columns (List[str]): Column names for values.
        data_minmax (Optional[Dict]): Min/max values for normalization.
        scaled (Optional[tuple]): Custom scaling range (min, max).
        show_circle (bool): Whether to show circular grid lines.
        circle_count (int): Number of circular grid lines.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        category_column: str,
        value_columns: List[str],
        data_minmax: Optional[Dict] = None,
        scaled: Optional[tuple] = None,
        show_circle: bool = False,
        circle_count: int = DefaultValues.CIRCLE_COUNT,
        **kwargs: Union[str, int, float, bool, list, tuple],
    ):
        """Initialize the RadarChart.

        Args:
            data (pd.DataFrame): Input data for the radar chart.
            category_column (str): Column name containing categories.
            value_columns (List[str]): Column names containing values to plot.
            data_minmax (Optional[Dict]): Min/max values for normalization. Defaults to None.
            scaled (Optional[tuple]): Custom scaling range (min, max). Defaults to None.
            show_circle (bool): Whether to show circular grid lines. Defaults to False.
            circle_count (int): Number of circular grid lines. Defaults to 5.
            **kwargs: Additional configuration parameters.
        """
        self.data = data
        self.category_column = category_column
        self.value_columns = value_columns
        self.data_minmax = data_minmax
        self.scaled = scaled
        self.show_circle = show_circle
        self.circle_count = circle_count

        # Validate required columns exist in data
        self._validate_columns()

        # Process data for radar chart
        self.processed_data = self._process_data()

        # Call parent constructor
        super().__init__(data, **kwargs)

    def _validate_columns(self) -> None:
        """Validate that required columns exist in the data.

        Raises:
            DataValidationError: If required columns are missing.
        """
        missing_columns = []

        if self.category_column not in self.data.columns:
            missing_columns.append(self.category_column)

        for col in self.value_columns:
            if col not in self.data.columns:
                missing_columns.append(col)

        if missing_columns:
            raise DataValidationError(
                ValidationMessages.COLUMN_MISSING.format(missing_columns),
                f"Available columns: {list(self.data.columns)}",
            )

    def _process_data(self) -> Dict[str, np.ndarray]:
        """Process data for radar chart visualization.

        Returns:
            Dict[str, np.ndarray]: Processed data ready for plotting.
        """
        # Normalize data if needed
        if self.scaled is not None:
            data_norm = normalize_minmax(
                data=self.data,
                category=self.category_column,
                data_minmax=self.data_minmax,
                vmin=self.scaled[0],
                vmax=self.scaled[1],
            )
        elif self.data_minmax is not None:
            data_norm = normalize_minmax(data=self.data, category=self.category_column, data_minmax=self.data_minmax)
        else:
            data_norm = self.data

        # Create radar data structure
        return create_data_structure(data_norm, self.category_column, self.value_columns)

    def plot(self) -> axes.Axes:
        """Create the radar chart visualization.

        Returns:
            matplotlib.axes.Axes: The axes object containing the plot.
        """
        # Create figure and polar axes
        self.fig = plt.figure(figsize=self.config.figure_size)
        self.ax = plt.subplot(111, polar=True)

        # Configure polar axes
        self._setup_polar_axes()

        # Draw the radar chart
        self._draw_radar_chart()

        # Apply title if specified
        if self.config.title:
            self._apply_title()

        # Apply legend if enabled
        if self.config.show_legend:
            self._apply_legend()

        return self.ax

    def _setup_polar_axes(self) -> None:
        """Set up polar axes configuration."""
        if self.ax is None:
            return

        # Create angles for the radar chart
        angles = create_angles(len(self.value_columns))

        # Configure polar axes
        self.ax.set_theta_offset(pi / 2)
        self.ax.set_theta_direction(-1)
        self.ax.set_xticks(angles[:-1], self.value_columns)
        self.ax.set_rlabel_position(0)

        # Set y-axis limits and ticks
        ylim_max = self._get_ymax_limit()
        yticks, yticks_label = self._get_yticks(ylim_max)

        if not self.show_circle:
            yticks = []

        if self.config.show_label:
            self.ax.set_yticks(yticks, yticks_label, color="grey", size=7)
        else:
            self.ax.set_yticks(yticks, [], color="grey", size=7)

        self.ax.set_ylim(0, ylim_max)

    def _draw_radar_chart(self) -> None:
        """Draw the actual radar chart data."""
        if self.ax is None:
            return

        angles = create_angles(len(self.value_columns))

        # Use configuration colors or theme colors
        colors = self.config.colors if hasattr(self.config, "colors") else self.theme.colors.primary

        # Draw radar chart using utility function
        draw_radar(
            ax=self.ax,
            data_radar=self.processed_data,
            angles=angles,
            colors=colors,
            colors_alpha=self.config.colors_alpha,
            marker=self.config.marker,
            marker_size=self.config.marker_size,
        )

    def _get_ymax_limit(self) -> float:
        """Calculate the maximum y-axis limit.

        Returns:
            float: Maximum y-axis value.
        """
        ymax = 0

        for key in self.processed_data:
            temp = self.processed_data[key].max()
            ymax = max(ymax, temp)

        # Ensure minimum ymax of 1
        return max(ymax, DefaultValues.MIN_YMAX)

    def _get_yticks(self, ylim_max: float) -> tuple:
        """Generate y-axis tick positions and labels.

        Args:
            ylim_max (float): Maximum y-axis value.

        Returns:
            tuple: (tick_positions, tick_labels)
        """
        yticks_label = np.linspace(0, ylim_max, self.circle_count).astype(int)
        yticks_label = yticks_label.astype(str)
        return np.linspace(0, ylim_max, self.circle_count), yticks_label

    def _apply_title(self) -> None:
        """Apply title to the chart."""
        if self.ax is not None and self.config.title:
            put_title(self.ax, self.config.title, self.config.title_position)

    def _apply_legend(self) -> None:
        """Apply legend to the chart."""
        if self.ax is not None:
            legend_styling(self.ax, self.config.legend_style, self.config.legend_col)

    def update_data(self, new_data: pd.DataFrame) -> None:
        """Update the chart data.

        Args:
            new_data (pd.DataFrame): New data for the chart.
        """
        self.data = new_data
        self._validate_columns()
        self.processed_data = self._process_data()

    def get_data_summary(self) -> Dict[str, Any]:
        """Get a summary of the chart data.

        Returns:
            Dict[str, Any]: Summary information about the data.
        """
        return {
            "category_column": self.category_column,
            "value_columns": self.value_columns,
            "data_shape": self.data.shape,
            "categories": list(self.processed_data.keys()),
            "value_count": len(self.value_columns),
        }

    def __repr__(self) -> str:
        """String representation of the RadarChart.

        Returns:
            str: String representation.
        """
        return (
            f"RadarChart(categories={len(self.processed_data)}, "
            f"values={len(self.value_columns)}, "
            f"data_shape={self.data.shape})"
        )

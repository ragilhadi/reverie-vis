"""Chart utility functions for ReverieVis package."""

from math import pi
from typing import Dict, List, Optional, Tuple

import numpy as np
from matplotlib import axes

from reverievis.core.constants import ColorDefaults, DefaultValues, LegendStyles, ValidationMessages


def create_angles(length: int) -> List[float]:
    """Create angles for radar chart visualization.

    Args:
        length (int): Number of value columns.

    Returns:
        List[float]: List of angles in radians.

    Raises:
        ValueError: If length is less than 1.
    """
    if length < 1:
        raise ValueError(ValidationMessages.LENGTH_INVALID)

    angles = [n / float(length) * 2 * pi for n in range(length)]
    # Add first angle to close the polygon
    angles += angles[:1]

    return angles


def draw_radar(
    ax: axes.Axes,
    data_radar: Dict[str, np.ndarray],
    angles: List[float],
    colors: Optional[List[str]] = None,
    colors_alpha: float = 0.2,
    marker: Optional[str] = None,
    marker_size: int = 3,
) -> None:
    """Draw radar chart on the given axes.

    Args:
        ax (axes.Axes): Matplotlib axes to draw on.
        data_radar (Dict[str, np.ndarray]): Data to plot, mapping categories to values.
        angles (List[float]): Angles for the radar chart.
        colors (Optional[List[str]]): List of colors for different categories. Defaults to None.
        colors_alpha (float): Alpha transparency for filled areas. Defaults to 0.2.
        marker (Optional[str]): Marker style for data points. Defaults to None.
        marker_size (int): Size of markers. Defaults to 3.

    Raises:
        ValueError: If data_radar is empty or angles don't match data length.
    """
    if not data_radar:
        raise ValueError(ValidationMessages.DATA_RADAR_EMPTY)

    if len(angles) < 2:
        raise ValueError(ValidationMessages.MIN_ANGLES_REQUIRED)

    # Default color palette if none provided
    default_colors = ColorDefaults.PRIMARY_COLORS

    for count, (key, values) in enumerate(data_radar.items()):
        # Validate data length matches angles
        if len(values) != len(angles):
            raise ValueError(ValidationMessages.DATA_LENGTH_MISMATCH.format(len(values), len(angles)))

        # Get color for this category
        if colors is not None and count < len(colors):
            color = colors[count]
        else:
            color = default_colors[count % len(default_colors)]

        # Plot the line
        ax.plot(
            angles,
            values,
            linewidth=1,
            linestyle="solid",
            marker=marker,
            markersize=marker_size,
            color=color,
            label=str(key),
        )

        # Fill the area
        ax.fill(angles, values, color=color, alpha=colors_alpha)


def legend_styling(ax: axes.Axes, style: str = LegendStyles.BOTTOM, col: int = 2) -> None:
    """Apply styling to the chart legend.

    Args:
        ax (axes.Axes): Matplotlib axes containing the legend.
        style (str): Legend position style ('bottom' or 'top'). Defaults to 'bottom'.
        col (int): Number of columns in legend. Defaults to 2.

    Raises:
        ValueError: If style is not 'bottom' or 'top', or col is less than 1.
    """
    if style not in [LegendStyles.BOTTOM, LegendStyles.TOP]:
        raise ValueError(ValidationMessages.INVALID_LEGEND_STYLE)

    if col < 1:
        raise ValueError(ValidationMessages.COLUMN_COUNT_INVALID)

    if style == LegendStyles.BOTTOM:
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.17), ncol=col, borderpad=1, frameon=False, fontsize=8)
    elif style == LegendStyles.TOP:
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.17), ncol=col, borderpad=1, frameon=False, fontsize=8)


def put_title(ax: axes.Axes, title: str, y: float = DefaultValues.Y_POSITION) -> None:
    """Add title to the chart.

    Args:
        ax (axes.Axes): Matplotlib axes to add title to.
        title (str): Title text.
        y (float): Vertical position of title. Defaults to 1.08.

    Raises:
        ValueError: If title is empty or y position is invalid.
    """
    if not title or not title.strip():
        raise ValueError(ValidationMessages.TITLE_EMPTY)

    if not isinstance(y, (int, float)):
        raise ValueError(ValidationMessages.Y_POSITION_INVALID)

    ax.set_title(title, y=y, fontsize=12, fontweight="bold", color="black")


def get_ymax_lim(data: Dict[str, np.ndarray]) -> float:
    """Calculate maximum y-axis limit for radar chart.

    Args:
        data (Dict[str, np.ndarray]): Data dictionary mapping categories to values.

    Returns:
        float: Maximum y-axis value.

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError(ValidationMessages.DATA_EMPTY)

    ymax = 0
    for _key, values in data.items():
        if len(values) > 0:
            temp = np.max(values)
            ymax = max(ymax, temp)

    # Ensure minimum ymax of 1
    return max(ymax, DefaultValues.MIN_YMAX)


def get_yticks(ylim_max: float, circle: int) -> Tuple[np.ndarray, np.ndarray]:
    """Generate y-axis tick positions and labels.

    Args:
        ylim_max (float): Maximum y-axis value.
        circle (int): Number of circular grid lines.

    Returns:
        Tuple[np.ndarray, np.ndarray]: (tick_positions, tick_labels)

    Raises:
        ValueError: If ylim_max is less than 0 or circle is less than 1.
    """
    if ylim_max < 0:
        raise ValueError(ValidationMessages.YLIM_MAX_INVALID)

    if circle < 1:
        raise ValueError(ValidationMessages.CIRCLE_COUNT_INVALID)

    yticks_label = np.linspace(0, ylim_max, circle).astype(int)
    yticks_label = yticks_label.astype(str)

    return np.linspace(0, ylim_max, circle), yticks_label


def apply_theme_to_axes(ax: axes.Axes, theme_colors: Dict[str, str]) -> None:
    """Apply theme colors to chart axes.

    Args:
        ax (axes.Axes): Matplotlib axes to style.
        theme_colors (Dict[str, str]): Dictionary of color settings.
    """
    if "background" in theme_colors:
        ax.set_facecolor(theme_colors["background"])

    if "grid" in theme_colors:
        ax.grid(True, color=theme_colors["grid"], alpha=0.3)

    if "text" in theme_colors:
        ax.tick_params(colors=theme_colors["text"])
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_color(theme_colors["text"])


def format_radar_axes(
    ax: axes.Axes, angles: List[float], labels: List[str], show_grid: bool = True, grid_alpha: float = 0.3
) -> None:
    """Format radar chart axes with proper styling.

    Args:
        ax (axes.Axes): Matplotlib axes to format.
        angles (List[float]): Angles for the radar chart.
        labels (List[str]): Labels for each angle.
        show_grid (bool): Whether to show grid lines. Defaults to True.
        grid_alpha (float): Alpha transparency for grid lines. Defaults to 0.3.
    """
    # Set angle ticks and labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Configure grid
    if show_grid:
        ax.grid(True, alpha=grid_alpha)

    # Set y-axis label position
    ax.set_rlabel_position(0)

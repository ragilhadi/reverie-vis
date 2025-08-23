"""Configuration management for ReverieVis charts."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from reverievis.core.constants import (
    ColorDefaults,
    ConfigKeys,
    DefaultValues,
    LegendStyles,
    ValidationMessages,
)


@dataclass
class ChartConfig:
    """Centralized configuration for chart styling and behavior.

    This class provides a clean interface for configuring chart appearance,
    behavior, and styling options. It uses dataclasses for type safety
    and easy serialization.

    Attributes:
        figure_size (tuple): Figure size as (width, height) in inches.
        colors (List[str]): List of colors for chart elements.
        colors_alpha (float): Alpha transparency for filled areas.
        show_legend (bool): Whether to display the legend.
        legend_style (str): Legend position style ('bottom', 'top').
        legend_col (int): Number of columns in legend.
        title (Optional[str]): Chart title.
        title_position (float): Title vertical position.
        marker (Optional[str]): Marker style for data points.
        marker_size (int): Size of markers.
        show_label (bool): Whether to show axis labels.
        line_width (float): Width of lines in charts.
        font_size (int): Base font size for text elements.
        background_color (str): Background color of the chart.
        grid_alpha (float): Alpha transparency for grid lines.
    """

    # Figure and layout
    figure_size: tuple = DefaultValues.FIGURE_SIZE
    background_color: str = ColorDefaults.BACKGROUND

    # Colors and styling
    colors: List[str] = field(default_factory=lambda: ColorDefaults.PRIMARY_COLORS)
    colors_alpha: float = DefaultValues.COLORS_ALPHA
    line_width: float = DefaultValues.LINE_WIDTH

    # Legend settings
    show_legend: bool = True
    legend_style: str = DefaultValues.LEGEND_STYLE
    legend_col: int = DefaultValues.LEGEND_COLUMNS

    # Title settings
    title: Optional[str] = None
    title_position: float = DefaultValues.TITLE_POSITION

    # Marker settings
    marker: Optional[str] = None
    marker_size: int = DefaultValues.MARKER_SIZE

    # Label settings
    show_label: bool = False

    # Font and text
    font_size: int = DefaultValues.FONT_SIZE
    font_weight: str = DefaultValues.FONT_WEIGHT

    # Grid and background
    grid_alpha: float = DefaultValues.GRID_ALPHA
    show_grid: bool = True

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        self._validate_config()

    def _validate_config(self) -> None:
        """Validate configuration parameters.

        Raises:
            ValueError: If configuration parameters are invalid.
        """
        if self.figure_size[0] <= 0 or self.figure_size[1] <= 0:
            raise ValueError(ValidationMessages.INVALID_FIGURE_SIZE)

        if not (0 <= self.colors_alpha <= 1):
            raise ValueError(ValidationMessages.INVALID_ALPHA)

        if self.legend_style not in [LegendStyles.BOTTOM, LegendStyles.TOP]:
            raise ValueError(ValidationMessages.INVALID_LEGEND_STYLE)

        if self.legend_col < 1:
            raise ValueError(ValidationMessages.INVALID_LEGEND_COLUMNS)

        if self.marker_size < 0:
            raise ValueError(ValidationMessages.INVALID_MARKER_SIZE)

        if self.line_width < 0:
            raise ValueError(ValidationMessages.INVALID_LINE_WIDTH)

        if self.font_size < 1:
            raise ValueError(ValidationMessages.INVALID_FONT_SIZE)

    def update(self, **kwargs: Union[str, int, float, bool, list, tuple]) -> None:
        """Update configuration with new values.

        Args:
            **kwargs: Configuration parameters to update.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(ValidationMessages.INVALID_CONFIG_PARAM.format(key))

        # Re-validate after update
        self._validate_config()

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of configuration.
        """
        return {
            ConfigKeys.FIGURE_SIZE: self.figure_size,
            ConfigKeys.BACKGROUND_COLOR: self.background_color,
            ConfigKeys.COLORS: self.colors,
            ConfigKeys.COLORS_ALPHA: self.colors_alpha,
            ConfigKeys.LINE_WIDTH: self.line_width,
            ConfigKeys.SHOW_LEGEND: self.show_legend,
            ConfigKeys.LEGEND_STYLE: self.legend_style,
            ConfigKeys.LEGEND_COL: self.legend_col,
            ConfigKeys.TITLE: self.title,
            ConfigKeys.TITLE_POSITION: self.title_position,
            ConfigKeys.MARKER: self.marker,
            ConfigKeys.MARKER_SIZE: self.marker_size,
            ConfigKeys.SHOW_LABEL: self.show_label,
            ConfigKeys.FONT_SIZE: self.font_size,
            ConfigKeys.FONT_WEIGHT: self.font_weight,
            ConfigKeys.GRID_ALPHA: self.grid_alpha,
            ConfigKeys.SHOW_GRID: self.show_grid,
        }

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "ChartConfig":
        """Create configuration from dictionary.

        Args:
            config_dict (Dict[str, Any]): Dictionary containing configuration.

        Returns:
            ChartConfig: New configuration instance.
        """
        return cls(**config_dict)

    def copy(self) -> "ChartConfig":
        """Create a copy of the configuration.

        Returns:
            ChartConfig: Copy of the configuration.
        """
        return ChartConfig(**self.to_dict())

    def __repr__(self) -> str:
        """String representation of the configuration.

        Returns:
            str: String representation.
        """
        return f"ChartConfig(figure_size={self.figure_size}, colors={len(self.colors)} colors)"

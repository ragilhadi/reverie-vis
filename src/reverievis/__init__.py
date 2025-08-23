"""ReverieVis - A package for creating beautiful visualizations easily.

This package provides a clean, object-oriented interface for creating various
types of charts and visualizations with consistent theming and configuration.

Authors:
    ragilhadi (ragilprasetyo310@gmail.com)

References:
    NONE
"""

# Import core classes for new API
# Import chart implementations
from reverievis.charts import RadarChart
from reverievis.core import Chart, ChartConfig, ConfigurationError, DataValidationError, ReverieVisError, Theme

# Import constants
from reverievis.core.constants import ChartTypes
from reverievis.core.factory import ChartFactory, create_chart, get_available_chart_types, register_chart

# Import utility functions
from reverievis.utils import (
    create_angles,
    create_data_structure,
    draw_radar,
    get_minmax,
    get_ymax_lim,
    get_yticks,
    legend_styling,
    normalize_minmax,
    put_title,
)

# Register available chart types with the factory
register_chart(ChartTypes.RADAR, RadarChart)

# Package version and metadata
__version__ = "1.0.0"
__author__ = "ragilhadi"
__email__ = "ragilprasetyo310@gmail.com"

# Main API exports
__all__ = [
    # Core classes
    "Chart",
    "ChartConfig",
    "Theme",
    "ReverieVisError",
    "DataValidationError",
    "ConfigurationError",
    # Factory functions
    "ChartFactory",
    "register_chart",
    "create_chart",
    "get_available_chart_types",
    # Chart implementations
    "RadarChart",
    # Utility functions
    "create_data_structure",
    "normalize_minmax",
    "get_minmax",
    "create_angles",
    "draw_radar",
    "legend_styling",
    "put_title",
    "get_ymax_lim",
    "get_yticks",
]

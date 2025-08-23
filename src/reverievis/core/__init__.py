"""Core module for ReverieVis package containing base classes and configuration."""

from reverievis.core.base import Chart
from reverievis.core.config import ChartConfig
from reverievis.core.constants import (
    ChartTypes,
    ColorConfigKeys,
    ColorDefaults,
    ColorPalettes,
    ConfigKeys,
    DefaultValues,
    ErrorTypes,
    FileExtensions,
    FontWeights,
    LegendStyles,
    Markers,
    StyleConfigKeys,
    StyleDefaults,
    ThemeConfigKeys,
    ThemeNames,
    TypographyConfigKeys,
    TypographyDefaults,
    ValidationMessages,
)
from reverievis.core.exceptions import ConfigurationError, DataValidationError, ReverieVisError
from reverievis.core.themes import Theme

__all__ = [
    "Chart",
    "ChartConfig",
    "ReverieVisError",
    "DataValidationError",
    "ConfigurationError",
    "Theme",
    # Constants
    "ChartTypes",
    "LegendStyles",
    "Markers",
    "FontWeights",
    "ThemeNames",
    "ColorPalettes",
    "ValidationMessages",
    "DefaultValues",
    "ColorDefaults",
    "TypographyDefaults",
    "StyleDefaults",
    "ErrorTypes",
    "FileExtensions",
    "ConfigKeys",
    "ThemeConfigKeys",
    "ColorConfigKeys",
    "TypographyConfigKeys",
    "StyleConfigKeys",
]

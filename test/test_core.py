"""Tests for core functionality of ReverieVis package."""

import pandas as pd
import pytest

from reverievis.charts import RadarChart
from reverievis.core import ChartConfig, DataValidationError, ReverieVisError, Theme
from reverievis.core.constants import DefaultValues, ThemeNames


class TestChartConfig:
    """Test ChartConfig class functionality."""

    def test_default_config(self) -> None:
        """Test default configuration creation."""
        config = ChartConfig()
        assert config.figure_size == DefaultValues.FIGURE_SIZE
        assert config.colors_alpha == DefaultValues.COLORS_ALPHA
        assert config.show_legend is True

    def test_custom_config(self) -> None:
        """Test custom configuration creation."""
        config = ChartConfig(figure_size=(10, 8), title="Test Chart", colors_alpha=0.5)
        assert config.figure_size == (10, 8)
        assert config.title == "Test Chart"
        assert config.colors_alpha == 0.5

    def test_config_validation(self) -> None:
        """Test configuration validation."""
        with pytest.raises(ValueError, match="Figure dimensions must be positive"):
            ChartConfig(figure_size=(-1, 5))

        with pytest.raises(ValueError, match="Colors alpha must be between 0 and 1"):
            ChartConfig(colors_alpha=1.5)

    def test_config_update(self) -> None:
        """Test configuration update functionality."""
        config = ChartConfig()
        config.update(title="Updated Title", colors_alpha=0.8)
        assert config.title == "Updated Title"
        assert config.colors_alpha == 0.8


class TestTheme:
    """Test Theme class functionality."""

    def test_default_theme(self) -> None:
        """Test default theme creation."""
        theme = Theme()
        assert theme.name == ThemeNames.DEFAULT
        assert len(theme.colors.primary) == 4
        assert theme.colors.background == "white"

    def test_dark_theme(self) -> None:
        """Test dark theme creation."""
        theme = Theme(ThemeNames.DARK)
        assert theme.name == ThemeNames.DARK
        assert theme.colors.background == "#2C3E50"
        assert theme.colors.text == "#ECF0F1"

    def test_theme_color_access(self) -> None:
        """Test theme color access functionality."""
        theme = Theme()
        color = theme.get_color(0, "primary")
        assert color in theme.colors.primary

        with pytest.raises(ValueError, match="Invalid palette: invalid_palette"):
            theme.get_color(0, "invalid_palette")

    def test_theme_update(self) -> None:
        """Test theme update functionality."""
        theme = Theme()
        theme.update_colors(background="#FF0000")
        assert theme.colors.background == "#FF0000"


class TestRadarChart:
    """Test RadarChart class functionality."""

    def test_radar_chart_creation(self) -> None:
        """Test radar chart creation with valid data."""
        # Create sample data
        data = pd.DataFrame({"Category": ["A", "B"], "Value1": [10, 20], "Value2": [15, 25]})

        chart = RadarChart(data=data, category_column="Category", value_columns=["Value1", "Value2"])

        assert chart.category_column == "Category"
        assert chart.value_columns == ["Value1", "Value2"]
        assert len(chart.processed_data) == 2

    def test_radar_chart_validation(self) -> None:
        """Test data validation in radar chart."""
        # Test with empty data
        with pytest.raises(DataValidationError, match="Missing required columns"):
            RadarChart(data=pd.DataFrame(), category_column="Category", value_columns=["Value1"])

        # Test with missing columns
        data = pd.DataFrame({"Category": ["A"], "Value1": [10]})
        with pytest.raises(DataValidationError, match="Missing required columns"):
            RadarChart(data=data, category_column="Category", value_columns=["Value1", "MissingColumn"])

    def test_radar_chart_data_processing(self) -> None:
        """Test data processing functionality."""
        data = pd.DataFrame({"Category": ["A", "B"], "Value1": [10, 20], "Value2": [15, 25]})

        chart = RadarChart(data=data, category_column="Category", value_columns=["Value1", "Value2"])

        # Test data summary
        summary = chart.get_data_summary()
        assert summary["category_column"] == "Category"
        assert summary["value_columns"] == ["Value1", "Value2"]
        assert summary["data_shape"] == (2, 3)


def test_exception_inheritance() -> None:
    """Test that custom exceptions inherit from base exception."""
    assert issubclass(DataValidationError, ReverieVisError)
    assert issubclass(DataValidationError, Exception)

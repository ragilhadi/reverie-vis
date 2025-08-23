"""Factory pattern for creating different chart types in ReverieVis."""

from typing import Dict, Optional, Type, Union

import pandas as pd

from reverievis.core.base import Chart
from reverievis.core.exceptions import ChartTypeError


class ChartFactory:
    """Factory for creating different chart types.

    This class provides a centralized way to create chart instances
    based on chart type strings. It maintains a registry of available
    chart types and their corresponding classes.

    Attributes:
        _chart_registry (Dict[str, Type[Chart]]): Registry of chart types.
    """

    def __init__(self):
        """Initialize the chart factory."""
        self._chart_registry: Dict[str, Type[Chart]] = {}

    def register(self, chart_type: str, chart_class: Type[Chart]) -> None:
        """Register a new chart type.

        Args:
            chart_type (str): String identifier for the chart type.
            chart_class (Type[Chart]): Chart class to register.
        """
        if not issubclass(chart_class, Chart):
            raise ValueError(f"Chart class must inherit from Chart: {chart_class}")

        self._chart_registry[chart_type.lower()] = chart_class

    def unregister(self, chart_type: str) -> None:
        """Unregister a chart type.

        Args:
            chart_type (str): String identifier for the chart type.
        """
        if chart_type.lower() in self._chart_registry:
            del self._chart_registry[chart_type.lower()]

    def get_available_types(self) -> list:
        """Get list of available chart types.

        Returns:
            list: List of available chart type strings.
        """
        return list(self._chart_registry.keys())

    def create(self, chart_type: str, data: pd.DataFrame, **kwargs: Union[str, int, float, bool, list, tuple]) -> Chart:
        """Create a chart instance based on type.

        Args:
            chart_type (str): Type of chart to create.
            data (pd.DataFrame): Input data for the chart.
            **kwargs: Additional arguments passed to chart constructor.

        Returns:
            Chart: New chart instance.

        Raises:
            ChartTypeError: If chart type is not supported.
        """
        chart_class = self._chart_registry.get(chart_type.lower())

        if chart_class is None:
            available_types = self.get_available_types()
            raise ChartTypeError(chart_type, available_types)

        try:
            return chart_class(data, **kwargs)
        except Exception as e:
            raise ChartTypeError(chart_type, details=f"Failed to create chart: {str(e)}") from e

    def is_supported(self, chart_type: str) -> bool:
        """Check if a chart type is supported.

        Args:
            chart_type (str): Chart type to check.

        Returns:
            bool: True if chart type is supported, False otherwise.
        """
        return chart_type.lower() in self._chart_registry

    def get_chart_class(self, chart_type: str) -> Optional[Type[Chart]]:
        """Get the chart class for a given type.

        Args:
            chart_type (str): Chart type to get class for.

        Returns:
            Optional[Type[Chart]]: Chart class if found, None otherwise.
        """
        return self._chart_registry.get(chart_type.lower())


# Global chart factory instance
chart_factory = ChartFactory()


def register_chart(chart_type: str, chart_class: Type[Chart]) -> None:
    """Register a chart type with the global factory.

    This is a convenience function for registering chart types
    with the global chart factory instance.

    Args:
        chart_type (str): String identifier for the chart type.
        chart_class (Type[Chart]): Chart class to register.
    """
    chart_factory.register(chart_type, chart_class)


def create_chart(chart_type: str, data: pd.DataFrame, **kwargs: Union[str, int, float, bool, list, tuple]) -> Chart:
    """Create a chart using the global factory.

    This is a convenience function for creating charts using
    the global chart factory instance.

    Args:
        chart_type (str): Type of chart to create.
        data (pd.DataFrame): Input data for the chart.
        **kwargs: Additional arguments passed to chart constructor.

    Returns:
        Chart: New chart instance.
    """
    return chart_factory.create(chart_type, data, **kwargs)


def get_available_chart_types() -> list:
    """Get list of available chart types from global factory.

    Returns:
        list: List of available chart type strings.
    """
    return chart_factory.get_available_types()

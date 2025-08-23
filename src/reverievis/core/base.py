"""Abstract base class for all chart types in ReverieVis."""

from abc import ABC, abstractmethod
from typing import Optional, Union

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import axes

from reverievis.core.config import ChartConfig
from reverievis.core.themes import Theme


class Chart(ABC):
    """Abstract base class for all chart types.

    This class provides a common interface for all chart implementations
    in ReverieVis. It handles data validation, configuration management,
    and provides common methods for chart operations.

    Attributes:
        data (pd.DataFrame): Input data for the chart.
        config (ChartConfig): Chart configuration settings.
        theme (Theme): Chart theme for styling.
        fig (Optional[plt.Figure]): Matplotlib figure object.
        ax (Optional[axes.Axes]): Matplotlib axes object.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        config: Optional["ChartConfig"] = None,
        theme: Optional["Theme"] = None,
        **kwargs: Union[str, int, float, bool, list, tuple],
    ):
        """Initialize the Chart with data and configuration.

        Args:
            data (pd.DataFrame): Input data for the chart.
            config (Optional[ChartConfig]): Chart configuration. Defaults to None.
            theme (Optional[Theme]): Chart theme. Defaults to None.
            **kwargs: Additional keyword arguments for configuration.
        """
        self.data = data
        self.config = config or ChartConfig(**kwargs)
        self.theme = theme or Theme()
        self.fig: Optional[plt.Figure] = None
        self.ax: Optional[axes.Axes] = None

        # Validate data
        self._validate_data()

        # Apply theme
        self.theme.apply(self)

    def _validate_data(self) -> None:
        """Validate input data.

        This method should be implemented by subclasses to validate
        data according to chart-specific requirements.
        """
        if self.data.empty:
            raise ValueError("Data cannot be empty")

    @abstractmethod
    def plot(self, **kwargs: Union[str, int, float, bool, list, tuple]) -> axes.Axes:
        """Create the visualization plot.

        This method must be implemented by subclasses to create
        the actual chart visualization.

        Args:
            **kwargs: Additional plotting parameters.

        Returns:
            matplotlib.axes.Axes: The axes object containing the plot.
        """
        pass

    def save(self, filename: str, **kwargs: Union[str, int, float, bool, list, tuple]) -> None:
        """Save the chart to a file.

        Args:
            filename (str): Output filename.
            **kwargs: Additional save parameters.
        """
        if self.fig is None:
            self.plot()

        if self.fig:
            self.fig.savefig(filename, **kwargs)

    def show(self) -> None:
        """Display the chart."""
        if self.fig is None:
            self.plot()

        if self.fig:
            plt.show()

    def get_figure(self) -> Optional[plt.Figure]:
        """Get the matplotlib figure object.

        Returns:
            Optional[plt.Figure]: The figure object if it exists.
        """
        return self.fig

    def get_axes(self) -> Optional[axes.Axes]:
        """Get the matplotlib axes object.

        Returns:
            Optional[axes.Axes]: The axes object if it exists.
        """
        return self.ax

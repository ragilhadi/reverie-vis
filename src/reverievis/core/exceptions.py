"""Custom exceptions for the ReverieVis package."""

from reverievis.core.constants import ErrorTypes


class ReverieVisError(Exception):
    """Base exception for all ReverieVis package errors.

    This is the base exception class that all other exceptions in the
    package inherit from. It provides a common interface for error
    handling and identification.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the exception with a message and optional details.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        self.message = message
        self.details = details
        super().__init__(self.message)

    def __str__(self) -> str:
        """String representation of the exception.

        Returns:
            str: Formatted error message with details if available.
        """
        if self.details:
            return f"{self.message} - Details: {self.details}"
        return self.message


class DataValidationError(ReverieVisError):
    """Raised when data validation fails.

    This exception is raised when the input data doesn't meet the
    requirements for a specific chart type or operation.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the data validation error.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        super().__init__(ErrorTypes.DATA_VALIDATION.format(message), details)


class ConfigurationError(ReverieVisError):
    """Raised when configuration is invalid or missing.

    This exception is raised when chart configuration parameters
    are invalid or when required configuration is missing.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the configuration error.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        super().__init__(ErrorTypes.CONFIGURATION.format(message), details)


class ChartTypeError(ReverieVisError):
    """Raised when an unsupported chart type is requested.

    This exception is raised when trying to create a chart type
    that is not supported by the package.
    """

    def __init__(self, chart_type: str, available_types: list = None):
        """Initialize the chart type error.

        Args:
            chart_type (str): The requested chart type.
            available_types (list, optional): List of available chart types. Defaults to None.
        """
        message = ErrorTypes.CHART_TYPE.format(chart_type)
        details = None

        if available_types:
            details = f"Available chart types: {', '.join(available_types)}"

        super().__init__(message, details)


class DataProcessingError(ReverieVisError):
    """Raised when data processing operations fail.

    This exception is raised when data transformation, normalization,
    or other processing operations encounter errors.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the data processing error.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        super().__init__(ErrorTypes.DATA_PROCESSING.format(message), details)


class PlottingError(ReverieVisError):
    """Raised when chart plotting operations fail.

    This exception is raised when matplotlib or other plotting
    operations encounter errors during chart creation.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the plotting error.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        super().__init__(ErrorTypes.PLOTTING.format(message), details)


class ThemeError(ReverieVisError):
    """Raised when theme operations fail.

    This exception is raised when theme loading, application,
    or customization operations encounter errors.
    """

    def __init__(self, message: str, details: str = None):
        """Initialize the theme error.

        Args:
            message (str): Primary error message.
            details (str, optional): Additional error details. Defaults to None.
        """
        super().__init__(ErrorTypes.THEME.format(message), details)

"""Constants for ReverieVis package to avoid hardcoded strings and typos."""


class ChartTypes:
    """Chart type constants."""

    RADAR = "radar"
    BAR = "bar"
    LINE = "line"
    SCATTER = "scatter"
    PIE = "pie"
    HISTOGRAM = "histogram"


class LegendStyles:
    """Legend style constants."""

    BOTTOM = "bottom"
    TOP = "top"
    LEFT = "left"
    RIGHT = "right"


class Markers:
    """Marker style constants."""

    CIRCLE = "o"
    SQUARE = "s"
    TRIANGLE = "^"
    DIAMOND = "D"
    STAR = "*"
    PLUS = "+"
    X_MARK = "x"
    NONE = None


class FontWeights:
    """Font weight constants."""

    NORMAL = "normal"
    BOLD = "bold"
    LIGHT = "light"
    HEAVY = "heavy"


class ThemeNames:
    """Theme name constants."""

    DEFAULT = "default"
    DARK = "dark"
    MINIMAL = "minimal"
    PROFESSIONAL = "professional"


class ColorPalettes:
    """Color palette constants."""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    ACCENT = "accent"


class ValidationMessages:
    """Validation error message constants."""

    DATA_EMPTY = "Data cannot be empty"
    DATA_NOT_DATAFRAME = "Data must be a pandas DataFrame"
    COLUMN_MISSING = "Missing required columns: {}"
    COLUMN_NOT_FOUND = "Column '{}' not found in data"
    NON_NUMERIC_COLUMN = "Column '{}' must contain numeric data"
    INVALID_FIGURE_SIZE = "Figure dimensions must be positive"
    INVALID_ALPHA = "Colors alpha must be between 0 and 1"
    INVALID_LEGEND_STYLE = "Legend style must be 'bottom' or 'top'"
    INVALID_LEGEND_COLUMNS = "Legend columns must be at least 1"
    INVALID_MARKER_SIZE = "Marker size must be non-negative"
    INVALID_LINE_WIDTH = "Line width must be non-negative"
    INVALID_FONT_SIZE = "Font size must be at least 1"
    INVALID_VMIN_VMAX = "vmin must be less than vmax"
    INVALID_PALETTE = "Invalid palette: {}"
    INVALID_THEME = "Unknown theme: {}"
    INVALID_CONFIG_PARAM = "Unknown configuration parameter: {}"
    INVALID_COLOR_PARAM = "Unknown color parameter: {}"
    INVALID_TYPOGRAPHY_PARAM = "Unknown typography parameter: {}"
    INVALID_STYLE_PARAM = "Unknown style parameter: {}"
    INVALID_CHART_TYPE = "Unsupported chart type: {}"
    DATA_LENGTH_MISMATCH = "Data length {} doesn't match angles length {}"
    MIN_ANGLES_REQUIRED = "At least 2 angles required"
    DATA_RADAR_EMPTY = "Data radar cannot be empty"
    TITLE_EMPTY = "Title cannot be empty"
    Y_POSITION_INVALID = "Y position must be a number"
    COLUMN_COUNT_INVALID = "Column count must be at least 1"
    LENGTH_INVALID = "Length must be at least 1"
    YLIM_MAX_INVALID = "ylim_max must be non-negative"
    CIRCLE_COUNT_INVALID = "Circle count must be at least 1"


class DefaultValues:
    """Default value constants."""

    FIGURE_SIZE = (16, 6)
    COLORS_ALPHA = 0.2
    LINE_WIDTH = 1.0
    LEGEND_STYLE = LegendStyles.BOTTOM
    LEGEND_COLUMNS = 2
    TITLE_POSITION = 1.08
    MARKER_SIZE = 3
    FONT_SIZE = 12
    FONT_WEIGHT = FontWeights.BOLD
    GRID_ALPHA = 0.3
    CIRCLE_COUNT = 5
    MIN_YMAX = 1.0
    Y_POSITION = 1.08


class ColorDefaults:
    """Default color constants."""

    PRIMARY_COLORS = ["#FF6D60", "#6DA9E4", "#F1C40F", "#9B59B6"]
    SECONDARY_COLORS = ["#A8E6CF", "#FFD3B6", "#FFAAA5", "#DCEDC8"]
    ACCENT_COLORS = ["#FF8B94", "#FFC3A0", "#FFEAA7", "#DDA0DD"]
    BACKGROUND = "white"
    TEXT = "#2C3E50"
    GRID = "#BDC3C7"
    DARK_BACKGROUND = "#2C3E50"
    DARK_TEXT = "#ECF0F1"
    DARK_GRID = "#34495E"
    DARK_PRIMARY = ["#E74C3C", "#3498DB", "#F1C40F", "#9B59B6"]
    DARK_SECONDARY = ["#2ECC71", "#E67E22", "#1ABC9C", "#F39C12"]
    MINIMAL_PRIMARY = ["#000000", "#666666", "#999999", "#CCCCCC"]
    MINIMAL_SECONDARY = ["#F5F5F5", "#E0E0E0", "#D0D0D0", "#C0C0C0"]
    PROFESSIONAL_PRIMARY = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D"]
    PROFESSIONAL_SECONDARY = ["#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"]


class TypographyDefaults:
    """Default typography constants."""

    TITLE_FONT = "Arial"
    LABEL_FONT = "Arial"
    TITLE_SIZE = 14
    LABEL_SIZE = 10
    TITLE_WEIGHT = FontWeights.BOLD
    LABEL_WEIGHT = FontWeights.NORMAL
    PROFESSIONAL_FONT = "Times New Roman"


class StyleDefaults:
    """Default style constants."""

    LINE_WIDTH = 2.0
    MARKER_SIZE = 6
    COLORS_ALPHA = 0.2
    GRID_ALPHA = 0.3
    BORDER_WIDTH = 1.0
    MINIMAL_LINE_WIDTH = 1.0
    MINIMAL_MARKER_SIZE = 4
    MINIMAL_ALPHA = 0.1
    PROFESSIONAL_LINE_WIDTH = 2.5
    PROFESSIONAL_BORDER_WIDTH = 1.5


class ErrorTypes:
    """Error type constants for exception messages."""

    DATA_VALIDATION = "Data validation error: {}"
    CONFIGURATION = "Configuration error: {}"
    CHART_TYPE = "Unsupported chart type: {}"
    DATA_PROCESSING = "Data processing error: {}"
    PLOTTING = "Plotting error: {}"
    THEME = "Theme error: {}"


class FileExtensions:
    """File extension constants."""

    PNG = ".png"
    JPG = ".jpg"
    JPEG = ".jpeg"
    PDF = ".pdf"
    SVG = ".svg"
    EPS = ".eps"


class ConfigKeys:
    """Configuration dictionary keys."""

    FIGURE_SIZE = "figure_size"
    BACKGROUND_COLOR = "background_color"
    COLORS = "colors"
    COLORS_ALPHA = "colors_alpha"
    LINE_WIDTH = "line_width"
    SHOW_LEGEND = "show_legend"
    LEGEND_STYLE = "legend_style"
    LEGEND_COL = "legend_col"
    TITLE = "title"
    TITLE_POSITION = "title_position"
    MARKER = "marker"
    MARKER_SIZE = "marker_size"
    SHOW_LABEL = "show_label"
    FONT_SIZE = "font_size"
    FONT_WEIGHT = "font_weight"
    GRID_ALPHA = "grid_alpha"
    SHOW_GRID = "show_grid"


class ThemeConfigKeys:
    """Theme configuration keys."""

    NAME = "name"
    COLORS = "colors"
    TYPOGRAPHY = "typography"
    STYLE = "style"


class ColorConfigKeys:
    """Color configuration keys."""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    ACCENT = "accent"
    BACKGROUND = "background"
    TEXT = "text"
    GRID = "grid"


class TypographyConfigKeys:
    """Typography configuration keys."""

    TITLE_FONT = "title_font"
    LABEL_FONT = "label_font"
    TITLE_SIZE = "title_size"
    LABEL_SIZE = "label_size"
    TITLE_WEIGHT = "title_weight"
    LABEL_WEIGHT = "label_weight"


class StyleConfigKeys:
    """Style configuration keys."""

    LINE_WIDTH = "line_width"
    MARKER_SIZE = "marker_size"
    COLORS_ALPHA = "colors_alpha"
    GRID_ALPHA = "grid_alpha"
    BORDER_WIDTH = "border_width"
    SHOW_GRID = "show_grid"

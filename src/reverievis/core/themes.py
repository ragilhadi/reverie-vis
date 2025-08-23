"""Theme system for consistent styling across ReverieVis charts."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Union

from reverievis.core.constants import (
    ColorConfigKeys,
    ColorDefaults,
    StyleConfigKeys,
    StyleDefaults,
    ThemeConfigKeys,
    ThemeNames,
    TypographyConfigKeys,
    TypographyDefaults,
    ValidationMessages,
)

if TYPE_CHECKING:
    from reverievis.core.base import Chart


@dataclass
class ColorPalette:
    """Color palette for chart elements.

    Attributes:
        primary (List[str]): Primary colors for main chart elements.
        secondary (List[str]): Secondary colors for supporting elements.
        accent (List[str]): Accent colors for highlighting.
        background (str): Background color.
        text (str): Text color.
        grid (str): Grid line color.
    """

    primary: List[str] = field(default_factory=lambda: ColorDefaults.PRIMARY_COLORS)
    secondary: List[str] = field(default_factory=lambda: ColorDefaults.SECONDARY_COLORS)
    accent: List[str] = field(default_factory=lambda: ColorDefaults.ACCENT_COLORS)
    background: str = ColorDefaults.BACKGROUND
    text: str = ColorDefaults.TEXT
    grid: str = ColorDefaults.GRID


@dataclass
class Typography:
    """Typography settings for chart text elements.

    Attributes:
        title_font (str): Font family for titles.
        label_font (str): Font family for labels.
        title_size (int): Font size for titles.
        label_size (int): Font size for labels.
        title_weight (str): Font weight for titles.
        label_weight (str): Font weight for labels.
    """

    title_font: str = TypographyDefaults.TITLE_FONT
    label_font: str = TypographyDefaults.LABEL_FONT
    title_size: int = TypographyDefaults.TITLE_SIZE
    label_size: int = TypographyDefaults.LABEL_SIZE
    title_weight: str = TypographyDefaults.TITLE_WEIGHT
    label_weight: str = TypographyDefaults.LABEL_WEIGHT


@dataclass
class ChartStyle:
    """Styling settings for chart elements.

    Attributes:
        line_width (float): Width of lines.
        marker_size (int): Size of markers.
        colors_alpha (float): Alpha transparency for filled areas.
        grid_alpha (float): Alpha transparency for grid lines.
        border_width (float): Width of chart borders.
        show_grid (bool): Whether to show grid lines.
    """

    line_width: float = StyleDefaults.LINE_WIDTH
    marker_size: int = StyleDefaults.MARKER_SIZE
    colors_alpha: float = StyleDefaults.COLORS_ALPHA
    grid_alpha: float = StyleDefaults.GRID_ALPHA
    border_width: float = StyleDefaults.BORDER_WIDTH
    show_grid: bool = True


class Theme:
    """Theme system for consistent styling across charts.

    This class provides a comprehensive theming system that ensures
    consistent appearance across all chart types. It includes color
    palettes, typography, and styling options.

    Attributes:
        name (str): Theme name identifier.
        colors (ColorPalette): Color palette configuration.
        typography (Typography): Typography configuration.
        style (ChartStyle): Chart styling configuration.
    """

    def __init__(self, name: str = ThemeNames.DEFAULT):
        """Initialize the theme with a name.

        Args:
            name (str): Theme name. Defaults to "default".
        """
        self.name = name
        self.colors = ColorPalette()
        self.typography = Typography()
        self.style = ChartStyle()

        # Apply default theme based on name
        self._apply_default_theme()

    def _apply_default_theme(self) -> None:
        """Apply default theme settings based on theme name."""
        if self.name == ThemeNames.DEFAULT:
            # Default theme is already set by dataclass defaults
            pass
        elif self.name == ThemeNames.DARK:
            self._apply_dark_theme()
        elif self.name == ThemeNames.MINIMAL:
            self._apply_minimal_theme()
        elif self.name == ThemeNames.PROFESSIONAL:
            self._apply_professional_theme()
        else:
            # Unknown theme, keep defaults
            pass

    def _apply_dark_theme(self) -> None:
        """Apply dark theme settings."""
        self.colors.background = ColorDefaults.DARK_BACKGROUND
        self.colors.text = ColorDefaults.DARK_TEXT
        self.colors.grid = ColorDefaults.DARK_GRID
        self.colors.primary = ColorDefaults.DARK_PRIMARY
        self.colors.secondary = ColorDefaults.DARK_SECONDARY

    def _apply_minimal_theme(self) -> None:
        """Apply minimal theme settings."""
        self.colors.primary = ColorDefaults.MINIMAL_PRIMARY
        self.colors.secondary = ColorDefaults.MINIMAL_SECONDARY
        self.style.line_width = StyleDefaults.MINIMAL_LINE_WIDTH
        self.style.marker_size = StyleDefaults.MINIMAL_MARKER_SIZE
        self.style.colors_alpha = StyleDefaults.MINIMAL_ALPHA
        self.style.show_grid = False

    def _apply_professional_theme(self) -> None:
        """Apply professional theme settings."""
        self.colors.primary = ColorDefaults.PROFESSIONAL_PRIMARY
        self.colors.secondary = ColorDefaults.PROFESSIONAL_SECONDARY
        self.typography.title_font = TypographyDefaults.PROFESSIONAL_FONT
        self.typography.label_font = TypographyDefaults.PROFESSIONAL_FONT
        self.style.line_width = StyleDefaults.PROFESSIONAL_LINE_WIDTH
        self.style.border_width = StyleDefaults.PROFESSIONAL_BORDER_WIDTH

    def apply(self, chart: "Chart") -> None:
        """Apply theme to a chart object.

        Args:
            chart: Chart object to apply theme to.
        """
        # This method will be implemented to apply theme settings
        # to chart objects. For now, it's a placeholder for future
        # theme application logic.
        pass

    def get_color(self, index: int, palette: str = ColorConfigKeys.PRIMARY) -> str:
        """Get a color from the specified palette.

        Args:
            index (int): Color index in the palette.
            palette (str): Palette name ('primary', 'secondary', 'accent').

        Returns:
            str: Color hex code.

        Raises:
            ValueError: If palette name is invalid.
        """
        if palette == ColorConfigKeys.PRIMARY:
            colors = self.colors.primary
        elif palette == ColorConfigKeys.SECONDARY:
            colors = self.colors.secondary
        elif palette == ColorConfigKeys.ACCENT:
            colors = self.colors.accent
        else:
            raise ValueError(ValidationMessages.INVALID_PALETTE.format(palette))

        return colors[index % len(colors)]

    def update_colors(self, **kwargs: Union[str, int, float, bool, list, tuple]) -> None:
        """Update color palette settings.

        Args:
            **kwargs: Color palette parameters to update.
        """
        for key, value in kwargs.items():
            if hasattr(self.colors, key):
                setattr(self.colors, key, value)
            else:
                raise ValueError(ValidationMessages.INVALID_COLOR_PARAM.format(key))

    def update_typography(self, **kwargs: Union[str, int, float, bool, list, tuple]) -> None:
        """Update typography settings.

        Args:
            **kwargs: Typography parameters to update.
        """
        for key, value in kwargs.items():
            if hasattr(self.typography, key):
                setattr(self.typography, key, value)
            else:
                raise ValueError(ValidationMessages.INVALID_TYPOGRAPHY_PARAM.format(key))

    def update_style(self, **kwargs: Union[str, int, float, bool, list, tuple]) -> None:
        """Update chart style settings.

        Args:
            **kwargs: Style parameters to update.
        """
        for key, value in kwargs.items():
            if hasattr(self.style, key):
                setattr(self.style, key, value)
            else:
                raise ValueError(ValidationMessages.INVALID_STYLE_PARAM.format(key))

    def to_dict(self) -> Dict[str, Any]:
        """Convert theme to dictionary representation.

        Returns:
            Dict[str, Any]: Dictionary representation of theme.
        """
        return {
            ThemeConfigKeys.NAME: self.name,
            ThemeConfigKeys.COLORS: {
                ColorConfigKeys.PRIMARY: self.colors.primary,
                ColorConfigKeys.SECONDARY: self.colors.secondary,
                ColorConfigKeys.ACCENT: self.colors.accent,
                ColorConfigKeys.BACKGROUND: self.colors.background,
                ColorConfigKeys.TEXT: self.colors.text,
                ColorConfigKeys.GRID: self.colors.grid,
            },
            ThemeConfigKeys.TYPOGRAPHY: {
                TypographyConfigKeys.TITLE_FONT: self.typography.title_font,
                TypographyConfigKeys.LABEL_FONT: self.typography.label_font,
                TypographyConfigKeys.TITLE_SIZE: self.typography.title_size,
                TypographyConfigKeys.LABEL_SIZE: self.typography.label_size,
                TypographyConfigKeys.TITLE_WEIGHT: self.typography.title_weight,
                TypographyConfigKeys.LABEL_WEIGHT: self.typography.label_weight,
            },
            ThemeConfigKeys.STYLE: {
                StyleConfigKeys.LINE_WIDTH: self.style.line_width,
                StyleConfigKeys.MARKER_SIZE: self.style.marker_size,
                StyleConfigKeys.COLORS_ALPHA: self.style.colors_alpha,
                StyleConfigKeys.GRID_ALPHA: self.style.grid_alpha,
                StyleConfigKeys.BORDER_WIDTH: self.style.border_width,
                StyleConfigKeys.SHOW_GRID: self.style.show_grid,
            },
        }

    @classmethod
    def from_dict(cls, theme_dict: Dict[str, Any]) -> "Theme":
        """Create theme from dictionary representation.

        Args:
            theme_dict (Dict[str, Any]): Dictionary containing theme data.

        Returns:
            Theme: New theme instance.
        """
        theme = cls(theme_dict.get(ThemeConfigKeys.NAME, ThemeNames.DEFAULT))

        if ThemeConfigKeys.COLORS in theme_dict:
            theme.update_colors(**theme_dict[ThemeConfigKeys.COLORS])

        if ThemeConfigKeys.TYPOGRAPHY in theme_dict:
            theme.update_typography(**theme_dict[ThemeConfigKeys.TYPOGRAPHY])

        if ThemeConfigKeys.STYLE in theme_dict:
            theme.update_style(**theme_dict[ThemeConfigKeys.STYLE])

        return theme

    def copy(self) -> "Theme":
        """Create a copy of the theme.

        Returns:
            Theme: Copy of the theme.
        """
        return Theme.from_dict(self.to_dict())

    def __repr__(self) -> str:
        """String representation of the theme.

        Returns:
            str: String representation.
        """
        return f"Theme(name='{self.name}', colors={len(self.colors.primary)} primary colors)"

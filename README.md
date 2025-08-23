# ReverieVis

A professional Python package for creating beautiful visualizations with clean, object-oriented design.

## Features

- **Clean Architecture**: Object-oriented design with clear separation of concerns
- **Multiple Chart Types**: Support for radar charts, with more chart types coming soon
- **Professional Theming**: Built-in themes (default, dark, minimal, professional)
- **Type Safety**: Comprehensive constants system preventing typos and errors
- **Easy Configuration**: Centralized configuration management
- **Extensible**: Factory pattern for easy addition of new chart types

## Installation

```bash
pip install reverievis
```

## Quick Start

### Basic Radar Chart

```python
import pandas as pd
from reverievis import RadarChart

# Create sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Speed': [80, 90, 70],
    'Accuracy': [85, 75, 95],
    'Efficiency': [90, 80, 85]
})

# Create and display chart
chart = RadarChart(
    data=data,
    category_column='Category',
    value_columns=['Speed', 'Accuracy', 'Efficiency']
)
chart.plot()
chart.show()
```

### Customized Chart

```python
from reverievis import RadarChart, ChartConfig, Theme
from reverievis.core.constants import LegendStyles, Markers

# Custom configuration
config = ChartConfig(
    figure_size=(12, 8),
    title="Performance Comparison",
    colors=['#FF6D60', '#6DA9E4', '#F7D060'],
    legend_style=LegendStyles.TOP,
    marker=Markers.CIRCLE
)

# Custom theme
theme = Theme("professional")

# Create chart
chart = RadarChart(
    data=data,
    category_column='Category',
    value_columns=['Speed', 'Accuracy', 'Efficiency'],
    config=config,
    theme=theme
)
chart.plot()
chart.show()
```

### Using the Factory Pattern

```python
from reverievis import create_chart

# Create chart using factory
chart = create_chart(
    'radar',
    data=data,
    category_column='Category',
    value_columns=['Speed', 'Accuracy', 'Efficiency']
)
chart.plot()
chart.show()
```

## Architecture

The package follows a clean, modular architecture:

```
reverievis/
├── core/           # Base classes and configuration
├── charts/         # Chart implementations
├── utils/          # Utility functions
├── constants/      # Type-safe constants
└── factory/        # Chart creation factory
```

## Key Components

- **`Chart`**: Abstract base class for all chart types
- **`ChartConfig`**: Centralized configuration management
- **`Theme`**: Professional theming system
- **`ChartFactory`**: Factory pattern for chart creation
- **Constants**: Type-safe constants preventing errors

## Documentation

📚 **Complete Documentation**: Visit our [GitBook documentation](https://reverie-vis.gitbook.io/docs) for comprehensive guides, examples, and API reference.

## Development

### Setup Development Environment

```bash
git clone https://github.com/ragilhadi/reverie-vis.git
cd reverie-vis
pip install -r requirements-dev.txt
```

### Pre-commit Setup (Recommended)

Pre-commit hooks automatically check code quality before each commit:

```bash
# Install pre-commit
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Run against all files (optional)
pre-commit run --all-files
```

The pre-commit hooks will automatically:
- **Format code** with Ruff
- **Check code quality** with Ruff linting
- **Validate imports** and catch common issues
- **Ensure consistent code style** across the project

### Manual Code Quality Checks

```bash
# Run tests
pytest src/tests/

# Format code
black src/

# Lint code
flake8 src/

# Type checking
mypy src/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Before contributing, please:**
1. Set up pre-commit hooks (see Development section above)
2. Ensure all tests pass
3. Follow the existing code style

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- **ragilhadi** - *Initial work* - [ragilhadi](https://github.com/ragilhadi)

## Acknowledgments

- Built with [Matplotlib](https://matplotlib.org/)
- Data handling with [Pandas](https://pandas.pydata.org/)
- Numerical operations with [NumPy](https://numpy.org/)

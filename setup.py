"""Setup configuration for ReverieVis package."""

import re
from pathlib import Path

from setuptools import find_packages, setup

FILE = Path(__file__).resolve()
PARENT = FILE.parent

with open("README.md") as f:
    long_description = f.read()


def get_version() -> str:
    """Get the version of the package."""
    file = PARENT / "src/reverievis/__init__.py"
    results = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(encoding="utf-8"), re.M)
    if results:
        return results[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="reverievis",
    version=get_version(),
    author="ragilhadi",
    author_email="ragilprasetyo310@gmail.com",
    description="A professional package for creating beautiful visualizations with clean, object-oriented design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ragilhadi/reverie-vis",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

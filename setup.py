from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="reverievis",
    version="0.0.1",
    description="A package used to easily create some beutiful visualization",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ragilhadi/reverie-vis",
    author="ragilhadi",
    author_email="ragilprasetyo310@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy >= 1.21.5",
                      "matplotlib >= 3.5.2",
                      "pandas >= 1.4.4"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.9",
)
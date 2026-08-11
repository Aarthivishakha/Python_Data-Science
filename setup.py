from setuptools import find_packages, setup


setup(
    name="python-data-science-pipeline",
    version="1.0.0",
    description="CSV analysis and regression pipeline for Python 3.8",
    python_requires=">=3.8,<3.9",
    packages=find_packages(),
    test_suite="tests",
    entry_points={"console_scripts": ["data-science=datascience.cli:main"]},
)

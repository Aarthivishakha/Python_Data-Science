from setuptools import find_packages, setup


setup(
    name="python-data-science-pipeline",
    version="1.0.0",
    description="CSV analysis and regression pipeline for Python 3.5",
    python_requires=">=3.5,<3.6",
    packages=find_packages(),
    test_suite="tests",
    entry_points={"console_scripts": ["data-science=datascience.cli:main"]},
)

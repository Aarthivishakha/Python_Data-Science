from setuptools import find_packages, setup


setup(
    name="python-data-science-pipeline",
    version="1.0.0",
    description="Data Science and regression ML pipeline for Python 3.16",
    python_requires=">=3.16,<3.17",
    packages=find_packages(),
    test_suite="tests",
    entry_points={"console_scripts": ["data-science=datascience.cli:main"]},
)

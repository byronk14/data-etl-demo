from setuptools import find_packages, setup

setup(
    name="dagster_data_etl",
    packages=find_packages(exclude=["dagster_data_etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "requests",
        "duckdb",
        "pandas",
        "dagster-duckdb"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

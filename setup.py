from setuptools import setup, find_packages

setup(
    name="ws_idealista",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy",
        "beatifulsoup4",
        "lxml",
        "requests",
        "schedule"
    ]
)
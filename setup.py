# setup.py
from setuptools import find_packages, setup

setup(
    name="puerro",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "puerro = puerro.cli:main",
        ],
    },
)

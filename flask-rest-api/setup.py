from setuptools import find_packages, setup

setup(
    name="flask-rest-api",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)

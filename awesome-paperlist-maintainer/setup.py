from setuptools import setup, find_packages

setup(
    name="awesome-paperlist-maintainer", 
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    ],
    author="Yichen (Zach) Wang",
    description="An automated maintenance tool for curated academic paper collections.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
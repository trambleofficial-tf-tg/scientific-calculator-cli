"""Setup configuration for Scientific Calculator CLI"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scientific-calculator-cli",
    version="2.0.0",
    author="Scientific Calculator Team",
    description="A feature-rich command-line scientific calculator with enhanced UI/UX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trambleofficial-tf-tg/scientific-calculator-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "scalc=main:main",
        ],
    },
    keywords="calculator scientific mathematics cli terminal",
)

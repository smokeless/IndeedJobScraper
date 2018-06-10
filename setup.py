import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IndeedJobScraper",
    version="0.0.1",
    author="Ross R.",
    author_email="ross.russell@protonmail.com",
    description="An indeed job scraper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smokeless/IndeedJobScraper"
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

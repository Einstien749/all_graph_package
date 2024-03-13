from setuptools import setup, find_packages

Version = '0.0.1'
Description = "This Package deals with mathematical graphs "
Long_Description = "It helps mathematicians and researchers deal with problems partaining to Graph Theory"

setup(
    name = "all_graphs",
    version = Version,
    description = Description,
    long_description = Long_Description,
    author = "Odimayo Taiye Moses",
    packages = find_packages(),
    author_email = "odimayomoses@gmail.com",
    install_requires = [],

    keywords = ['python', 'graph theory', 'graphs'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
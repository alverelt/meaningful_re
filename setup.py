import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="meaningful_re",
    version="0.1.23",
    description="Regular expression builder with chainable methods.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aelt/meaningful_re",
    author="Alver Lopez",
    author_email="alverelt@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["meaningful_re"],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)

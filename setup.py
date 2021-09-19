from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from naughtty.version import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.io",
    classifiers=classifiers,
    description="Python package and CLI tool for executing shell commands in a pseudo-terminal",
    entry_points={
        "console_scripts": [
            "naughtty=naughtty.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="naughtty",
    packages=[
        "naughtty",
        "naughtty.version",
    ],
    package_data={
        "naughtty": ["py.typed"],
        "naughtty.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/naughtty",
    version=version,
)

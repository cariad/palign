from pathlib import Path

from setuptools import setup

from palign import version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Pillow text alignment helper",
    include_package_data=True,
    install_requires=[
        "nvalues==1.0.0b4",
        "pillow~=9.3",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="palign",
    packages=[
        "palign",
    ],
    package_data={
        "palign": ["py.typed"],
    },
    python_requires=">=3.9",
    url="https://github.com/cariad/palign",
    version=version,
)

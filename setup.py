from setuptools import setup

setup(
    name="maketxt",
    version="1.0.0",
    py_modules=["maketxt"],  # Looks for maketxt.py
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "maketxt=maketxt:main", # Command=Module:Function
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

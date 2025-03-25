from setuptools import setup

setup(
    name="screenreclib",  # The name of your package
    version="0.1",           # The version of your package
    py_modules=["screen"],   # List of modules in your package (screen.py in your case)
    install_requires=[],     # List any dependencies your package has here
    long_description=open("README.md").read(),  # Load content of README.md
    long_description_content_type="text/markdown",  # Specify the markdown format
    url="https://github.com/your-username/screen_recorder",  # Your project's URL (if on GitHub)
    classifiers=[           # Add some metadata about your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

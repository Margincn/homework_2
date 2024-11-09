from setuptools import setup, find_packages

setup(
    name="math_quiz",  
    version="0.1",
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[], # There are currently no external dependencies

    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",  # Entry point: package_name.module_name:function_name
        ],
    },

    author="Shujie Tang",
    author_email="tangsjcn@gmail.com", 
    description="A simple math quiz game.",
    long_description=open("README.md").read(),  # Read README.md as a detailed description of the project
    long_description_content_type="text/markdown", 
    url="https://github.com/Margincn/homework_2.git",
    license="Apache License 2.0",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',  # Python version requirement
)

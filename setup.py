from setuptools import setup, find_packages

# Long description with accurate technical usage based on source code
long_description = """
# Emilve: The Python Syntax Hacker 🚀

Emilve adapts Python to YOU, not the other way around. Created by Emiliano (emicicx).

1. Braces Support {}
Stop worrying about rigid indentation. Use curly braces just like in C# or Java! This module injects the code directly into the caller's frame.

Example:
from Emilve import Braces
with Braces('''
    def hello() {
        print("Hello from Emilve!")
    }
    hello()
'''):
    pass

2. Auto-Installation (AutoPip) 📦
Forget 'ModuleNotFoundError'. Emilve monitors exceptions; if a library is missing, it asks for permission, installs it, and restarts your script automatically.

Example:
import emilve  # Monitor activates automatically
import requests_that_i_do_not_have  # Emilve handles the installation prompt!

3. Case Insensitivity (Functions & Variables) 🔠
Did you write 'Print()' instead of 'print()' or 'MyVariable' instead of 'myvariable'? Emilve fixes typos in real-time by mapping locals and builtins.

Example:
from Emilve import CaseSensivity
var = 1
CaseSensivity("print(f"the var is {VaR}")")
#This work!

---
Note: This library is a tool for developers seeking extreme flexibility.
The respect for others' code is peace.
Contact: emicicsmaker@gmail.com
"""

setup(
    name="Emilve", 
    version="1.2.0", 
    author="Emiliano (emicicx)",
    author_email="emicicsmaker@gmail.com",
    description="Python syntax hacker: Braces, Case Sensitivity, and Auto-Installation.",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="braces, syntax, automation, case-insensitive, autopip, emilve",
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[ctypes], # Zero external dependencies.
)
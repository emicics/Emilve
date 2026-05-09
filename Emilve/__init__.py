# Emilve/__init__.py
"""
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

To use it, you must activate the context manager with Active=False:

Example:
from Emilve import CaseSensivity
with CaseSensivity(Active=False):
    MY_VARIABLE = "Magic"
    print(my_variable)  # It works!
    Print("It also works for functions!")
    
4. Semicolon allow you use ; in your code only importing it

---
Note: This library is a tool for developers seeking extreme flexibility.
The respect for others' code is peace.
Contact: emicicsmaker@gmail.com
"""
from .core import CaseSensivity
from .Braces import Braces
from . import AutoPip
from .Zen import display_zen
from .SemiColon import SemiColon
# Definimos Zen como una función, NO como una instancia de clase
def Zen():
    display_zen()
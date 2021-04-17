"""
Script that automates the process of writing a keybindings.md
By directly getting the keybindings from keybindings.py
"""

# Local import
from keybindings import Keybindings

def get_keybindings():
    current_keybindings = Keybindings()
    list_of_keys = list(current_keybindings.init_keys())
    return list_of_keys


print(*get_keybindings(), sep="\n")

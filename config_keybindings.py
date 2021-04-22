"""
MODIFY THIS FILE TO CREATE CUSTOM KEYBINDINGS

Keybindings are configured with tuples, inside Predifined lists Variables

Modifier -> list() -> Ex: [MOD, CONTROL]

Key -> str() -> Ex: 'j'

Command -> str() -> Ex: vscode

(Modifier, Key, Command)
"""

from libqtile.confreader import ConfigError

# Import default mod keys
from keys.default import *


# Define constants here
TERMINAL = "termite"


# Basic window manager movements

# ------------ Hardware Configs ------------
HARDWARE_KEYS = [
    # (Modifier, Key, Command)

    # Volume
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # Brightness
    ([], "XF86MonBrightnessUp", "brightnessctl set +10%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 10%-"),
]


APPS = [
    
]

##########################
# Your custom keys here  #
##########################

CUSTOM_SPAWN_KEYS = [
    
]

SPAWN_KEYS = HARDWARE_KEYS + APPS + CUSTOM_SPAWN_KEYS 

SPAWN_CMD_KEYS = [
    
]
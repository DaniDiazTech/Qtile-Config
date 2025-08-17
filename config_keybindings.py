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

from functions import PWA

from os.path import expanduser

HOME = expanduser("~")

# Define constants here
TERMINAL = "alacritty"


# Basic window manager movements


# Qtile shutdown/restart keys
SHUTDOWN_MODIFIER = [MOD, CONTROL]
RESTART           = "r"
SHUTDOWN          = "q"


# Group movement keys:
GROUPS_KEY     = CONTROL
SWAP_GROUP_KEY = SHIFT

NEXT_GROUP = "period"
PREV_GROUP = "comma"


# ------------ Hardware Configs ------------
HARDWARE_KEYS = [
    # (Modifier, Key, Command)

    # Volume
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # Brightness
    ([], "XF86MonBrightnessUp", "brightnessctl set +5%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 5%-"),
]


APPS = [
    ([MOD], "Return", TERMINAL),
    # (Modifier, Key, Command)
    ([MOD],      "e", "thunar"),
    ([MOD, ALT], "d", "emacs"),
    ([MOD, ALT], "o", "env LIBGL_ALWAYS_SOFTWARE=1 obs"),
    ([MOD, ALT], "v", "gvim"),
    ([MOD, ALT], "b", "brave"),
    ([MOD, ALT], "c", "code"),
    ([MOD, ALT], "p", "pycharm"),
    ([MOD, ALT], "a", "pavucontrol"),
    ([MOD, ALT], "e", "vim -g .config/qtile/config.py"),
    ([MOD, ALT], "z", "zoom"),

    # Media hotkeys
    ([MOD],      "Up", "pulseaudio-ctl up 5"),
    ([MOD],      "Down", "pulseaudio-ctl down 5"),
    
    # Makes reference to play-pause script
    # You can find it in my scripts repository
    ([ALTGR],    "space", "play-pause"),
   
    # Run "rofi-theme-selector" in terminal to select a theme
    ([MOD], "space", 'rofi -modi "drun,power-menu:rofi-power-menu,run,window,ssh" -show drun -show-icons'),
    
    # Screenshots
    ([],         "Print", "xfce4-screenshooter"),
    # Full screen screenshot
    ([ALT],      "Print", "xfce4-screenshooter -f -c"),

    # Terminal apps
    ([MOD, ALT], "n", TERMINAL + " -e nvim"),
    
]

##########################
# Your custom keys here  #
##########################

CUSTOM_SPAWN_KEYS = [
    # PWA keys
    ([MOD, ALT], "s", PWA.spotify()),
    ([MOD, ALT], "m", PWA.music()),
    ([MOD, ALT], "t", PWA.calendar()),
    ([MOD, ALT], "y", PWA.youtube()),
    ([MOD, ALT], "h", PWA.habitica()),

    # Security
    ([MOD, ALT], "l", "xflock4"),
]


SPAWN_KEYS = HARDWARE_KEYS + APPS + CUSTOM_SPAWN_KEYS 

SPAWN_CMD_KEYS = [
    # Takes full screenshot and creates a file on the screenshot folder
    ([SHIFT],    "Print", f"xfce4-screenshooter -f -s {HOME}/Pictures/Screenshots/"),
]

"""Qtile default keybindings"""

# Keys
MOD = "mod4"
ALT = "mod1"
ALTGR = "mod5"
SHIFT = "shift"
CONTROL = "control"

# Basic wm bindings

# All of these variables include the MOVEMENT_KEYS at the start

# The key which the WM will use to move the layouts
MOVEMENT_KEY   = MOD
KILL_KEY       = MOD

SWAP_KEY       = SHIFT
FLOATING_KEY   = SHIFT
GROUPS_KEY     = CONTROL
SWAP_GROUP_KEY = SHIFT


############   BINDINGS FOR MONADTALL   ##############
# Move between windows
LEFT   = "h"
RIGHT  = "l"
DOWN   = "j"
UP     = "k"

# Swap windows 
SWAP_LEFT  = "h"
SWAP_RIGHT = "l"
SWAP_DOWN  = "j"
SWAP_UP    = "k"

SWAP_FLIP  = "space" # Flip the layout

###########         LAYOUTS               ###############
# Change windows lenght
GROW       = "i"
SHRINK     = "m"
NORMALIZE  = "n"
MAXIMIZE   = "o"

# Floating layout
TOOGLE_FLOATING = "f"
TOOGLE_FULL     = "g"

# Groups key
# Move screen to next and previous group
NEXT     = "k"
PREVIOUS = "j"

# Kill Functions
KILL_CURRENT           = "w"
KILL_ALL               = "x"
KILL_ALL_MINUS_CURRENT = "c"

# Rotates layouts

TOOGLE_LAYOUT = "Tab"
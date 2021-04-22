
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Import the function that move the window to the next and prev group
from functions import Functions, PWA

from config_keybindings import *


class Keybindings:
    def __init__(self):
        self.mod = MOD
        self.alt = ALT
        self.altgr = ALTGR
        self.terminal = TERMINAL
        self.shift = SHIFT
        self.control = CONTROL

        # All keys are stored keys
        self.keys = []

    def init_keys(self):

        #################### CUSTOM KEYS  ##########################
        return [
            ############   BINDINGS FOR MONADTALL   ##############
            Key([self.mod], "h", lazy.layout.left()),
            Key([self.mod], "l", lazy.layout.right()),
            Key([self.mod], "j", lazy.layout.down()),
            Key([self.mod], "k", lazy.layout.up()),
            Key([self.mod, "shift"], "h", lazy.layout.swap_left()),
            Key([self.mod, "shift"], "l", lazy.layout.swap_right()),
            Key([self.mod, "shift"], "j", lazy.layout.shuffle_down()),
            Key([self.mod, "shift"], "k", lazy.layout.shuffle_up()),
            Key([self.mod], "i", lazy.layout.grow()),
            Key([self.mod], "m", lazy.layout.shrink()),
            Key([self.mod], "n", lazy.layout.normalize()),
            Key([self.mod], "o", lazy.layout.maximize()),
            Key([self.mod, "shift"], "space", lazy.layout.flip()),

            ############   BINDINGS FOR FLOATING   ##############
            Key([self.mod, "shift"], "f", lazy.window.toggle_floating(),
                desc='toggle floating'),
            Key([self.mod, "shift"], "g", lazy.window.toggle_fullscreen(),
                desc='toggle fullscreen'),

            # Move screen to next and previous workspace
            Key([self.control], "k", lazy.screen.next_group(),
                desc="Move screen to the next workspace"),
            Key([self.control], "j", lazy.screen.prev_group(),
                desc="Move screen to the previous workspace"),

            # Move window to next group
            Key([self.control, self.shift], "k", Functions.window_to_next_group(),
                desc="Move screen to the next workspace"),
            Key([self.control, self.shift], "j", Functions.window_to_prev_group(),
                desc="Move screen to the previous workspace"),
            # Kill Functions
            Key([self.mod, self.altgr], "c", Functions.kill_all_windows_minus_current(),
                desc="Kill all windows except current in the workspace"),
            Key([self.mod, self.altgr], "x", Functions.kill_all_windows(),
                desc="Kill all windows except current in the workspace"),

            # Toggle between different layouts as defined below
            Key([self.mod], "Tab", lazy.next_layout(),
                desc="Toggle between layouts"),


            # Basic Commands
            Key([self.mod], "w", lazy.window.kill(),
                desc="Kill focused window"),
            Key([self.mod], "Return", lazy.spawn(
                self.terminal), desc="Launch terminal"),
            Key([self.mod, "control"], "r",
                lazy.restart(), desc="Restart qtile"),
            Key([self.mod, "control"], "q",
                lazy.shutdown(), desc="Shutdown qtile"),
            Key([self.mod], "space", lazy.spawn('rofi -modi "drun,run,window,ssh" -show drun'),
                desc="Run Rofi"),

            # THESE ARE MY PREFERED APPS YOU CAN SWITCH KEYBINDINGS JUST
            # BY TYPING THE PATH TO YOUR APPS #####
            # Applications hotkeys
            Key([self.mod], "e", lazy.spawn("thunar"), desc="Open Thunar"),
            # Most apps are opened with Super + left self.alt keys
            Key([self.mod, self.alt], "d", lazy.spawn(
                "emacs"), desc="Open Doom Emacs"),
            Key([self.mod, self.alt], "o", lazy.spawn(
                "env LIBGL_ALWAYS_SOFTWARE=1 obs"), desc="Open Obs Studio"),
            Key([self.mod, self.alt], "v", lazy.spawn(
                "gvim"), desc="Open Gvim"),
            Key([self.mod, self.alt], "n", lazy.spawn(
                self.terminal + " -e nvim"), desc="Open Neovim"),
            Key([self.mod, self.alt], "f", lazy.spawn(self.terminal + \
                                                      " -e ./.config/vifm/scripts/vifmrun"), desc="Open vifm"),
            Key([self.mod, self.alt], "b", lazy.spawn(
                "brave"), desc="Open Brave"),
            Key([self.mod, self.alt], "c", lazy.spawn(
                "codium"), desc="Open VS codium"),
            Key([self.mod, self.alt], "p", lazy.spawn(
                "pycharm"), desc="Open Pycharm CE"),
            Key([self.mod, self.alt], "a", lazy.spawn("pavucontrol"),
                desc="Open Pulse audio GUI controller"),
            Key([self.mod, self.alt], "e", lazy.spawn("vim -g .config/qtile/config.py"),
                desc="Open Qtile config file in gvim"),
            Key([self.mod, self.alt], "r", lazy.spawn("vim -g .vimrc"),
                desc="Open Qtile config file in gvim"),


            # PWA hotkeys

            Key([self.mod, self.alt], "s",
                lazy.spawn(PWA.spotify()),
                desc="Open Spotify PWA"),  # In others system the PWA id will be different

            Key([self.mod, self.alt], "m",
                lazy.spawn(PWA.music()),
                desc="Open Youtube Music PWA"),
            Key([self.mod, self.alt], "t",
                lazy.spawn(PWA.calendar()),
                desc="Open Calendar PWA"),

            # My own created PWA's
            Key([self.mod, self.alt], "y",
                lazy.spawn(PWA.youtube()),
                desc="Open Youtube PWA"),
            Key([self.mod, self.alt], "l",
                lazy.spawn(PWA.notion()),
                desc="Open my custom Notion PWA"),
            Key([self.mod, self.alt], "h",
                lazy.spawn(PWA.habitica()),
                desc="Open my custom Habitica PWA"),


            # Media hotkeys
            Key([self.mod], 'Up', lazy.spawn('pulseaudio-ctl up 5')),
            Key([self.mod], 'Down', lazy.spawn('pulseaudio-ctl down 5')),
            Key([self.altgr], "space", lazy.spawn(
                'play-pause')),
            # Makes reference to play-pause script
            # You can find it in my scripts repository
            # Screenshots
            Key([], "Print", lazy.spawn('xfce4-screenshooter')),
            Key([self.alt], "Print", lazy.spawn('xfce4-screenshooter -f -c')),
            Key([self.shift], "Print", lazy.spawncmd(
                "xfce4-screenshooter -f -s /home/daniel/Pictures/Screenshots/")),
                
            # ------------ Hardware Configs ------------

            # Volume
            Key([], "XF86AudioLowerVolume", lazy.spawn(
                "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
            Key([], "XF86AudioRaiseVolume", lazy.spawn(
                "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
            Key([], "XF86AudioMute", lazy.spawn(
                "pactl set-sink-mute @DEFAULT_SINK@ toggle")),

            # Brightness
            Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
            Key([], "XF86MonBrightnessDown",
                lazy.spawn("brightnessctl set 10%-")),
        ]

    def init_keys_groups(self, group_names):
        """
        Create bindings to move between groups
        """
        keys = []

        for icon in group_names:
            index = (icon[0]).lower()

            keys += [Key([self.mod, 'control'], index, lazy.group[icon].toscreen()), Key(
                [self.mod, 'shift'], index, lazy.window.togroup(icon, switch_group=True))]

        return keys


class Mouse:
    def __init__(self):
        self.mod = MOD

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse

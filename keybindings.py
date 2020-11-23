from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import layout

# Import the function that move the window to the next and prev group
from functions import Functions


class Keybindings:
    def __init__(self, mod="mod4", alt="mod1", altgr="mod5", termite="termite"):
        self.mod = mod
        self.alt = alt
        self.altgr = altgr
        self.termite = termite

    def init_keys(self):

        #################### CUSTOM KEYS  ##########################
        return [
            # Switch between windows in current stack pane
            Key([self.mod], "k", lazy.layout.down(),
                desc="Move focus down in stack pane"),
            Key([self.mod], "j", lazy.layout.up(),
                desc="Move focus up in stack pane"),

            # Move windows up or down in current stack
            Key([self.mod, "control"], "k", lazy.layout.shuffle_down(),
                desc="Move window down in current stack "),
            Key([self.mod, "control"], "j", lazy.layout.shuffle_up(),
                desc="Move window up in current stack "),
            Key([self.mod, "control"], "h", lazy.layout.swap_left()),
            Key([self.mod, "control"], "l", lazy.layout.swap_right()),

            # Move screen to next and previous workspace
            Key([self.mod], "l", lazy.screen.next_group(),
                desc="Move screen to the next workspace"),
            Key([self.mod], "h", lazy.screen.prev_group(),
                desc="Move screen to the previous workspace"),

            ####### MOVE WINDOWS TO PREV AND NEXT GROUPS ######
            Key([self.mod, "shift"], "l", Functions.window_to_next_group(),
                desc="Move window and screen to the next workspace"),
            Key([self.mod, "shift"], "h", Functions.window_to_prev_group(),
                desc="Move window and screen to the previous workspace"),

            ####### MOVE WINDOWS TO PREV AND NEXT GROUPS ######
            Key([self.mod, self.altgr], "w", Functions.kill_all_windows(),
                desc="Kill all windows in the workspace"),
            Key([self.mod, self.altgr], "c", Functions.kill_all_windows_minus_current(),
                desc="Kill all windows except current in the workspace"),

            # Switch window focus to other pane(s) of stack
            Key([self.mod], "space", lazy.layout.next(),
                desc="Switch window focus to other pane(s) of stack"),

            # Swap panes of split stack
            Key([self.mod, "shift"], "space", lazy.layout.rotate(),
                desc="Swap panes of split stack"),

            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            Key([self.mod, "shift"], "Return", lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack"),
            Key([self.mod], "Return", lazy.spawn(
                self.termite), desc="Launch terminal"),

            # Toggle between different layouts as defined below
            Key([self.mod], "Tab", lazy.next_layout(),
                desc="Toggle between layouts"),
            Key([self.mod], "w", lazy.window.kill(), desc="Kill focused window"),

            # Normalize or Maximize windows
            Key([self.mod, self.altgr], "n",
                lazy.layout.normalize(), desc="Normalize current windows"),
            Key([self.mod, self.altgr], "m",
                lazy.layout.maximize(), desc="Normalize current windows"),

            # Basic Commands
            Key([self.mod, "control"], "r",
                lazy.restart(), desc="Restart qtile"),
            Key([self.mod, "control"], "q",
                lazy.shutdown(), desc="Shutdown qtile"),
            Key([self.mod, self.alt], "space", lazy.spawn("dmenu_run -p 'Run: '"),
                desc="Run Dmenu"),

            ### THESE ARE MY PREFERED APPS YOU CAN SWITCH KEYBINDINGS JUST BY TYPING THE PATH TO YOUR APPS #####
            # Applications hotkeys
            # Apps are opened with Super + left self.alt keys
            Key([self.mod, self.alt], "d", lazy.spawn(
                "emacs"), desc="Open Doom Emacs"),
            Key([self.mod, self.alt], "v", lazy.spawn("gvim"), desc="Open Gvim"),
            Key([self.mod, self.alt], "o", lazy.spawn(
                "env LIBGL_ALWAYS_SOFTWARE=1 obs"), desc="Open Obs Studio"),
            Key([self.mod, self.alt], "n", lazy.spawn(
                self.termite + " -e nvim"), desc="Open Neovim"),
            Key([self.mod, self.alt], "f", lazy.spawn(self.termite + \
                                                      " -e ./.config/vifm/scripts/vifmrun"), desc="Open vifm"),
            Key([self.mod, self.alt], "b", lazy.spawn(
                "brave"), desc="Open Brave"),
            Key([self.mod, self.alt], "c", lazy.spawn(
                "codium"), desc="Open VS codium"),
            Key([self.mod, self.alt], "p", lazy.spawn(
                "pycharm"), desc="Open Pycharm CE"),
            Key([self.mod, self.alt], "a", lazy.spawn("pavucontrol"),
                desc="Open Pulse audio GUI controller"),
            Key([self.mod, self.alt], "e", lazy.spawn("emacs ~/.config/qtile/config.py"),
                desc="Open Qtile config file on emacs"),


            # PWA hotkeys

            Key([self.mod, self.alt], "s",
                lazy.spawn(
                    "/usr/lib/brave-beta/brave --profile-directory=Default --app-id=pjibgclleladliembfgfagdaldikeohf"),
                desc="Open Spotify PWA"),  # In others system the PWA id will be different

            Key([self.mod, self.alt], "y",
                lazy.spawn(
                    "/usr/lib/brave-beta/brave --profile-directory=Default --app-id=cinhimbnkkaeohfgghhklpknlkffjgod"),
                desc="Open Youtube Music PWA"),

            # Media hotkeys
            Key([self.mod], 'Up', lazy.spawn('pulseaudio-ctl up 5')),
            Key([self.mod], 'Down', lazy.spawn('pulseaudio-ctl down 5')),
            Key([self.mod], 'm', lazy.spawn('pulseaudio-ctl set 1')),

            # Screenshots
            Key([], "Print", lazy.spawn('flameshot gui')),
            Key([self.alt], "Print", lazy.spawn('flameshot full -c')),
        ]

    def init_keys_groups(self, group_names):
        """
        Create bindings to move between groups
        """
        keys = []

        for icon in group_names:
            indx = (icon[0]).lower()

            keys += [
                Key([self.mod, 'control'], indx, lazy.group[icon].toscreen()),
                Key([self.mod, 'shift'], indx, lazy.window.togroup(icon, switch_group=True))]

        return keys


class Mouse:
    def __init__(self):
        self.mod = "mod4"

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse

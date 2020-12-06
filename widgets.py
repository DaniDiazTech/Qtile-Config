import os
from libqtile import bar, layout, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

from functions import PWA
# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )

# extension_defaults = widget_defaults.copy()


class MyWidgets:
    def __init__(self):
        self.colors = [["#292d3e", "#292d3e"],  # panel background
                       # background for current screen tab
                       ["#434758", "#434758"],
                       ["#ffffff", "#ffffff"],  # font color for group names
                       # border line color for current tab
                       ["#bc13fe", "#bc13fe"],  # Group down color
                       # border line color for other tab and odd widgets
                       ["#8d62a9", "#8d62a9"],
                       ["#668bd7", "#668bd7"],  # color for the even widgets
                       ["#e1acff", "#e1acff"],  # window name

                       ["#000000", "#000000"],
                       ["#5B2C6F", "#5B2C6F"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"], ]

        self.termite = "termite"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.Image(
                filename="~/.config/qtile/icons/terminal-iconx14.png",
                mouse_callbacks={
                    'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run -p "Run: "')}
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="Ubuntu Bold",
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[2],
                inactive=self.colors[2],
                rounded=False,
                highlight_color=self.colors[1],
                highlight_method="line",
                this_current_screen_border=self.colors[3],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.Prompt(
                prompt=lazy.spawncmd(),
                font="Ubuntu Mono",
                padding=10,
                foreground=self.colors[3],
                background=self.colors[1]
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowName(
                foreground=self.colors[6],
                background=self.colors[0],
                padding=0
            ),
            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
            # widget.TextBox(
            #         text = '',
            #         background = self.colors[0],
            #         foreground = self.colors[4],
            #         padding = 0,
            #         fontsize = 37
            #         ),
            # widget.TextBox(
            #         text = " ⟳",
            #         padding = 2,
            #         foreground = self.colors[2],
            #         background = self.colors[4],
            #         fontsize = 14
            #         ),
            # # widget.CheckUpdates(
            # #         update_interval = 1000,
            # #         foreground = self.colors[2],
            # #         mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(self.termite + ' -e sudo pacman -Syu')},
            # #         background = self.colors[4]
            # #         ),
            # widget.TextBox(
            #         text = "Updates",
            #         padding = 5,
            #         mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(self.termite + ' -e sudo pacman -Syu')},
            #         foreground = self.colors[2],
            #         background = self.colors[4]
            #         ),
            widget.TextBox(
                text='',
                background=self.colors[0],
                foreground=self.colors[11],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text=" 🖬",
                foreground=self.colors[7],
                background=self.colors[11],
                padding=0,
                fontsize=14
            ),
            widget.Memory(
                foreground=self.colors[7],
                background=self.colors[11],
                mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                    self.termite + ' -e htop')},
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[11],
                foreground=self.colors[10],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[10],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                foreground=self.colors[7],
                background=self.colors[10],
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[10],
                foreground=self.colors[9],
                padding=0,
                fontsize=37
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=self.colors[0],
                background=self.colors[9],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                foreground=self.colors[7],
                background=self.colors[9],
                padding=5
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[8],
                background=self.colors[9],
                padding=0,
                fontsize=37
            ),
            widget.Clock(
                foreground=self.colors[7],
                background=self.colors[8],
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn(PWA.notion())},
                format="%B %d  [ %H:%M ]"
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[0],
                background=self.colors[8]
            ),
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=20))]

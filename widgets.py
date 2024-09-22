import os
from libqtile import bar, widget
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
                       ["#AD343E", "#AD343E"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"],
                       ["#f1ffff", "#f1ffff"],
                       ["#4c566a", "#4c566a"], ]

        self.termite = "alacritty"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
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
                active=self.colors[-2],
                inactive=self.colors[-1],
                # rounded=True,
                rounded=False,
                # highlight_color=self.colors[9],
                # highlight_method="line",
                highlight_method='block',
                urgent_alert_method='block',
                # urgent_border=self.colors[9],
                this_current_screen_border=self.colors[9],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=True
            ),
            # widget.Prompt(
            #     prompt=lazy.spawncmd(),
            #     font="Ubuntu Mono",
            #     padding=10,
            #     foreground=self.colors[3],
            #     background=self.colors[1]
            # ),
            widget.Sep(
                linewidth=0,
                padding=25,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowName(
                foreground=self.colors[6],
                background=self.colors[0],
                padding=5
            ),
            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
            # widget.TextBox(
            #     font="Ubuntu Bold",
            #     text='',
            #     background=self.colors[0],
            #     foreground=self.colors[11],
            #     padding=0,
            #     fontsize=37
            # ),
            widget.Battery(
                charge_char='+', discharge_char='-', error_message='error',
                format='{percent:2.0%} ({char}{hour:d}:{min:02d})', hide_threshold=None,
                low_percentage=0.1, foreground=self.colors[7], background=self.colors[10], update_delay=10),
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
                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                    self.termite + ' -e htop')},
                padding=5
            ),
            widget.ThermalSensor(
                # interface="enp5s0",
                # fmt='Net: {down} ↓↑ {up}',
                foreground=self.colors[7],
                background=self.colors[9],
                padding=5
            ),
            # widget.TextBox(
            #     text='',
            #     background=self.colors[11],
            #     foreground=self.colors[10],
            #     padding=0,
            #     fontsize=37
            # ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[10],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                foreground=self.colors[7],
                background=self.colors[10],
                padding=5
            ),
            # widget.TextBox(
            #     text='',
            #     background=self.colors[10],
            #     foreground=self.colors[9],
            #     padding=0,
            #     fontsize=37
            # ),
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
            # widget.TextBox(
            #     text='',
            #     foreground=self.colors[8],
            #     background=self.colors[9],
            #     padding=0,
            #     fontsize=37
            # ),
            widget.Clock(
                foreground=self.colors[7],
                background=self.colors[8],
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())},
                format="%A %d - %H:%M"
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

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen2 = self.init_widgets_screen()
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=20)),
                Screen(top=bar.Bar(
                    widgets=self.init_widgets_screen2(), opacity=1.0, size=20))
                ]


# bar = Bar([
#         Sep(
#             linewidth = 0,
#             padding = 2,
#             foreground = onedark_darker["color4"],
#             background = onedark_darker["color4"]
#         ),
#         Image(
#             filename = "~/.config/qtile/icons/archlinux_blue.png",
#             scale = "False",
#             mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty")},
#             background = onedark_darker["color4"],
#         ),
#         #widget.Sep(
#         #    linewidth = 0,
#         #    padding = 2,
#         #    foreground = onedark_darker["colorback"],
#         #    background = onedark_darker["colorback"]
#         #),
#         right_arrow(onedark_darker["color4"], onedark_darker["colorback"]),
#         GroupBox(
#             font = "JetBrains Nerd Font Mono Bold",
#             fontsize = 12,
#             fmt = '{}',
#             borderwidth = 2,
#             background = onedark_darker["colorback"],
#             active = onedark_darker["color6"],
#             inactive = onedark_darker["color5"],
#             rounded = False,
#             #Block_highlight_text_color = onedark_darker["color3"],
#             highlight_method = 'line',
#             highlight_color = onedark_darker["colorback"],  #  line block colour
#             this_current_screen_border = onedark_darker["color4"],
#             this_screen_border = onedark_darker["color7"],
#             urgent_alert_method = 'line',
#             urgent_border = onedark_darker["color10"],
#             urgent_text = onedark_darker["color14"],
#             disable_drag = True,
#         ),
#         right_arrow(onedark_darker["colorback"], onedark_darker["color14"]),
#         CurrentLayoutIcon(
#             custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color14"],
#             padding = 0,
#             scale = 0.7
#         ),
#         CurrentLayout(
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color14"],
#             padding = 5,
#         ),
#         right_arrow(onedark_darker["color14"], onedark_darker["color9"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             background = onedark_darker["color9"],
#             foreground = onedark_darker["color4"],
#             padding = 2
#         ),
#         WindowCount(
#             format = ' {num} ',
#             background = onedark_darker["color9"],
#             foreground = onedark_darker["color4"],
#             show_zero = True,
#         ),
#         right_arrow(onedark_darker["color9"], onedark_darker["color1"]),
#         WindowName(
#             foreground = onedark_darker["color5"],
#             background = onedark_darker["color1"],
#             padding = 5,
#             format = '[ {name} ]',
#             empty_group_string = '[ ]',
#             parse_text = parse_func,
#         ),
#         #widget.Spacer(),
#         Sep(
#             linewidth = 0,
#             padding = 6,
#             foreground = onedark_darker["color1"],
#             background = onedark_darker["color1"],
#         ),
#         left_arrow(onedark_darker["color2"], onedark_darker["color1"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color2"],
#         ),
#         Net(
#             interface = "wlp44s0",
#             format = '{down} {up}',
#             prefix = 'M',
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color2"],
#             padding = 5,
#         ),
#         left_arrow(onedark_darker["color3"], onedark_darker["color2"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color3"]
#         ),
#         CPU(
#             background = onedark_darker["color3"],
#             foreground = onedark_darker["colorback"],
#             fmt = 'Cpu: {}',
#             #format = '{freq_current}GHz {load_percent}%',
#             format = '[ {load_percent} ]%',
#             padding = 5,
#         ),
#         left_arrow(onedark_darker["color4"], onedark_darker["color3"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color4"]
#         ),
#         ThermalSensor(
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color4"],
#             threshold = 90,
#             fmt = 'Temp: {}',
#             format='[ {temp:.0f}{unit} ]',
#             padding = 5,
#         ),
#         left_arrow(onedark_darker["color5"], onedark_darker["color4"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color5"]
#         ),
#         Memory(
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color5"],
#             #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
#             fmt = 'Mem: {}',
#             #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
#             format = '[ {MemUsed:.0f} ]{mm}',
#             padding = 5,
#         ),
#         left_arrow(onedark_darker["color6"], onedark_darker["color5"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color6"]
#         ),
#         Battery(
#             padding = 5,
#             background = onedark_darker["color6"],
#             foreground = onedark_darker["colorback"],
#             charge_char = 'AC',
#             discharge_char = '',
#             empty_char = 'ﮣ',
#             full_char = 'ﭹ',
#             fmt = 'Bat: {}',
#             format = '{char}[ {percent:2.0%} ]', #{hour:d}:{min:02d} {watt:.2f} W'
#             #low_background = none,
#             low_forground = '#ff0000',
#             update_interval = 60,
#         ),
#         #battery,

#         left_arrow(onedark_darker["color7"], onedark_darker["color6"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color7"]
#         ),
#         PulseVolume(
#             background = onedark_darker["color7"],
#             foreground = onedark_darker["colorback"],
#             fmt = 'Vol: [ {} ]',
#             device = 'default',
#             channel = 'Master',
#             limit_max_volume = True,
#             padding = 5,
#             update_interval = 0.1,
#             mute_command = 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
#             volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
#             volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
#         ),
#         #volume,
#         #widget.Volume(
#         #    foreground = onedark_darker[8],
#         #    background = onedark_darker[0],
#         #    fmt = 'Vol: {}',
#         #    padding = 5,
#         #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')}
#         #),
#         left_arrow(onedark_darker["color10"], onedark_darker["color7"]),
#         TextBox(
#             text = '',
#             font = "Font Awesome 6 Free Solid",
#             fontsize = 15,
#             padding = 2,
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color10"]
#         ),
#         Clock(
#             foreground = onedark_darker["colorback"],
#             background = onedark_darker["color10"],
#             format = "%a %d, %b [ %I:%M ]%P",
#             padding = 5,
#         ),
#         left_arrow(onedark_darker["colorback"], onedark_darker["color10"]),
#         Systray(
#             background = onedark_darker["colorback"],
#             padding = 2
#         ),

#         #widget.TextBox(
#         #    text = '',
#         #    font = "Mononoki Regular Bold",
#         #    fontsize = 18,
#         #    padding = 0,
#         #    background = onedark_darker[0],
#         #    foreground = onedark_darker[9],
#         #),
#     ], size=25)

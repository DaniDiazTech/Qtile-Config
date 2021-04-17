from libqtile import layout


class Layouts:
    def __init__(self):
        self.default = {
            "border_width": 2,
            "margin": 8,
            "border_focus": "#668bd7",
            "border_normal": "1D2330"}

    def init_layouts(self):
        """
        Returns the layouts variable
        """
        layouts = [
            layout.Max(**self.default),
            layout.MonadTall(**self.default),
            layout.floating.Floating(**self.default),
            layout.TreeTab(
                font="Ubuntu",
                fontsize=10,
                sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
                section_fontsize=10,
                border_width=2,
                bg_color="1c1f24",
                active_bg="c678dd",
                active_fg="000000",
                inactive_bg="a9a1e1",
                inactive_fg="1c1f24",
                padding_left=0,
                padding_x=0,
                padding_y=5,
                section_top=10,
                section_bottom=20,
                level_shift=8,
                vspace=3,
                panel_width=200
            ),
            # layout.Stack(num_stacks=2),
            # Try more layouts by unleashing below layouts.
            # layout.Bsp(),
            # layout.Columns(),
            # layout.Matrix(),
            # layout.MonadWide(**self.default),
            # layout.RatioTile(),
            # layout.Tile(),
            # layout.VerticalTile(),
            # layout.Zoomy(),
        ]
        return layouts

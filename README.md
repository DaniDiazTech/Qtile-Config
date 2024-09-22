# Qtile configuration file

## Screenshots 🖥️

![Qtile Screenshots](../assets/Remake-1.png)

![Qtile Screenshots](../assets/Remake-2.png)

![Qtile Screenshots](../assets/REMAKE-3.png)

## What is Qtile?

[Qtile](http://www.qtile.org/) is a window manager written and configured in Python🐍. It is hackable and lightweight, you can install it among other desktop environments and [standalone WM's](https://wiki.archlinux.org/index.php/window_manager).

## Installation 🐧

Install Qtile and other dependencies.

### For Arch Linux
All software, one command:

```bash
yay -S qtile picom rofi nitrogen xorg-server-xephyr
lxappearance-gtk3 megasync python-psutil brave-browser alacritty
bat playerctl pulseaudio-ctl dunst alacritty fish starship neovim
pavucontrol flameshot noto-fonts-emoji noto-fonts-emoji brightnessctl blueman xfce4-power-manager network-manager-applet xfce4-clipman-plugin
```

Also install Rofi Power menu:
```
git clone git@github.com:jluttine/rofi-power-menu.git
cp rofi-power-menu ~/.local/bin/
```

The [xephyr](https://wiki.archlinux.org/index.php/Xephyr) package is for testing purposes.

[Nitrogen](https://wiki.archlinux.org/index.php/nitrogen) help us to set a cool wallpaper since Qtile doesn't have a wallpaper manager by default.

### For Debian, Ubuntu

For Debian, Ubuntu and derivates [here](http://docs.qtile.org/en/latest/manual/install/ubuntu.html) is the qtile installation guide.

#### Dependencies

```
sudo apt install picom rofi xserver-xephyr nitrogen
```

## Cloning the config files 📁

```
git clone git@github.com:DaniDiazTech/Qtile-Config.git ~/.config/qtile
```

## Testing 🧪

If you want to test the config files without crashing your current qtile instance, type the following commands:

```
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile "/PATH/TO/TEST-CONFIG"
```

Once you've done all these steps you should have a cool Qtile instance, but most keybindings won't work, because probably you don´t have the software I use, you could install [my software](https://github.com/DaniDiazTech/Qtile-Config/blob/main/software.txt) or re-map the keybindings in [keybindings.py](https://github.com/Daniel1404/Qtile-Config/blob/main/keybindings.py) file.

## Startup  🏁

One of the most important functions in the config is the startup function located at the bottom of _config.py_.

``` python
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
```

You can manage the autostart applications editing the  _autostart.sh_ file.

``` bash
#! /bin/bash 
picom --experimental-backend &
nitrogen --restore &
```

You can setup your Qtile instance quickly using the `setup.py` file:

```python
python setup.py
```

Remember to set a wallpaper with nitrogen so every time you boot into Qtile, your wallpaper will be restored.

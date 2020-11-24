# Qtile configuration file

## Screenshots

![Qtile Screenshots](../assets/qtile-2.png)

![Qtile Screenshots](../assets/Qtile-1.png)

## What is Qtile?

[Qtile](http://www.qtile.org/) is a window manager written and configured in python, it is really hackable and lightweight, you can install it among other desktop environments and [standalone WM's](https://wiki.archlinux.org/index.php/window_manager). 

## Installation
Install Qtile and other dependencies.

### For Arch Linux

```
sudo pacman -S qtile picom rofi nitrogen xorg-server-xephyr
```

The [xephyr](https://wiki.archlinux.org/index.php/Xephyr) package is for testing  purposes.

[Nitrogen](https://wiki.archlinux.org/index.php/nitrogen) Help us to set a cool wallpaper since qtile don´t have a wallpaper manager by default.

### For Debian, Ubuntu

For Debian, Ubuntu and derivates [here](http://docs.qtile.org/en/latest/manual/install/ubuntu.html) is the qtile installation guide.
#### Dependencies
```
sudo apt install picom rofi xserver-xephyr nitrogen
```
## Cloning the config files
```
git clone git@github.com:Daniel1404/Qtile-Config.git ~/.config/qtile
```

## Testing 

If you want to test the config files, without crash your current qtile instance, type the following commands:

```
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile "/PATH/TO/TEST-CONFIG"
```
Once you've done all these steps you  should have a cool Qtile instance, but most keybindings won't work, because probably you don´t have the software I use, you could install [my software]() or re-map the keybindings in [keybindings.py](https://github.com/Daniel1404/Qtile-Config/blob/main/keybindings.py) file.

## Startup 

One of the most important functions in the config is the startup function located  at the button of _config.py_.

``` python
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
```
You can manage the autostart applications modyfing the  _autostart.sh_ file.

``` bash
#! /bin/bash 
picom &
nitrogen --restore &
```
Remember to set a wallpaper with nitrogen so every startup your wallpaper will be restored.

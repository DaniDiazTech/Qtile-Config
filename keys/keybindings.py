
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Import the function that move the window to the next and prev group
from functions import Functions, PWA

from config_keybindings import *


class Keybindings:

    keys = []
    
    spawn_keys = SPAWN_KEYS
    
    cmd_keys = SPAWN_CMD_KEYS

    def create_layout_keys(self):
        ############   BINDINGS FOR MONADTALL   ##############
        modifier = [MOVEMENT_KEY]
        
        layout_left  = Key(modifier, LEFT, lazy.layout.left())
        
        layout_right = Key(modifier, RIGHT, lazy.layout.right())
        
        layout_down  = Key(modifier, DOWN, lazy.layout.down())
        
        layout_up    = Key(modifier, UP, lazy.layout.up())

        toogle_layout = Key(modifier, TOOGLE_LAYOUT, lazy.next_layout())
        
        self.keys += [layout_left, layout_right, layout_down, layout_up, toogle_layout] 

    def create_swap_keys(self):
        modifier = [MOVEMENT_KEY, SWAP_KEY]

        left  = Key(modifier, SWAP_LEFT, lazy.layout.swap_left())
        right = Key(modifier, SWAP_RIGHT, lazy.layout.swap_right())
        down  = Key(modifier, SWAP_DOWN, lazy.layout.shuffle_down())
        up    = Key(modifier, SWAP_UP, lazy.layout.shuffle_up())
        
        flip  = Key(modifier, SWAP_FLIP, lazy.layout.flip()) 

        self.keys += [left, right, down, up, flip] 

    
    def create_windows_keys(self):
        
        modifier = [MOVEMENT_KEY] 

        grow      = Key(modifier, GROW, lazy.layout.grow())
        shrink    = Key(modifier, SHRINK, lazy.layout.shrink())
        normalize = Key(modifier, NORMALIZE, lazy.layout.normalize())
        maximize  = Key(modifier, MAXIMIZE, lazy.layout.maximize())
        
        self.keys += [grow, shrink, normalize, maximize] 
    
    def create_shutdown_keys(self):
        
        shutdown = Key(SHUTDOWN_MODIFIER, SHUTDOWN, lazy.shutdown())
        restart  = Key(SHUTDOWN_MODIFIER, RESTART, lazy.restart())
        
        self.keys += [shutdown, restart]
    
    def create_kill_keys(self):
        modifier = [MOVEMENT_KEY, ALTGR] 

        all_minus_current = Key(modifier, KILL_ALL_MINUS_CURRENT, 
                            Functions.kill_all_windows_minus_current())
        all_              = Key(modifier, KILL_ALL,
                            Functions.kill_all_windows())
        current           = Key([KILL_KEY], KILL_CURRENT,
                                lazy.window.kill())
       
        self.keys += [all_minus_current, all_, current] 

    def create_floating_keys(self):
        
        modifier = [MOVEMENT_KEY, FLOATING_KEY]

        floating = Key(modifier, TOOGLE_FLOATING, lazy.window.toggle_floating())
        full = Key(modifier, TOOGLE_FULL, lazy.window.toggle_fullscreen())
        
        self.keys += [floating, full]        
    
    def create_groups_keys(self):
        modifier      = [GROUPS_KEY]
        swap_modifier = [GROUPS_KEY, SWAP_GROUP_KEY]

        move_next = Key(modifier, NEXT_GROUP, lazy.screen.next_group()) 
        move_prev = Key(modifier, PREV_GROUP, lazy.screen.prev_group()) 
        
        swap_next = Key(swap_modifier, NEXT_GROUP, Functions.window_to_next_group()) 
        swap_prev = Key(swap_modifier, PREV_GROUP, Functions.window_to_prev_group()) 

        self.keys += [move_next, move_prev, swap_next, swap_prev]

    def create_spawn_keys(self):
           
        for spawn_key in self.spawn_keys:
            
            modifier, key, command = spawn_key

            keybinding = Key(modifier, key, lazy.spawn(command)) 

            self.keys.append(keybinding)
            
    def create_cmd_keys(self):
                    
        for cmd_key in self.cmd_keys:
            
            modifier, key, command = cmd_key

            keybinding = Key(modifier, key, lazy.spawncmd(command)) 

            self.keys.append(keybinding)
    
    
    def init_keys_groups(self, group_names):
        """
        Create bindings to move between groups
        """
        group_keys = []
        for icon in group_names:
            index = (icon[0]).lower()

            group_keys += [Key([MOVEMENT_KEY, GROUPS_KEY], index, lazy.group[icon].toscreen()), Key(
                [MOVEMENT_KEY, SWAP_GROUP_KEY], index, lazy.window.togroup(icon, switch_group=True))]

        return group_keys        
        
    def init_keys(self):
        
        self.create_layout_keys()
        self.create_swap_keys()
        self.create_windows_keys()
        self.create_shutdown_keys()
        self.create_kill_keys()
        self.create_floating_keys()
        self.create_groups_keys()

        self.create_cmd_keys() 
        self.create_spawn_keys()

        return self.keys
        

class Mouse:
    def __init__(self, mod_key=MOD):
        self.mod = mod_key

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse



from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess



mod = "mod4"
terminal = guess_terminal()




keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.function(lambda _: subprocess.run(["amixer", "set", "Master", "5%+"])), desc="rise volume"),
    Key([], "XF86AudioLowerVolume", lazy.function(lambda _: subprocess.run(["amixer", "set", "Master", "5%-"])), desc="lower volume"),
    Key([], "XF86AudioMute", lazy.function(lambda _: subprocess.run(["amixer", "set", "Master", "toggle"])), desc="set to 0 volume"),
    Key([], "XF86MonBrightnessUp", lazy.function(lambda _: subprocess.run(["/home/noa/.qtilescript/log", "xbacklight -set", "", "xbacklight -get", "110", "20", "1"])), desc="set to 0 volume"),
    Key([], "XF86MonBrightnessDown", lazy.function(lambda _: subprocess.run(["/home/noa/.qtilescript/log", "xbacklight -set", "", "xbacklight -get", "91", "20", "-1"])), desc="set to 0 volume"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([], "Print", lazy.function(lambda _: subprocess.run(["scrot", "/home/noa/Documents/screenshots/%Y-%m-%d-%T-screenshot.png"]))),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),



    KeyChord([mod], "u", [
        Key([], "XF86MonBrightnessUp", lazy.function(lambda _: subprocess.run(["/home/noa/.qtilescript/log", "xbacklight -set", "", "xbacklight -get", "250", "20", "5"])), desc="set to 0 volume"),
        Key([], "XF86MonBrightnessDown", lazy.function(lambda _: subprocess.run(["/home/noa/.qtilescript/log", "xbacklight -set", "", "xbacklight -get", "40", "20", "-5"])), desc="set to 0 volume")],
        mode="ultra")
]
 

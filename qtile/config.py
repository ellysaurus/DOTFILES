# -*- coding: utf-8 -*-
#
#                                  qtile config
#                          ____________________________
#                              ██╗    ██╗   ███████╗
#                              ██║    ██║   ██╔════╝
#                              ██║ █╗ ██║   █████╗
#                              ██║███╗██║   ██╔══╝
#                              ╚███╔███╔╝██╗███████╗
#                               ╚══╝╚══╝ ╚═╝╚══════╝
#            This is my config file for the tiling window manager qtile
#                    This is based a lot on DistroTube's config
#        -------------------------------------------------------------------
#        GitHub:    https://github.com/waltereikrem
#        YouTube:   https://www.youtube.com/channel/UC7HB3RUOhPsFEZakNTA01CQ
#        -------------------------------------------------------------------
#
#
# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myConfig = "/home/walter/.config/qtile/config.py"    # The Qtile config file location

##### KEYBINDINGS #####
keys = [
         ### The essentials
         Key(
             [mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key(
             [mod, "shift"], "Return",
             lazy.spawn("krunner"),
             desc='Krunner Run Launche'
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key(
             [mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key(
             [mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Window controls
         Key(
             [mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key(
             [mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key(
             [mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key(
             [mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key(
             [mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key(
             [mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key(
             [mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         ### Stack controls
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key(
             [mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         ### Dmenu scripts launched with ALT + CTRL + KEY
         Key(
             ["mod1", "control"], "e",
             lazy.spawn("./.dmenu/dmenu-edit-configs.sh"),
             desc='Dmenu script for editing config files'
             ),
         Key(
             ["mod1", "control"], "m",
             lazy.spawn("./.dmenu/dmenu-sysmon.sh"),
             desc='Dmenu system monitor script'
             ),
         Key(
             ["mod1", "control"], "p",
             lazy.spawn("passmenu"),
             desc='Passmenu'
             ),
         Key(
             ["mod1", "control"], "r",
             lazy.spawn("./.dmenu/dmenu-reddio.sh"),
             desc='Dmenu reddio script'
             ),
         Key(
             ["mod1", "control"], "s",
             lazy.spawn("./.dmenu/dmenu-surfraw.sh"),
             desc='Dmenu surfraw script'
             ),
         Key(
             ["mod1", "control"], "t",
             lazy.spawn("./.dmenu/dmenu-trading.sh"),
             desc='Dmenu trading programs script'
             ),
         Key(
             ["mod1", "control"], "i",
             lazy.spawn("./.dmenu/dmenu-scrot.sh"),
             desc='Dmenu scrot script'
             ),
         ### My applications launched with SUPER + ALT + KEY
         Key(
             [mod, "mod1"], "b",
             lazy.spawn("brave"),
             desc='brave browser'
             ),
]

##### GROUPS #####
group_names = [(" 1 ", {'layout': 'monadtall'}),
               (" 2 ", {'layout': 'monadtall'}),
               (" 3 ", {'layout': 'monadtall'}),
               (" 4 ", {'layout': 'monadtall'}),
               (" 5 ", {'layout': 'monadtall'}),
               (" 6 ", {'layout': 'monadtall'}),
               (" 7 ", {'layout': 'monadtall'}),
               (" 8 ", {'layout': 'monadtall'}),
               (" 9 ", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 3,
                "margin": 25,
                "border_focus": "d7af87",
                "border_normal": "1b1519"
                }

##### THE LAYOUTS #####
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [["#1b1519", "#1b1519"], # 0 - panel background
          ["#40323b", "#40323b"], # 1 - background for current screen tab
          ["#fdfdae", "#fdfdae"], # 2 - font color for group names
          ["#ebdbb2", "#ebdbb2"], # 3 - border line color for current tab
          ["#39342d", "#39342d"], # 4 - border line color for other tab and odd widgets
          ["#2b2222", "#2b2222"], # 5 - color for the even widgets
          ["#c3807a", "#c3807a"], # 6 - window title
          ["#c3807a", "#c3807a"], # 7 - dark beige font color
          ["#535337", "#535337"], # 8 - dark beige background
          ["#3a3a3a", "#3a3a3a"]] # 9 - dark gray systray

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####
def init_widgets_list():
    widgets_list = [
          widget.TextBox(
                        text ='  ',# i 
                        background = colors[0],
                        foreground = colors[2],
                        fontsize=14
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Hack Nerd Font",
                        fontsize = 9,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0
                        ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[5],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" ₿",
                        padding = 0,
                        foreground=colors[7],
                        background=colors[5],
                        fontsize=12
                        ),
               widget.BitcoinTicker(
                        foreground=colors[7],
                        background=colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=-4.5,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" 🌡",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[4],
                        fontsize=11
                        ),
               widget.ThermalSensor(
                        foreground=colors[2],
                        background=colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.TextBox(
                        text="  ",
                        padding = 2,
                        foreground=colors[7],
                        background=colors[5],
                        fontsize=14
                        ),
               widget.Pacman(
                        execute = "alacritty",
                        update_interval = 1800,
                        foreground = colors[7],
                        background = colors[5]
                        ),
               widget.TextBox(
                        text=" ",
                        padding = -1,
                        foreground=colors[7],
                        background=colors[5]
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.Net(
                        interface = "wlp0s20f3",
                        format = '  {down} ↓↑ {up}',
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.TextBox(
                       text="  ",
                        foreground=colors[7],
                        background=colors[5],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[7],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[0],
                        background = colors[4],
                        padding = 0,
                        scale=0.7
                        ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.Clock(
                        foreground = colors[7],
                        background = colors[5],
                        format="%A, %B %d  %H:%M "
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=-5.5,
                        fontsize=36
                        ),
               widget.TextBox(
                        text=' ',
                        background = colors[4],
                        foreground = colors[3],
                        padding=0.5,
                        fontsize=16
                        ),
               widget.Battery(
                	format = "{char} {percent:-1.1%}",
                	update_interval = 0.5,
                        padding=4,
                	low_percentage = -1.05,
                	full_char = " Full",
                	charge_char = "",
                	discharge_char = "",
                        background = colors[4],
                        font="Hack Nerd Font",
                        foreground = colors[3],
                       ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[0],
                        background = colors[4]
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=-5.5,
                        fontsize=37
                        ),
               widget.Systray(
                        background=colors[5],
                        padding = 5
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[0],
                        background = colors[5]
                        ),
              ]

    return widgets_list

##### SCREENS ##### (TRIPLE MONITOR SETUP)
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'krunner'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"

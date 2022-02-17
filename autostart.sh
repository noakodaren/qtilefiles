#!/bin/sh
setxkbmap se &
xss-lock ./.locker &
xfsettingsd &
xfconf-query -c xfce4-keyboard-shortcuts -p / -r -R &

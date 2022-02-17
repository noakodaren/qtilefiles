#!/bin/sh
setxkbmap se &
xinput set-prop 11 323 1 &
xss-lock ./.locker &
xfsettingsd &
xfconf-query -c xfce4-keyboard-shortcuts -p / -r -R &
xinput set-prop 11 352 0 

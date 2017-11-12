#!/bin/bash

setxkbmap

xmodmap -e "keycode 135 = Left"
xmodmap -e "keycode 113 = Right"

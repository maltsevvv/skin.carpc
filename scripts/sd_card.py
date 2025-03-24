#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import xbmc
import subprocess

cmd = "df -h | awk '$NF==\"/\"{printf $1}'"
sd = subprocess.check_output(cmd, shell = True).decode("utf-8")
sd = str(sd)
if sd == '/dev/mmcblk0p2' or sd == '/dev/root':
    xbmc.executebuiltin('Notification($LOCALIZE[20186], $LOCALIZE[13013])')
    os.system('sudo raspi-config nonint enable_overlayfs && sudo reboot')
elif sd == 'overlayroot' or sd == 'overlay':
    xbmc.executebuiltin('Notification($LOCALIZE[20186], $LOCALIZE[13013])')
    os.system('sudo raspi-config nonint disable_overlayfs && sudo reboot')
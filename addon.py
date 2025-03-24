#!/usr/bin/env python

from __future__ import print_function
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs
import os
import sys
import subprocess
import re
import threading
import string
import time

from time import sleep
from sendcan import sendcan
from tvtuner import tvtuner
from dumpcan import dumpcan
from bluetooth import a2dpinfo
from threading import Thread, Timer

def rpi_cpu():
    cmd = 'vcgencmd measure_temp'
    cpu_temp = subprocess.check_output(cmd, shell=True).decode("utf8")
    cpu_temp = str(cpu_temp[5:9])
    xbmcgui.Window(10000).setProperty('rpi_cpu', str(cpu_temp))
    sleep(5)
    rpi_cpu()

def sd():
    cmd = "df -h | awk '$NF==\"/\"{printf $1}'"
    sd = subprocess.check_output(cmd, shell = True).decode("utf-8")
    sd = str(sd)
    if sd == '/dev/mmcblk0p2' or sd == '/dev/root':
        xbmc.executebuiltin('Skin.SetString(sd,open)')
    elif sd == 'overlayroot' or sd == 'overlay':
        xbmc.executebuiltin('Skin.SetString(sd,close)')

if __name__ == '__main__':
    Thread(target = dumpcan).start()
    Thread(target = tvtuner).start()
    Thread(target = sendcan).start()
    Thread(target = a2dpinfo).start()
    Thread(target = rpi_cpu).start()
    Thread(target = sd).start()
    
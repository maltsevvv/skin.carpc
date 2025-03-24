import sys
import os
import xbmc
import can
import datetime
import glob

import urllib3

BOT = '5914983604:AAHGhxt0yRz4hmCa2tcoU2fgVfibkN9Eg0s'
ID = '260825514'

datetime = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S');
logdir = "/home/pi/log/"

xbmc.executebuiltin('Notification(Start, Log CAN-Bus Create )');
makedir = 'mkdir ' + logdir
os.system(makedir);
os.system('candump can0 -a -n 5000 -e -x | sudo  tee ' + logdir + 'canlog-' + datetime + '.txt')
xbmc.executebuiltin('Notification(Finish, Log CAN-Bus Created )');

list_of_files = glob.glob(logdir + '*')
latest_file = max(list_of_files, key=os.path.getmtime)
final_path = "@" + latest_file


def check_internet_conn():
    http = urllib3.PoolManager(timeout=3.0)
    r = http.request('GET', 'google.com', preload_content=False)
    code = r.status
    r.release_conn()
    if code == 200:
        return True
    else:
        return False

def send():
    if check_internet_conn() == True: 
        send_tm = "curl -s -X POST 'https://api.telegram.org/bot" + BOT + "/sendDocument' -F chat_id=" + ID + " -F document=" + final_path + " -F caption=" # + MSG + ""
        os.system(send_tm)
        xbmc.executebuiltin('Notification(Log CAN-Bus, Send to Telegram Bot )');
    else:
        xbmc.executebuiltin('Notification(ERROR, Send Log CAN-Bus to Telegram Bot)');
send()

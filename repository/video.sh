#!/bin/bash

BGreen="\033[1;32m"     # Green
BRed="\033[1;31m"       # Red
BBlue="\033[1;34m"      # Blue
NC="\033[0m"            # No Color



if [ -e /boot/firmware/config.txt ] ; then
  FIRMWARE=/firmware
else
  FIRMWARE=
fi
CONFIG=/boot${FIRMWARE}/config.txt

if [ -e /boot/firmware/cmdline.txt ] ; then
  FIRMWARE=/firmware
else
  FIRMWARE=
fi
CMDLINE=/boot${FIRMWARE}/cmdline.txt

rpi_conf() {
	if ! [ -e $CONFIG.backup ] ; then
		cp $CONFIG $CONFIG.backup
	fi
	if ! [ -e $CMDLINE.backup ] ; then
		cp $CMDLINE $CMDLINE.backup
	fi
}


config_tv() {
	if [ -e $CMDLINE.rns ]; then
		rm $CMDLINE.rns
	fi
	cp $CMDLINE $CMDLINE.rns
	cp $CMDLINE.backup $CMDLINE
	reboot
}


config_rns() {
	if [ -e $CMDLINE.rns ]; then
		rm $CMDLINE.backup
		mv $CMDLINE.rns $CMDLINE
		reboot
	fi
}


echo '---------------------------------------------------------'
if (whiptail --title "Video Output" --yes-button " TV " --no-button " RNS " --yesno "Select video output source" 10 60); then
	echo ${BGreen}"Use HDMI Video Output TV"${NC}
	echo $(config_tv)
else
	echo ${BGreen}"Use HDMI Video Output RNS"${NC}
	echo $(config_rns)
fi
echo '---------------------------------------------------------'


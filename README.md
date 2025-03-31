[![Raspberry - Buster](https://img.shields.io/badge/Raspberry-Buster_(Kodi_18)-blue?logo=raspberrypi&logoColor=red)](https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2020-02-14/2020-02-13-raspbian-buster-lite.zip "Downloads Buster")
[![Raspberry - Bookworm](https://img.shields.io/badge/Raspberry-Bookworm_(Kodi_20)-blue?logo=raspberrypi&logoColor=red)](https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2024-07-04/2024-07-04-raspios-bookworm-arm64-lite.img.xz "Downloads Bookworm")

[![KODI-repository](https://img.shields.io/badge/KODI-repository.maltsev_kodi.zip-red?logo=kodi)](https://github.com/maltsevvv/repository-kodi/raw/refs/heads/master/repository.maltsev_kodi.zip "Downloads Repository for auto update skin")
[![KODI_18-skin.carpc](https://img.shields.io/badge/KODI_18-skin.carpc-red?logo=kodi)](https://github.com/maltsevvv/repository-kodi/raw/refs/heads/master/kodi18/skin.carpc/skin.carpc-1.0.5.zip "Downloads Latest Version Skin CarPC for Kodi 18")
[![KODI_20-skin.carpc](https://img.shields.io/badge/KODI_20-skin.carpc-red?logo=kodi)](https://github.com/maltsevvv/repository-kodi/raw/refs/heads/master/kodi20/skin.carpc/skin.carpc-1.0.5.zip "Downloads Latest Version Skin CarPC for Kodi 20")



## Скрипт для автоматической установки  
```
sudo apt update
```

```
sudo apt upgrade -y
```

```
wget -P /tmp https://raw.githubusercontent.com/maltsevvv/skin.carpc/master/repository/autoinstall.sh
```

```
sudo sh /tmp/autoinstall.sh
```

***
## MCP2515(sn65hvd230) NiRen connect to Raspberry PI. Recommended
[![RPI-CAN](https://github.com/maltsevvv/repository-kodi/blob/master/img/rpi+mcp2515sn230+pcm5102.png)

## MCP2515(tja1050) NiRen connect to Raspberry PI
[![RPI-CAN](https://github.com/maltsevvv/repository-kodi/blob/master/img/rpi+mcp2515tja1050+pcm5102.png)

## Possibility of receiving video on RNSD
[![RNSD](https://github.com/maltsevvv/repository-kodi/blob/master/img/rnsd.png)

## Possibility of receiving video on RNSE
[![RNSE](https://github.com/maltsevvv/repository-kodi/blob/master/img/rnse.png)
***
## Raspberry Pi Audio Receiver

Через телефон передаем аудио на Raspberry, а затем звук выводится на аудио систему.

### Requirements

- Использовать USB-адаптер Bluetooth (внутренний чипсет Raspberry Pi Bluetooth оказался неподходящим для воспроизведения звука и вызывает всевозможные странные проблемы с подключением)

- Адаптер USB – Bluetooth V5.0

**Еще раз: не пытайтесь использовать внутренний чип Bluetooth.**

### Добавить устройства Bluetooth

Устройство должно быть доступно для новых подключений Bluetooth, но в некоторых случаях вам может потребоваться выполнить сопряжение вручную:

    sudo bluetoothctl

    scan on

    connect 00:00:00:00:00:00

    trust 00:00:00:00:00:00

 `Заменить 00:00:00:00:00:00 на MAC Вашего телефона`
### Вы используете USB Bluetooth модуль. Необходимо проверить определился ли он в OS.

    hciconfig

`hci0:   Type: Primary  Bus: USB`  
`        BD Address: 00:1A:7D:DA:71:13  ACL MTU: 679:8  SCO MTU: 48:16`  
`        DOWN` `Bluetooth не работает. Можно, попробовать обновить ядро Linux.`  
`        RX bytes:706 acl:0 sco:0 events:22 errors:0`  
`        TX bytes:68 acl:0 sco:0 commands:22 errors:0`  

    sudo rpi-update

    sudo reboot

### Проверяем статyс USB Bluetooth модуля.

    hciconfig

`hci0:   Type: Primary  Bus: USB`  
`        BD Address: 00:1A:7D:DA:71:13  ACL MTU: 679:8  SCO MTU: 48:16`  
`        UP RUNNING PSCAN ISCAN` `Все хорошо, работает.`  
`        RX bytes:706 acl:0 sco:0 events:22 errors:0`  
`        TX bytes:68 acl:0 sco:0 commands:22 errors:0`  

### Отключить встроенный BT в raspberry pi  

    sudo nano /boot/firmware/config.txt

`dtoverlay=disable-bt`

    sudo reboot


## Подключается, но нет звука

Проверить номер идентификатора аудио карты

    cat /proc/asound/cards

`0 [b1             ]: bcm2835_hdmi - bcm2835 HDMI 1`  
`1 [Headphones     ]: bcm2835_headpho - bcm2835 Headphones`  
`2 [sndrpihifiberry]: RPi-simple - snd_rpi_hifiberry_dac`

    sudo nano /etc/asound.conf

`defaults.pcm.card 0` `заменить цифру, на номер Вашей карты`  
`defaults.ctl.card 0` `заменить цифру, на номер Вашей карты`  

### change image on load system. ONLY BUSTER


    wget -P /tmp https://raw.githubusercontent.com/maltsevvv/maltsev-Kodi-Repo/master/splash/splash.sh
    sudo sh /tmp/splash.sh

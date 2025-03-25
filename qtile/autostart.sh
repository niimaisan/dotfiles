#!/bin/sh

xrandr --output DVI-D-0 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --dpi 96
xset s off
xset -dpms
udiskie &
numlockx &
pkill pasystray
pasystray &
pkill picom
picom &
dunst &
mpd &
feh --bg-fill /home/adroc/pics/wallpapers/1378050.png /home/adroc/pics/wallpapers/1378048.png
flatpak run com.bitwarden.desktop &
flatpak run com.discordapp.Discord &
flatpak run --command=jellyfin org.jellyfin.JellyfinServer &
telegram-desktop &
redshift -l 43.35619:-8.25796 &
rclone --vfs-cache-mode writes mount onedrive: /mnt/data/onedrive &

#!/bin/bash
#
# Slax post-install script for Poli
#
# Author:
#   Schronk Tamás
#
# Description:
#   A post-installation bash script for Ubuntu (13.10)
#
# Based on rougeth[0] script.
# 
# [0] - https://gist.github.com/rougeth/8108714
#
# Usage:
#   $ cd /tmp
#   $ wget http://...
#   $ chmod +x poli_install.sh
#   $ ./poli_install.sh
#
#

# https://stackoverflow.com/a/28709668
function cecho() {
  local code="\033["
  case "$1" in
    black  | bk) color="${code}0;30m";;
    red    |  r) color="${code}1;31m";;
    green  |  g) color="${code}1;32m";;
    yellow |  y) color="${code}1;33m";;
    blue   |  b) color="${code}1;34m";;
    purple |  p) color="${code}1;35m";;
    cyan   |  c) color="${code}1;36m";;
    gray   | gr) color="${code}0;37m";;
    *) local text="$1"
  esac
  [ -z "$text" ] && local text="\n\n$color$2${code}0m\n\n"
  printf "$text"
  sleep 1
}

echo 'Dpkg::Progress-Fancy "1";\nAPT::Color "1";' | tee /etc/apt/apt.conf.d/99progressbar

clear

cecho red "------------------------------------------------------------------------
=> Slax 9.3 post-install script
------------------------------------------------------------------------"

cecho "Bármikor megszakíthatod a 'CTRL+C' -vel"

cecho red "-----------------------------------------------------------------------------
=> Billentyűzet beállítása
-----------------------------------------------------------------------------"
fbsetkb hu
echo "Kész!"


cecho red "-----------------------------------------------------------------------------
=> Rendszer frissítés
-----------------------------------------------------------------------------"

echo '=> Update repository information'
apt-get update -qq | echo -ne
echo '=> Performe system upgrade'
apt-get dist-upgrade -y | echo -ne
echo 'Kész'

cecho red "-----------------------------------------------------------------------------
=> Telepítéshez szükséges eszközök telepítése
-----------------------------------------------------------------------------"

apt-get install -y apt-transport-https dirmngr software-properties-common | echo -ne
echo "Kész"

cecho red "-----------------------------------------------------------------------------
=> Add PPAs (Personal Package Archives)
-----------------------------------------------------------------------------"

add-apt-repository -y "deb https://packages.microsoft.com/repos/vscode stable main"
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB3E94ADBE1229CF
echo '=> Update repository information'
apt-get update -qq | echo -ne
echo "Kész"


cecho red "-----------------------------------------------------------------------------
=> Install developer packages
-----------------------------------------------------------------------------"
apt-get install -y git python3 python3-pip nano code | echo -ne

cecho red "-----------------------------------------------------------------------------
=> Fix VS Code
-----------------------------------------------------------------------------"
sed -i 's/Icon=code/Icon=\/usr\/share\/pixmaps\/code.png/g' /usr/share/applications/code.desktop
sed -i 's/New Empty Window/VS Code/g' /usr/share/applications/code.desktop

echo 'Minden kész!'

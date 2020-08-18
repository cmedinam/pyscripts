#!/bin/bash 

su -c "./install-basic-tools.sh"

chsh -s /bin/zsh

su -c "reboot"


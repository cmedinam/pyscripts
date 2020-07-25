#!/bin/zsh

./install-extend-tools.sh

su -c "./installers/install-S11powerline.sh"

./configure-extend-tools.sh

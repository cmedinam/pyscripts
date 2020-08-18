#!/bin/bash

tm_color='\033[0;33m'
if_color='\033[1;36m'
reset_color='\033[0m'

pr(){
	echo -e "[ ${tm_color}$(date)${reset_color} ] > ${if_color}$1${reset_color}"
}
if [[ UID -ne 0 ]]; then
	pr "Run this script as root"
else
	if [[ -z $(which tmux) ]]; then
		apt-get install -y  tmux
	else
		pr "Tmux already installed!"
	fi

	if [[ -z $(which zsh) ]]; then
		apt-get install -y  zsh
	else
		pr "zSh already installed!"
	fi

	if [[ -z $(which curl) ]]; then
		apt-get install -y  curl
	else
		pr "Curl already installed!"
	fi

	if [[ -z $(which git) ]]; then
		apt-get install -y  git
	else
		pr "Git already installed!"
	fi
	
	if [[ -z $(which vim) ]]; then
		apt-get install -y  vim
	else
		pr "Vim already installed!"
	fi

	if [[ -z $(which pip) ]]; then
		apt-get install -y  python-pip
	else
		pr "Pip for python2 already installed!"
	fi

	if [[ -z $(which pip3) ]]; then
		apt-get install -y  python3-pip
	else
		pr "Pip for python3 already installed1"
	fi

	cp mount-units.sh /etc/init.d/mount-host-units
	ln -s /etc/init.d/mount-host-units /etc/rc2.d/S80mount-host-units
fi


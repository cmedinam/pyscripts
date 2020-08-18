#!/bin/zsh

if [[ $(lsb_release -rs | cut -d "." -f1) -le 14 ]] ; then
	[[ -z $(which pip) ]] && sudo apt-get install python-pip
	pip install git+git://github.com/Lokaltog/powerline
else
	apt-get install powerline
fi

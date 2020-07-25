#!/bin/zsh

if [[ UID -ne 0 ]] ; then
	echo "Please run this script as root"
else
	if [[ $(lsb_release -sc) == 'trusty' ]] ; then
		if [[ -z $(which pip) ]] ; then
			apt-get install python-pip
		fi
		pip install git+git://github.com/Lokaltog/powerline
	else
		apt-get install powerline
	fi
fi

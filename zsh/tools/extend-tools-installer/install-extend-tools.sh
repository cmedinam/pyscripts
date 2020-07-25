#!/bin/bash

tm_color='\033[0;33m'
if_color='\033[1;36m'
reset_color='\033[0m'

pr(){
	echo -e "[ ${tm_color}$(date)${reset_color} ] > ${if_color}$1${reset_color}"
}
if [[ UID -eq 0 ]]; then
	pr "Run this script as NOT root"
else
	pr "Installation Begin!"
	for installer in $(ls ./installers) ; do 
		./installers/$installer
	done
	
	pr "Installation Finished!"
fi


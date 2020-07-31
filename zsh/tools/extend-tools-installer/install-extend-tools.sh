#!/bin/bash

tm_color='\e[0;93m'; 
if_color='\e[0;94m';
reset_color='\e[0m'

pr(){
	echo -e "[ ${tm_color}$(date)${reset_color} ] > ${if_color}$@${reset_color}"
}
if [[ UID -eq 0 ]]; then
	pr Run this script as NOT root
else
	pr Installation Begin!
	for installer in $(ls ./installers) ; do 
		pr "Installing `expr "$installer" : '.*S[0-9]*\(.*\)\.sh'` ..."
		./installers/$installer
		pr "`expr "$installer" : '.*S[0-9]*\(.*\)\.sh'` installation success!"
	done
	
	pr Installation Finished!
fi


#!/bin/bash

tm_color='\e[0;93m'
if_color='\e[0;94m'
reset_color='\e[0m'

pr(){
	echo -e "[ ${tm_color}$(date)${reset_color} ] > ${if_color}$@${reset_color}"
}
if [[ UID -eq 0 ]]; then
	pr "Run this script as NOT root"
else
	pr "Configuration Begin!"
	for configurer in $(ls ./configurers) ; do 
		pr Configuring `expr "$configurer" : '.*S[0-9]*\(.*\)\.sh'` ...
		./configurers/$configurer
		pr `expr "$configurer" : '.*S[0-9]*\(.*\)\.sh'` configuration success!
	done
	pr "Configuration Finished!"
fi


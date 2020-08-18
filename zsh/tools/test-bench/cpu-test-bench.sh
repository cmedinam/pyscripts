#!/bin/zsh

source colors.sh


END_LOOD=0
THREADS=4
OPTIONS=(OP1 OP2 OP3)

console_width (){
  stty -a | grep -Po '(?<=columns )\d+'
}

show_sensor_info (){
  if [[ ! -z $(command -v sensors) ]] ; then
    sep "."
    sensors
  fi
} 

show_installed (){
  echo -n "${BBlu}Checking${RCol} if ${UYel}$1${RCol} is installed ... "
  [[ -z $(command -v $1) ]] && echo -e "${BRed}no" || echo -e "${BGre}yes"
  echo -en "${RCol}"
}

show_installed_tools (){
  sep "."
  for cmd in "stress" "stress-ng" "s-tui" "sysbench" "7z" ; do
    show_installed $cmd
  done
}

sep (){ 
  echo "" 
  for i in $(seq $(console_width)) ; do echo -n "$1"; done
  echo ""
  echo ""
}

current_status (){
  show_sensor_info
  show_installed_tools
  sep "."
}


print_header (){
  sep "~"
  echo -e "${IGre}$1${RCol}"
  sep "~"
}

install_mgn (){
    [[ $# -le 1 ]] && app=$1 || app=$2
    if [[ -z $(command -v $app) ]] ; then
      echo Installing $1
      sudo apt-get install $1
    else
      echo Uninstalling $1
      sudo apt-get remove $1
    fi
}

process_opt (){
  echo -e "${RCol}"
  case $1 in
    "(U)Install stress")
    install_mgn stress
    break ;;
    "(U)Install stress-ng")
    install_mgn stress-ng
    break ;;
    "(U)Install s-tui")
    install_mgn s-tui
    break ;;
    "(U)Install sysbench")
    install_mgn sysbench
    break ;;
    "(U)Install p7zip-full")
    install_mgn "p7zip-full" 7z
    break ;;
    "Run stress")
    stress --cpu $THREADS
    break ;;
    "Run stress-ng")
    stress-ng --cpu $THREADS
    break ;;
    "Run s-tui")
    s-tui
    break ;;
    "Run sysbench")
    sysbench cpu --threads=$THREADS
    break ;;
    "Run p7zip-full")
    7z b
    break ;;
    "Exit")
    echo "Closing application..."
    return 1
    break ;;
    *)
    echo Default selected option
    return 1
    ;;
  esac
}

print_opt_menu (){
  select opt in "${@}"; do
    if [ 1 -le "$REPLY" ] && [ "$REPLY" -le $# ]; then
      # Valid option selected
      process_opt $opt
      return $?
    else
      # Invalid option
      return 0
    fi
  done
}

run_menu (){
  END_LOOP=0
  while [[ $END_LOOP -eq 0 ]]
  do
    # clear
    sep
    echo "TESTER TOOLS MANAGER"
    current_status
    print_header "$1"
    echo -e "${Gre}"
    print_opt_menu "${@:2}"
    END_LOOP=$?
    echo -e "${RCol}"
    sleep 1
  done
}

#echo "TESTER TOOLS MANAGER"
#current_status
run_menu "Testing and Benchmarking Tools"\
 "(U)Install stress"\
 "(U)Install stress-ng"\
 "(U)Install s-tui"\
 "(U)Install sysbench"\
 "(U)Install p7zip-full"\
 "Run stress"\
 "Run stress-ng"\
 "Run s-tui"\
 "Run sysbench"\
 "Run p7zip-full"\
 "Exit"

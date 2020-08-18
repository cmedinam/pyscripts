#!/bin/zsh

END_LOOD=0

OPTIONS=(OP1 OP2 OP3)

print_header (){
  echo "------------------------------"
  echo $1
  echo "------------------------------"
}

process_opt (){
  case $1 in 
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
      echo Valid option selected: $opt
      process_opt $opt
      return $?
    else
      # Invalid option
      echo Invalid option: $opt
      return 0
    fi
  done
}

run_menu (){
  END_LOOP=0
  while [[ $END_LOOP -eq 0 ]]
  do
    clear
    print_header "$1"
    print_opt_menu "${@:2}"
    END_LOOP=$?
    sleep 1
  done
}

run_menu "My Menu" "Option 1" "Option 2" "Option 3"

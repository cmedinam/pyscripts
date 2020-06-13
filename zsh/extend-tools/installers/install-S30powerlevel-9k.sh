#!/bin/zsh

git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

sed -i 's/ZSH\_THEME\=\".*\"/ZSH\_THEME\=\"powerlevel9k\/powerlevel9k\"/g' ~/.zshrc

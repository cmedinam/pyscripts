#!/bin/zsh

if [[ $(lsb_release -rs | cut -d "." -f1) -le 14 ]] ; then 
	git clone https://github.com/bhilburn/powerlevel9k.git $HOME/.oh-my-zsh/custom/themes/powerlevel9k

	sed -i 's/ZSH\_THEME\=\".*\"/ZSH\_THEME\=\"powerlevel9k\/powerlevel9k\"/g' $HOME/.zshrc
else 
	git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

	sed -i 's/ZSH\_THEME\=\".*\"/ZSH\_THEME\=\"powerlevel10k\/powerlevel10k\"/g' $HOME/.zshrc
fi

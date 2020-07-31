#!/bin/zsh
echo "#!/bin/zsh" > $HOME/.vimrc
echo -n "Expected powerline on " 
if [[ $(lsb_release -rs | cut -d "." -f1) -le 14 ]]; then
	pwline=/usr/local/lib/python2.7/dist-packages/powerline
	echo "$pwline"
else
	pwline=/usr/share/powerline
	echo "$pwline"
fi

echo "set rtp+=$pwline/bindings/vim/" >> $HOME/.vimrc
echo "\" Always show statusline" >> $HOME/.vimrc
echo "set laststatus=2" >> $HOME/.vimrc
echo "\" Use 256 colours (Use this setting only if your terminal supports 256 colours)" >> $HOME/.vimrc
echo "set t_Co=256" >> $HOME/.vimrc

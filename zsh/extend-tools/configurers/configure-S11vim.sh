#!/bin/zsh
echo "#!/bin/zsh" > ~/.vimrc
echo -n "Expected powerline on " 
if [[ $(lsb_release -sc) == 'trusty' ]]; then
	pwline=/usr/local/lib/python2.7/dist-packages/powerline
	echo "$pwline"
else
	pwline=/usr/share/powerline
	echo "$pwline"
fi

echo "set rtp+=$pwline/bindings/vim/" >> ~/.vimrc
echo "\" Always show statusline" >> ~/.vimrc
echo "set laststatus=2" >> ~/.vimrc
echo "\" Use 256 colours (Use this setting only if your terminal supports 256 colours)" >> ~/.vimrc
echo "set t_Co=256" >> ~/.vimrc

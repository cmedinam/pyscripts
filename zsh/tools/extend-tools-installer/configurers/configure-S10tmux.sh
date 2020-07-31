#!/bin/zsh
echo "#!/bin/zsh" > $HOME/.tmux.conf
echo "TERM=screen-256color" >> $HOME/.tmux.conf
echo "set-option -g default-terminal \$TERM" >> $HOME/.tmux.conf
echo -n "Expected powerline on " 
if [[ $(lsb_release -rs | cut -d "." -f1) -le 14 ]]; then
	pwline=/usr/local/lib/python2.7/dist-packages/powerline
	echo "$pwline"
else
	pwline=/usr/share/powerline
	echo "$pwline"
fi

echo "source $pwline/bindings/tmux/powerline.conf" >> $HOME/.tmux.conf

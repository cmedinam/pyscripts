#!/bin/zsh
echo "#!/bin/zsh" > ~/.tmux.conf
echo "TERM=screen-256color" >> ~/.tmux.conf
echo "set-option -g default-terminal \$TERM" >> ~/.tmux.conf
echo -n "Expected powerline on " 
if [[ $(lsb_release -sc) == 'trusty' ]]; then
	pwline=/usr/local/lib/python2.7/dist-packages/powerline
	echo "$pwline"
else
	pwline=/usr/share/powerline
	echo "$pwline"
fi

echo "source $pwline/bindings/tmux/powerline.conf" >> ~/.tmux.conf

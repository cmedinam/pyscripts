#!/bin/zsh

cd $HOME
# Cloramos el repositorio
git clone https://github.com/powerline/fonts.git --depth=1
# Instalamos
cd fonts
./install.sh
# Limpiamos
cd ..
rm -rf fonts

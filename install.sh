#!/bin/bash

read -p "Do you want me to pip,json,magic and telegram-bot ? (yes/no):"

if [ "$REPLY" != "yes" ]; then
	echo " "

 else
 	echo "Update and upgrade apt-get"
	sudo apt-get update && sudo apt-get upgrade
	echo "Installing python pip"
	sudo apt-get install python-pip python-dev build-essential 
	echo "Installing pip upgrade"
	sudo pip install --upgrade pip 
	echo "Installing pip virtualenv"
	sudo pip install --upgrade virtualenv 
	echo "Installing py telebot"
        sudo pip install simplejson
        sudo apt-get install libmagic-dev
        sudo pip install python-magic
        sudo pip install pytelegrambotapi --upgrade
 	echo " "
 +fi

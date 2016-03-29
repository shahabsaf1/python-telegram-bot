if [ "$REPLY" != "yes" ]; then
	echo "
"
else
	echo "Update and upgrade apt-get"
	sudo apt-get update && sudo apt-get upgrade
	echo "Installing python pip"
	sudo apt-get install python-pip python-dev build-essential 
	echo "Installing pip upgrade"
	sudo pip install --upgrade pip 
	echo "Installing pip virtualenv"
	sudo pip install --upgrade virtualenv 
	echo "Installing pip telebot"
        sudo pip install telebot
	echo " "
fi

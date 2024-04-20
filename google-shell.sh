#!/bin/bash
cd $HOME
echo "Made by @sanatani_x_anonymous"
echo "Telegram:-https://t.me/temuxhacking"
apt update
apt install curl python openssh openssl -y

curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-470.0.0-linux-arm.tar.gz
echo "Decompressing Google Cloud SDK file"
tar -xvzf google-cloud-cli-470.0.0-linux-arm.tar.gz
echo "Adding the gcloud CLI to your path"
sleep 2 
echo "If Question Asked Just Hit Enter"
sleep 5
./google-cloud-sdk/install.sh
echo "Initializing the gcloud CLI"
./google-cloud-sdk/bin/gcloud init

echo "alias google='gcloud alpha cloud-shell ssh'" >> .bashrc
clear
echo "Now exit and reopen your Termux, then type 'google' to start Google shell" 
sleep 7
exit

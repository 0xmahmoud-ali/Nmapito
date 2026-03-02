#!/bin/bash

BLUE='\033[94m'
GREEN='\033[92m'
END='\033[0m'

echo -e "${BLUE}Installing System Requirements for Nmapito${END}"


# Update the system
sudo apt-get update

#Install Nmap
echo "Installing Nmap"
sudo apt-get install nmap -y

#Install Nikto
echo "Installing Nikto"
sudo apt-get install nikto -y

#Done
echo "installation is finished and now you can run: python3 nmapito.py"

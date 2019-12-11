#!/bin/bash
# A small Bash script to copy and change permission of project.cgi

echo "Copying switch.cgi to /usr/lib/cgi-bin/"
sudo cp switch.cgi /usr/lib/cgi-bin/
echo "Adding s permission to switch"
sudo chmod +s /usr/lib/cgi-bin/switch.cgi

#!/bin/bash

#This script is used to install the Planning Center Checkout Page app onto a Mac.

#Create the directory for the app to live
mkdir /Library/WebServer/PlanningCenterCheckoutPage
cp -a WebFiles/. /Library/WebServer/PlanningCenterCheckoutPage

#Setup launcing app on startup
cp ./local.planningCenterCheckout.plist /Library/LaunchAgents/local.planningCenterCheckout.plist

#Move to the application directory
cd /Library/WebServer/PlanningCenterCheckoutPage

#Create the virtual python environment
/usr/bin/python3 -m venv PCCPVENV
source ./PCCPVENV/bin/activate
pip3 install Flask
pip3 install requests
pip3 install simplejson

shutdown -r now

# Planning Center Checout Page
This app can be used to create a ProPresenter Prop to overlay checkout information from planning center on top of what you are displaying on your screen.

## Installation Instructions
1. Clone the git repo onto your computer. ```git clone https://github.com/CBC-LSM/PlanningCenterCheckoutPage.git```
3. In terminal type ```mv WebFiles/config_template.py WebFiles/config.py```
4. Open config.py in your favorite text editor and enter your planning center API keys into the configuration file.
5. In terminal, run
```
chmod 755 MacOS_Install.sh
sudo ./MacOS_Install.sh
```
6. Your computer will restart
7. Create a new prop in ProPresenter
8. Add a webpage object pointed at http://127.0.0.1:8005

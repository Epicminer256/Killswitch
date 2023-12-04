# Killswitch

Breaks Securly via custom Chrome app

![Killswitch Logo](icons/144x144.png)

# For users who got it installed already

If you clear your browser cache, the program gets essentually wiped off the app. If you clear your cookies you just have to re-enable killswitch.

# Wanna deploy?

### Setup on windows:
1. Make venv with `python -m venv .`
2. Install dependencies for epicdnschef and install flask

### Running on Windows:
- Target Machine
    1. On target machine, goto `chrome://flags` and goto `Unsafely treat insecure origins as secure`
    2. Add `http://toggle.securly.com` to the list and hit `Restart`
- Windows Distribution Machine
    1. Turn on your mobile hotspot (changing the network name and password is recommended)
    2. Open `start_hotspot.bat` and leave the amount of days blank
- Back at the Target Machine
    1. Have target machine connect to WiFi network
    2. Install PWA from website (if this doesn't work, check if the command prompts updated or not)
    3. After install, right-click the Google app and look for "Killswitch"
    4. After opening, it installs itself and you can now disconnect from the hotspot. Also make sure to click `Disable Securly` on the way

### If you are on GNU/Linux (for the wierdo nerd setups):
- Target Machine
    1. On target machine, goto `chrome://flags` and goto `Unsafely treat insecure origins as secure`
    2. Add `http://toggle.securly.com` to the list and hit `Restart`
- Linux Distribution Machine
    1. Connect to a WiFi/hotspot that allows for http and dns servers
        - Personal hotspots are perfered
        - Some networks that may not work are business or school networks due to firewalls on ports 
    2. Open `start_regular.sh` and type in your server IP (found with `ip a`), then leave the amount of days blank
- Back at the Target Machine
    1. Have target machine connect to WiFi network
    2. Have target machine's DNS server the same as the server's ip
    3. Install PWA from website (if this doesn't work, check if the command prompts updated or not)
    3. After install, right-click the Google app and look for "Killswitch"
    4. After opening, it installs itself and you can now disconnect from the hotspot. Also make sure to click `Disable Securly` on the way

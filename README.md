# Rustplus-Alarm
A python program that is able to light up an LED if a Smart Alarm is triggered in the game Rust. 
Python Libraries used in this Project: 
  -RPi.GPIO
  -Time
  -asyncio 
  -os
  -rustplus

Steps to it work: 
1. connect LED to Raspberry PI / Arduino
2. Get SteamID (Copy via Steam)
3. Get Rust Server IP (Can check via the Rust Console)
4. Get PlayerToken (Check with Rustplus Chrome Addon https://chromewebstore.google.com/detail/rustpluspy-link-companion/gojhnmnggbnflhdcpcemeahejhcimnlf?pli=1)
5. Get EntityID (Place and connect the smart Alarm)
6. Pair it with the Rust+ App while using the Chrome addon.
7. Copy EntityID and all other info into the server details section in Rust+API.py
8. Copy the LEDLoop.py and Rust+API.py to the Raspberry PI
9. Create a virtual environment to install all needed libraries
10. In the virtual environment type: python Rust+APi.py

🚨 Rustplus-Alarm

A Python program that lights up an LED on a Raspberry Pi or Arduino when a Smart Alarm is triggered in the game Rust, using the Rust+ Companion API.

🧰 Libraries Used
    
    RPi.GPIO
    time
    asyncio
    os
    rustplus

🔧 Setup Instructions
    
    Connect an LED to your Raspberry Pi / Arduino.
    
    Get your SteamID
    📋 (Right-click your profile in Steam → Copy Page URL → Grab the number)

    Get the Rust server IP
    📡 (Join the server → Open the Rust console → Use player.ip or look at logs)

    Get your Player Token
    🔐 Use the Rust+ Chrome Addon

    Get the EntityID of your Smart Alarm
    📱 Place and pair your alarm using the Rust+ app and Chrome addon

   Create a virtual environment:
      python3 -m venv venv
      source venv/bin/activate

  Install dependencies (Inside your virtual environment)
      pip install rustplus RPi.GPIO

  Run the Script:
      python Rust+API.py

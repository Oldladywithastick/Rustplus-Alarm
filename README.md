# 🚨 Rustplus-Alarm

A Python program that lights up an LED on a Raspberry Pi or Arduino when a Smart Alarm is triggered in the game Rust, using the Rust+ Companion API.

---

## 🧰 Libraries Used

- `RPi.GPIO`
- `time`
- `asyncio`
- `os`
- `rustplus`

---

## 🔧 Setup Instructions

1. **Connect** an LED to your Raspberry Pi / Arduino.

2. **Get your SteamID**  
   📋 Right-click your profile in Steam → Copy Page URL → Grab the number

3. **Get the Rust server IP**  
   📡 Join the server → Open the Rust console → Use `player.ip` or check logs

4. **Get your Player Token**  
   🔐 Use the [Rust+ Chrome Addon](https://chromewebstore.google.com/detail/rustpluspy-link-companion/gojhnmnggbnflhdcpcemeahejhcimnlf?pli=1)

5. **Get the EntityID** of your Smart Alarm  
   📱 Place and pair your alarm using the Rust+ app and the Chrome addon

6. **Configure** `Rust+API.py` with your:
   - `SteamID`
   - `PlayerToken`
   - `EntityID`

---

## 🛠️ Setting Up & Running

### 1. Create a virtual environment, Install dependencies and run the Script
```bash
python3 -m venv venv
source venv/bin/activate

2. Install dependencies (inside the virtual environment)

   pip install rustplus RPi.GPIO

3. Run the Script
   python3 Rust+API.py

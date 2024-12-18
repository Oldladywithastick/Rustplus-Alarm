#Use RUstplus on Github Chrome addon to receive info
import asyncio
import os  #Needed for LEDLoop.py
from rustplus import RustSocket, ServerDetails #Rustplus Library from Github, you need a virtual environment

#trigger LEDLoop.py
def trigger_led_loop():
    print("Alarm detected! Activating LEDLoop.py...")
    os.system("python3 LEDLoop.py")

#Wait for successfull socket connection with provided details. 
async def check_rust_alarm():
    server_details = ServerDetails("154.6.138.33", "28082", 76561199084429057, -1924586762) #Example ServerIP, ServerPort (28082 is default), SteamID, Playertoken. (Check with Chrome Addon)
    socket = RustSocket(server_details)
    await socket.connect()

    try:
        entity_info = await socket.get_entity_info(371824932) #Enter entitity ID (Check with chrome addon or Rust Combatlog)
        alarm_triggered = entity_info.value  # Save entity value to later check 
        
        print(f"Entity Info: {entity_info}") #Outprint entity info with value

        # Check if Value changed and smart alarm was therefore triggered
        if alarm_triggered: #If true, LEDLoop.py gets triggered 
            trigger_led_loop()
        else:
            print("No alarm detected.")
    except Exception as e:
        print(f"Error fetching entity info: {e}")
    finally:
        await socket.disconnect()

#Loop
async def main():
    while True:
        await check_rust_alarm()
        await asyncio.sleep(3)  #Check for Alarm detection every 3 sec. Chan change for your liking

# Run the program
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated by user.")

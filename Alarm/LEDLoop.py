import RPi.GPIO as GPIO #GPPIO Library to use Pins on Raspberry or Arduino
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #Change to your connected PIN
start_time = time.time()
while time.time() - start_time < 20: #Change Number to your desired LEDLoop.py length
    print("Loop is running")
    GPIO.output(18, True)
    time.sleep(0.5)#Make it blink faster by changing both time values
    GPIO.output(18, False)
    time.sleep(0.5) 

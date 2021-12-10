
from phue import Bridge
import time
import RPi.GPIO as GPIO
from hue_control import turn_on_off_event


# broadcome
GPIO.setmode(GPIO.BCM)
# input pin
pin = 24
# setup input
GPIO.setup(pin, GPIO.IN)
BRIDGE_IP = 'YOUR_BRIDGE_IP'

b = Bridge(BRIDGE_IP)


def callback(pin):
    """Define what happens when detected"""

    if GPIO.input(pin):
        turn_on_off_event(b)
    else:
        turn_on_off_event(b)


GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(pin, callback)

print('Detection is on...')

while True:
    time.sleep(5)

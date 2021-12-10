## ABOUT

This program uses RaspberryPi sound/noise sensor (peeks like **claps** or **snaps**) to ON/OFF Phillips Hue lights (connected to Hue Bridge)
<br /> 
<br />

## WHAT IS NEEDED

1. RaspberryPi (following project was performed with use of RaspberryPi Zero WH)
2. Sensors:
    - Sound/Noise sensor (cheapest 3 pin 5V) (*[**example 'How to set sound/noise sensor'**](https://www.instructables.com/Using-a-sound-sensor-with-a-Raspberry-Pi-to-contro/)*)
3. Hue Bridge and light
<br />

## INSTALLATION

If your sensor is connected and RaspberryPi is set:
1. In RaspberyPi terminal type:
    - **pip3 install Adafruit_DHT**
    - **pip3 install phue**

2. In *hand_clap_on_off.py* set value of:
    - **pin** - pin which you used to connect sensor to Raspberry Pi
    - **BRIDGE_IP** - your heu bridge ip
<br />

## HOW TO

1. Run ***hand_clap_on_off.py***
2. Clap your hands to turn ON/OFF lights
<br />


## ADDITIONALLY

1. Phillips hue light is controlled with use of light's name. In order to change that variable go to **hue_control.py**.
2. You may change sensitivity of the sensor using its potentiometer (hardware)
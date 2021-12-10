from phue import Bridge


def turn_on_off_event(b, name: str):
    """Turn on or off light
    Parameter:

    b -> bridge

    name -> name of lights"""

    b.connect()
    lights = b.get_light_objects('name')
    # boolen
    if lights[name].on:
        lights[name].on = False
    else:
        lights[name].on = True


def main():
    BRIDGE_IP = 'YOUR_BRIDGE_IP'

    b = Bridge(BRIDGE_IP)
    light_name = 'desk'
    turn_on_off_event(b, light_name)


if __name__ == '__main__':
    main()

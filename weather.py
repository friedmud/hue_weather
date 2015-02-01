#!/usr/bin/env python

import time
import pyowm
from phue import Bridge
from hue_rgb import Converter

from config import *

owm = pyowm.OWM()
current_status = ''
previous_status = ''

b = Bridge(HUE_ADDRESS)
b.connect()

converter = Converter()

low_temp = False

color_changed_time = 0

def changeLightColor(lights, rgb_color):
    global color_changed_time
    color_changed_time = time.time()
    for l in lights:
        l.xy = converter.rgbToCIE1931(rgb_color[0], rgb_color[1], rgb_color[2])

while True:
    lights = b.lights

    observation = owm.weather_at_id(OWM_CITY_ID)
    w = observation.get_weather()

    temp = w.get_temperature('fahrenheit')['temp']
    current_status = w.get_status()

    print 'Temperature:', temp
    print 'Status:', current_status

    # Is it time to refresh the color?
    time_to_refresh = time.time() - color_changed_time > REFRESH_TIME

    print "Time to refresh:", time_to_refresh

    if temp < LOW_TEMP and not low_temp:
        if time_to_refresh:
            print 'Low temperature!'
            low_temp = True
            changeLightColor(lights, colors["low_temp"])
    else:
        low_temp = False

    if current_status != previous_status or time_to_refresh:
        print 'Weather changed to:', current_status

        previous_status = current_status

        # If there is a defined color for this status: change it
        if current_status in colors:
            changeLightColor(lights, colors[current_status])

    time.sleep(SLEEP_TIME)

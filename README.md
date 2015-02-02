# Hue Weather

Control your Philips Hue lights based on the weather

## Why?

I was frustrated by the lack of options when using IFTTT.  In particular the "Change Color" outputs on IFTTT would _also_ turn on the lights: meaning that if it started snowing in the middle of the night then all of the lights in my house would come on... genius!

## What?

This is simple for now.  It uses [Open Weather Maps](http://openweathermap.org) to get the current conditions for one place and then changes the color of your Hue lights based on your preferences.

## How?

### Dependencies

To get it up and running you'll need a few libraries:

If you don't have pip:

```bash
sudo easy_install pip
```

Then...

```bash
sudo pip install phue
sudo pip install pyowm
```

### Open Weather Map

You'll need to [sign up for Open Weather Map](http://openweathermap.org/register) and get your very open application Key (you'll use that in a moment).

### Clone

Clone the repository from Github...

### config.py

The next thing you'll need is to create a `config.py` file inside your clone.  You'll need your OWM key, your IP address for your Hue Bridge and the ID of the city's weather you want to track from OWM.

```python
# Hue bridge IP address
HUE_ADDRESS = '192.168.1.2'

# Open Weather Map Personal Key
OWM_KEY = 'YOUR OPEN WEATHER MAP ID'

# Open Weather Map ID for the city
OWM_CITY_ID = 4929180

# Time between updates (seconds)
SLEEP_TIME = 900

# Time between refreshing for the same weather status (seconds)
REFRESH_TIME = 2695

# Temperature to trigger the low temperature color
LOW_TEMP = 20 # F

# R, G, B values
colors = {
    "low_temp" : [31, 55, 209],
    "snow" : [213, 44, 222],
    "rain" : [44, 222, 65],
    "clouds" : [0, 251, 255],
    "extreme" : [222, 44, 44]
}
```

## Use...
Just run `weather.py`

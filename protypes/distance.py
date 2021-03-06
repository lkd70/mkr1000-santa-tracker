import json
import math
import sys

leds = [
    {'name': 'North Pole', 'location': {'lat': 90.0, 'lng': 30.0}},
    {'name': 'Alaska (US)', 'location': {'lat': 64.536117, 'lng': -151.258768}},
    {'name': 'Alberta (Canada)', 'location': {'lat': 48.9202307, 'lng': -93.69738}},
    {'name': 'Ontario (Canada)', 'location': {'lat': 50.956252, 'lng': -87.369255}},
    {'name': 'Utah (US)', 'location': {'lat': 40.7765868, 'lng': -111.9905244}},
    {'name': 'Tennessee (US)', 'location': {'lat': 36.1865589, 'lng': -86.9253274}},
    {'name': 'Mexico City (Mexico)', 'location': {'lat': 19.39068, 'lng': -99.2836957}},
    {'name': 'Bogota (Columbia)', 'location': {'lat': 4.6482837, 'lng': -74.2478905}},
    {'name': 'Brasilia (Brazil)', 'location': {'lat': -15.721751, 'lng': -48.0082759}},
    {'name': 'Santiago (Chile)', 'location': {'lat': -33.4727092, 'lng': -70.7699135}},
    {'name': 'Greenland', 'location': {'lat': 70.8836652, 'lng': -59.6665893}},
    {'name': 'UK', 'location': {'lat': 64.6748061, 'lng': -7.9869018}},
    {'name': 'Spain', 'location': {'lat': 40.4379332, 'lng': -3.749576}},
    {'name': 'Mali', 'location': {'lat': 17.5237416, 'lng': -8.4791157}},
    {'name': 'Finland', 'location': {'lat': 64.6479136, 'lng': 17.1440256}},
    {'name': 'Greece', 'location': {'lat': 38.2540419, 'lng': 21.56707}},
    {'name': 'Libya', 'location': {'lat': 21.520733, 'lng': 23.237173}},
    {'name': 'Central African Republic', 'location': {'lat': 6.2540984, 'lng': -0.2809593}},
    {'name': 'Botswana', 'location': {'lat': -22.327399, 'lng': 22.4437318}},
    {'name': 'Saudi Arabia', 'location': {'lat': 24.0593214, 'lng': 40.6158589}},
    {'name': 'Turkmenistan', 'location': {'lat': 38.9423384, 'lng': 57.3349508}},
    {'name': 'Xinjiang (China)', 'location': {'lat': 42.0304225, 'lng': 77.3185349}},
    {'name': 'India', 'location': {'lat': 20.8925986, 'lng': 73.7613366}},
    {'name': 'Henan (China)', 'location': {'lat': 33.8541479, 'lng': 111.2634555}},
    {'name': 'Cambodia', 'location': {'lat': 12.2978202, 'lng': 103.8594626}},
    {'name': 'Japan', 'location': {'lat': 34.452585, 'lng': 125.382845}},
    {'name': 'Australia', 'location': {'lat': -25.0340388, 'lng': 115.2378468}},
    {'name': 'New Zealand', 'location': {'lat': -43.0225411, 'lng': 163.4767905}},
    {'name': 'South Pole', 'location': {'lat': -90.0, 'lng': 30.0}},
]


def distance(loc1, loc2, unit='M'):
    lat1 = loc1['lat']
    lng1 = loc1['lng']
    lat2 = loc2['lat']
    lng2 = loc2['lng']

    radlat1 = math.pi * lat1 / 180
    radlat2 = math.pi * lat2 / 180
    theta = lng1-lng2
    radtheta = math.pi * theta / 180
    dist = (math.sin(radlat1) * math.sin(radlat2) +
        math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta));
    dist = math.acos(dist)
    dist = dist * 180 / math.pi
    dist = dist * 60 * 1.1515
    if unit == 'K':
        return dist * 1.609344

    if unit == 'N':
        return dist * 0.8684

    return dist


def closest_led(loc):
    min_dist = sys.float_info.max
    min_led = None
    for led in leds:
        led_loc = led['location']
        dist = distance(loc, led_loc)
        if dist < min_dist:
            min_dist = dist
            min_led = led
    return min_dist,min_led



with open('santa2016.json') as data_file:
    data = json.load(data_file)

dest = []

for dest_json in data['destinations']:
    # dest.append({
    #     'city': dest_json['city'],
    #     'location': dest_json['location']
    #     })
    dist, led = closest_led(dest_json['location'])
    print u'city:{0} loc:{1} led:{2} led-loc:{3} dist:{4}'.format(
        dest_json['city'],
        dest_json['location'],
        led['name'],
        led['location'],
        dist)


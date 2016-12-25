import smbus
import time
import requests
import json

bus = smbus.SMBus(1)
# write to register in order to start reading values
bus.write_byte(0x48, 0x00)
url = 'http://smartclub.herokuapp.com/sendtunes'
amplitudes = [] 

while True:
    reading = bus.read_byte(0x48)
    amplitudes.append(reading)
    # POST the last 10 amplitudes and then reset the list 
    if len(amplitudes) == 10:
        payload = {'music': amplitudes}
        resp = requests.post(url, data={'music': json.dumps(amplitudes)})
        if (resp.status_code == 200):
            # reset amplitudes 
            amplitudes = []
        else:
            print resp.text
            break 
    time.sleep(0.5) 

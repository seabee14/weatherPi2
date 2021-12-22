#!/usr/bin/python3

import BlynkLib
from sense_hat import SenseHat
import time

BLYNK_AUTH = '7amAdO3tAsdDs_S_jH8BgMQwCLdz-QJ9'

# initialize Blynk
blynk = BlynkLib.Blynk('7amAdO3tAsdDs_S_jH8BgMQwCLdz-QJ9')

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# register handler for virtual pin V1 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()

#tmr_start_time = time.time()
# infinite loop that waits for event
while True:
    blynk.run()
    blynk.virtual_write(1, round(sense.temperature,2))  # writing temp data to pin 1
    blynk.virtual_write(2, round(sense.humidity,2))     # writing humity data to pin 2
    blynk.virtual_write(3, round(sense.pressure,2))     # writing pressure data to pin 3
    time.sleep(1)
# main.py -- put your code here!
# main.py -- put your code here!
import pyb
from pyb import Pin

voice = Pin('PE2',Pin.IN)
light = Pin('PE3',Pin.IN)
led = pyb.Pin("PE4",pyb.Pin.OUT_PP)

while 1:
    if light.value()==1:
        if voice.value()==1:
            led.value(0)    
        else:
            led.value(1)
            pyb.delay(5000)
    else:
        led.value(0)
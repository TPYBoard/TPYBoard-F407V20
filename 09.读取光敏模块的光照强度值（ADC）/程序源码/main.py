# main.py -- put your code here!
import pyb
from pyb import ADC,Pin
adc = ADC(Pin('PA1'))

while True:
    print(adc.read())
    pyb.delay(2000)
 
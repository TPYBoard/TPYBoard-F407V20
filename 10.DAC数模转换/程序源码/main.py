# main.py -- put your code here!
import pyb
from pyb import DAC
#----------DAC--------------#
dac = DAC(1, bits=12)   #PA4 pin
dac.write(4095)

dac2 = DAC(2, bits=12)  #PA5 pin
dac2.write(2048)


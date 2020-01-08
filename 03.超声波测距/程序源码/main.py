import pyb
from pyb import Pin
from pyb import Timer
import upcd8544
from machine import SPI,Pin
Trig = Pin('PE2',Pin.OUT_PP)
Echo = Pin('PE3',Pin.IN)
num=0
flag=0
run=1
def start(t):
    global flag
    global num
    if(flag==0):
        num=0
    else:
        num=num+1
def stop(t):
    global run
    if(run==0):
        run=1
start1=Timer(1,freq=10000,callback=start)
stop1=Timer(4,freq=2,callback=stop)

while True:
    if(run==1):
        SPI = pyb.SPI(1)
        RST    = pyb.Pin('PB8')
        CE     = pyb.Pin('PB6')
        DC     = pyb.Pin('PB7')
        LIGHT  = pyb.Pin('PB9')
        lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
        Trig.value(1)
        pyb.udelay(100)
        Trig.value(0)
        while(Echo.value()==0):
            Trig.value(1)
            pyb.udelay(100)
            Trig.value(0)
            flag=0
        if(Echo.value()==1):
            flag=1
            while(Echo.value()==1):           
                flag=1
        if(num!=0):
            #print('num:',num)
            distance=num/10000*34299/2
            print('Distance')
            print(distance,'cm')
            lcd_5110.lcd_write_string('Distance',0,0)
            lcd_5110.lcd_write_string(str(distance),0,1)
            lcd_5110.lcd_write_string('cm',58,1)
            lcd_5110.lcd_write_string('This is a test of F407',0,2)
        flag=0
        run=0
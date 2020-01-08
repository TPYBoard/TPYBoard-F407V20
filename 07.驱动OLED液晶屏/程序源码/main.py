import pyb
from ssd1306 import SSD1306


display = SSD1306(pinout={'dc': 'PB7',
                          'res': 'PB8'},
                  height=64,
                  external_vcc=False)

display.poweron()
display.init_display()
display.draw_text(1,1,'Hello EveryOne',size=1,space=1)
display.draw_text(1,10,'Micropython F407',size=1,space=1)
display.draw_text(1,20,'Let Us Do it',size=1,space=1)
# 显示出你想要显示的内容
display.display()
 
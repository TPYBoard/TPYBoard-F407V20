import pyb
from pyb import UART
 
#����HC-05/06����ģ�����ӵĴ���
#���ڱ��6 ������9600 �շ����ݳ�ʱʱ��100ms
uart = UART(6,9600,timeout=100)

while True:
    #�жϴ��ڻ������Ƿ�������
    if uart.any() > 0:
        #��ȡȫ������,���ص���bytes
        data = uart.read()
        #�ֽ�����ת�ַ���
        id = data.decode()
        #�ַ���ת����
        id = int(id)
        #���ص�LED�����1 or 2���ж������Ƿ���ϣ���ֹ�����쳣
        if id == 1 or id == 2:
            pyb.LED(id).toggle()
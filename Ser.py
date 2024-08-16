import string
import time

import serial

'''
@description:               串口类
@param {string} port        串口号
@param {int}    baudrate    波特率
@param {float}  timeout     超时时间
'''
class Ser(object):
    """
    @description:               初始化函数
    @param {string} port        串口号
    @param {int}    baudrate    波特率
    @param {float}  timeout     超时时间
    """
    def __init__(self, port: string, baudrate: int = 9600, timeout: float = 0.5):
        self.port = port
        self.baurdate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.isopen()

    """
    @description: 确认串口是否打开
    """
    def isopen(self):
        if self.ser.isOpen():
            print("open %s success" % self.port)
        else:
            self.ser.close()
            print("open %s failed" % self.port)
        return self.ser.isOpen()

    """
    @description: 接收数据
    """
    def receive_data(self):
        datas = ''
        while True:
            data = self.ser.read()
            # 没读到就接着尝试读，读到了就退出循环并return读取到的内容
            if data =='':
                continue
            elif data == b'\n':
                break
            else:
                datas += data.decode('utf-8')

        return datas

    """
    @description:           发送数据
    @param {string} data    发送的数据
    """
    def send_data(self, data: string):
        self.ser.write(data.encode('utf-8'))

    """
    @description:           发送并接受数据
    @param {string} data    发送的数据
    """
    def send_and_receive(self, data: string):
        self.ser.write(data.encode('utf-8'))
        time.sleep(0.1)
        count = self.ser.in_waiting
        if count>0:
            data = self.ser.read(count)
            return data


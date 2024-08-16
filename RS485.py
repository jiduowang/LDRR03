import binascii
import string
import time

import crcmod

from Ser import Ser

'''
@description:           RS485类，继承Ser类
@param {string} port    接口
@param {int} baudrate   波特率
'''
class RS485(Ser):
    """
    @description:           RS485类，继承Ser类
    @param {string} port    接口
    @param {int} baudrate   波特率
    """

    def __init__(self, port: string, baudrate: int):
        super().__init__(port, baudrate)

    """
    @description:           发送数据
    @param {string} data    需要发送的数据（十六进制表示）
    """
    def send_data(self, data: string):
        data = bytes.fromhex(data)
        self.ser.write(data)

    """
    @description:                   接受数据
    @return {string} decoded_data   已解码的接收的数据
    """
    def receive_data(self):
        time.sleep(0.05)    #ensure all data input buffer
        data = self.ser.read_all()
        hex_data = binascii.hexlify(data)
        decoded_data = hex_data.decode('utf-8')
        return decoded_data

    """
    @description:                       发送并接受数据
    @param  {string}    data            发送的数据
    @return {string}    decoded_data    已解码的接收的数据
    """
    def send_and_receive(self, data: string):
        hex_data = bytes.fromhex(data)
        self.ser.write(hex_data)
        time.sleep(0.05)
        receive_data = self.ser.read_all()
        hex_receive_data = binascii.hexlify(receive_data)
        decoded_data = hex_receive_data.decode('utf-8')
        return decoded_data

    """
    @description                    crc16检验
    @param {string} data            需要进行crc检验16进制的字符串
    @param {string} result_data     crc校验码    
    """
    def crc_dig(self, data):
        byte_data = bytes.fromhex(data)
        crc_func = crcmod.predefined.mkPredefinedCrcFun("modbus")
        crc_data = crc_func(byte_data)
        result_data = format(crc_data, '04X')

        return ' '+result_data[2:]+' '+result_data[:2]


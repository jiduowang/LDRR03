import time

import string

from RS485 import RS485

class LDRR03(RS485):
    def __init__(self, port: string):
        super().__init__(port, 115200)
        self.read_distance_cm = '01 03 00 00 00 01'
        self.read_distance_mm = '01 03 00 01 00 01'
        self.read_db = '01 03 00 04 00 01'
        self.read_max_distance = '01 03 07 D4 00 01'
        self.set_max_distance = '01 06 07 D4 00'
        self.read_power = '01 03 07 D7 00 01'
        self.max_power = '01 06 07 D7 00'

    def receive_data_process(self, receive_data: string):
        hex_data = ''

        return None


    def get_distance(self, unit: str):
        if unit == 'cm':
            get_instruct = '01 03 00 00 00 01'
            get_instruct += self.crc_dig(get_instruct)

        elif unit == 'mm':
            get_instruct = '01 03 00 01 00 01'
            get_instruct += self.crc_dig(get_instruct)

        else:
            print('unit is error')
            return None

        data = self.send_and_receive(get_instruct)
        hex_data = ''

        for i in range(2*int(data[4:6],16)):
            hex_data+=data[6+i]
        result_data = int(hex_data,16)
        print("距离为" + str(result_data) + unit)
        return result_data

    def get_db(self):
        get_instruct = '01 03 00 04 00 01'
        get_instruct += self.crc_dig(get_instruct)

        data = self.send_and_receive(get_instruct)

        hex_data = ''

        for i in range(2 * int(data[4:6], 16)):
            hex_data += data[6 + i]
        result_data = int(hex_data, 16)

        print("信号强度为" + str(result_data) + "db")

        return result_data



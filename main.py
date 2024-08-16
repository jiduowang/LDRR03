import time

import pandas as pd

from LDRR03 import LDRR03

if __name__ == '__main__':
    lidar = LDRR03("COM4")
    i = 0
    data_arr = []
    while True:
        i += 1
        data = lidar.get_distance('mm')
        data_arr.append(data)
        time.sleep(0.1)
        print(i)
    name = ['data']
    test = pd.DataFrame(data=data_arr, columns=name)
    test.to_csv('data.csv')
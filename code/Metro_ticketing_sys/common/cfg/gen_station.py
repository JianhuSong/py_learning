#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自动生成15条地铁线路,每天线上的站点数量是随机的（10~20）
import random

def gen_station():
    name = [chr(x) for x in range(97,112)]
    num = list(range(1,20))
    info = ''
    with open('station_test.txt','a') as fp:
        for i in range(15):
            info += f'\n{i+1}:'
            for j in range(20):
                info += f'{name[i]}{str(j + 1)}' if j == 19 else f'{name[i]}{str(j + 1)}-'
        fp.writelines(info)
if __name__ == '__main__':
    gen_station()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 有关站点的配置全部在这里
# 采用list来存放站点信息
# 首先从文件中读取站点信息
# 站点信息的格式为：（出现的标点符号全是英文状态下的）
# 线号：起点-站点名-...-站点
# 举例：
# 1:站点1-站点2-站点3-...站点22
# 环线的话在所有不重复的站点后，加一个已经存在的站点就行，这个就会被识别成环线

def get_station_info(filename:str):
    all_stations = []
    with open(filename) as fp:
        content = fp.readlines()
        for line in content:
            try:
                station = line.split(':')[1] if line.split(':')[1][-1] != '\n' else line.split(':')[1][:-1]
                all_stations.append(list(station.split('-')))
            except Exception:
                print(f'{line}格式不符合要求，读取下一行')

    return all_stations

if __name__ == '__main__':
    stations = get_station_info('d:/BaiduNetdiskWorkspace/coding/py_learning/code/Metro_ticketing_sys/common/cfg/station_test.txt')
    print(stations)
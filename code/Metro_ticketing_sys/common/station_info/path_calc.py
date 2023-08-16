#!/usr/bin/env python
# -*- coding: utf-8 -*-

import station

all_stations = station.get_station_info('d:/BaiduNetdiskWorkspace/coding/py_learning/code/Metro_ticketing_sys/common/cfg/station_test.txt')

# def find_lines_by_station(sta):
#     ret = []
#     for i,value in enumerate(all_stations):
#         if sta in value:
          
def gen_all_mult_station(stations:list):
    """获取当前所有站点中的所有交汇点

    Args:
        stations (list): 所有站点

    Returns:
        list: 如果有交汇点，返回[('stationname',[line1,line2,...]),...]形式的结果，每个元素的都是一个tuple,元组的第一项是站点名称，
        站点的第二项是一个list，包含所有经过该站点的线路号。
        如果没有交汇点，返回一个空的列表
    """
    print('stations:',stations)
    mult_stations = []
    for i,value in enumerate(stations):
        for sta in value:
            mult_lines   = [i]
            mult_lines.extend(j for j in range(i+1,len(stations)) if sta in stations[j])
            need_append = all(sta != x for (x, _) in mult_stations)
            if len(mult_lines) >= 2 and need_append:
                mult_stations.append((sta,mult_lines))

    return mult_stations

# 获取一条线路上和其它线路的交点
def has_mult_station(line_num, all_mult):
    return [(x,y) for x, y in all_mult if (line_num -1) in y]
   

# 获取交点所在的所有线路号
def get_line_nums_by_sta(sta, all_mult):
    return [(x,y) for x,y in all_mult if x == sta]

# 找到站点所在线路号(最先出现在哪条线路上，那么这个站点就归属于哪个线路)
def get_line_num_by_sta(sta, stas):
    for i,value in enumerate(stas):
        if sta in value:
            return i+1
     
# def calc_path(begin,end):
#     # 找到起点所在的地铁线和站点

if __name__ == '__main__':
    all_mult_sta = gen_all_mult_station(all_stations)
    print('all_mult_station:',all_mult_sta)
    # 求1号线上的交汇站点
    line1_mult_sta = has_mult_station(4,all_mult_sta)
    print(line1_mult_sta)
    
    for sta in line1_mult_sta:
        all_lines = get_line_nums_by_sta(sta,all_mult_sta)
        print(f"sta = {sta}, lines={all_lines}")
    








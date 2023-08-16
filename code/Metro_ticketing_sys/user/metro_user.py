#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 这个是用户购票的界面，面向购票的用户
import time

def welcome():
    print("--------------欢迎使用3000的地铁购票系统--------------")
    print('当前的站点信息:')  # 这里到时候通过获取站点信息
    print('1.购票')
    print('2.退出')
    print('------------------------------------------------------')

def user_sys_main():
    while True:
        welcome()
        options = input()
        if options != '1':
            break
        people_num = input('请输入票据的张树：')
        end_station = input('请输入终点站名称：')

if __name__ == '__main__':
    user_sys_main()


    
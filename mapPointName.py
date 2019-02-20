#!/usr/bin/env
#-*- coding:utf-8 -*-
import requests
import pandas as pd
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
def parse():
    datas = []
    totalListData = pd.read_csv('locs.csv')
    totalListDict = totalListData.to_dict('index')
    for i in range(0, len(totalListDict)):
	datas.append(str(totalListDict[i]['centroidx']) + ',' + str(totalListDict[i]['centroidy']))
    return datas
#GPS转高德经纬度		
def transform(location):
    parameters = {'coordsys':'gps','locations': location, 'key': 'c79e81a7ec10dee4c0bebc3599b01ec1'}
    base = "http://restapi.amap.com/v3/assistant/coordinate/convert"
    response = requests.get(base, parameters)
    answer = response.json()
    return answer['locations']
 #经纬度转地址
def geocode_location(location):
    parameters = {'location': location, 'key': 'c79e81a7ec10dee4c0bebc3599b01ec1'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(base, parameters)
    answer = response.json()
    print "经纬度：" + location + "对应的地址是:" + answer['regeocode']['addressComponent']['district'],answer['regeocode']['formatted_address']#.encode('gbk','replace')
    return answer

#地址转经纬度
def geocode_address(address):
    parameters = {'address': address, 'key': 'c79e81a7ec10dee4c0bebc3599b01ec1'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    print "地址：" + address + "对应的经纬度是:" + answer['geocodes'][0]['location']
    return answer
#指定经纬度添加标签
def makers_location(location):
	parameters = {'location': location, 'key': 'c79e81a7ec10dee4c0bebc3599b01ec1'}

if __name__=='__main__':
    address = '上海市嘉定区安亭镇安拓路56号汽车·创新港'
    location = '121.195122,31.279140'
    msg = geocode_location(location)
    geocode_address(address)
    #print msg

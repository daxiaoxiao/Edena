# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
1.
a=[23,23,22,24,25,23,24]
print(a[0])
print(a[1])
print('ÖÜÈý'+str(a[2]))
print(a[3])
print(a[4])
print(a[5])
print(a[6])

2.
a={'ÐÇÆÚÒ»':['31','Ð¡Óê'],
   'ÐÇÆÚ¶þ':['31','Çç'],
   'ÐÇÆÚÈý':['33','Çç'],
   'ÐÇÆÚËÄ':['32','±©Óê'],
   'ÐÇÆÚÎå':['34','¶àÔÆ']}
print(a['ÐÇÆÚÈý'])

3.
a=b'1'
print(a)
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=shanghai&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json
data=json.loads(data)
print(data['main']['temp'])
print(data['weather'][0]['description'])
print(data['main']['pressure'])

4.
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#data字典--〉〉list列表--〉〉2 index列表--〉〉main字典--〉〉temp变量        温度
#data字典--〉〉list列表--〉〉2 index列表--〉〉dt_txt变量                   时间
print(data['list'][2]['dt_txt'],
      data['list'][2]['main']['temp'],
      data['list'][2]['main']['temp_min'],
      data['list'][2]['main']['temp_max'],
      data['list'][2]['main']['pressure'],
      data['list'][2]['weather'][0]['description'])
print(data['list'][10]['dt_txt'],
      data['list'][10]['main']['temp'],
      data['list'][10]['main']['temp_min'],
      data['list'][10]['main']['temp_max'],
      data['list'][10]['main']['pressure'],
      data['list'][10]['weather'][0]['description'])
print(data['list'][18]['dt_txt'],
      data['list'][18]['main']['temp'],
      data['list'][18]['main']['temp_min'],
      data['list'][18]['main']['temp_max'],
      data['list'][18]['main']['pressure'],
      data['list'][18]['weather'][0]['description'])
print(data['list'][26]['dt_txt'],
      data['list'][26]['main']['temp'],
      data['list'][26]['main']['temp_min'],
      data['list'][26]['main']['temp_max'],
      data['list'][26]['main']['pressure'],
      data['list'][26]['weather'][0]['description'])
print(data['list'][34]['dt_txt'],
      data['list'][34]['main']['temp'],
      data['list'][34]['main']['temp_min'],
      data['list'][34]['main']['temp_max'],
      data['list'][34]['main']['pressure'],
      data['list'][34]['weather'][0]['description'])
print('第一天：','_'*int( data['list'][2]['main']['temp']))
print('第二天：','_'*int( data['list'][10]['main']['temp']))
print('第三天：','_'*int( data['list'][18]['main']['temp']))
print('第四天：','_'*int( data['list'][26]['main']['temp']))
print('第五天：','_'*int( data['list'][34]['main']['temp']))
temp={
      data['list'][2]['main']['temp'],
      data['list'][10]['main']['temp'],
      data['list'][18]['main']['temp'],
      data['list'][26]['main']['temp'],
      data['list'][34]['main']['temp'],
      }   
print(sorted(temp))









  

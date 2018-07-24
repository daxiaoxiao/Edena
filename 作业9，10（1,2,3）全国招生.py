# -*- coding: utf-8 -*-
"""
作业10：
1.获取2300所学校的编号
2.获取31所城市的编号
3.获取142600数据，每组三个城市
4.将142600数据使用spark统计
Created on Mon Jul 23 14:58:47 2018

@author: susan
"""
#1.获取2300所学校的编号
ls=open("all_school.txt",encoding="utf-8").readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split("-jianjie-")[1].split(".")[0])
#2.获取31所城市
ls2=open("XML高考派城市.txt",encoding="gbk").readlines()
cityls=[]
for line in ls2:
    text=line.split(", ")
    if len(text)==2:
         print(text[1].split(")")[1][2:4],text[1].split(")")[0])
        

import urllib.request as r
f=open('全国计划招生表--贵州.txt','a',encoding='utf-8')
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}
for schoolId in schoolls:
        req=r.Request(url,data='id={}&type={}&city=52&state=1'.format(schoolId,type).encode(),headers=headers)
        for type in (1,2):
            try:
                data=r.urlopen(req).read().decode('utf-8','ignore')
                while '<!DOCTYPE html>' in data:
                    data=r.urlopen(req).read().decode('utf-8','ignore')
                f.write(data+'\n')
                print('success')
            except Exception as err:
                print('have an error')

f.close()#关闭保存程序  


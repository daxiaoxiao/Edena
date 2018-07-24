# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:43:33 2018

@author: susan
"""
plist=[]
for i in range(1,101):
    j=44*(i-1)
    plist.append(j)
def web_information(num):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%99%95%E8%A5%BF&bcoffset=7&p4ppushleft=1%2C48&ntoffset=4&s='+str(num)+'&ajax=true'
    import urllib.request as r
    data=r.urlopen(url).read().decode('utf-8','ignore')
    f=open('淘宝裙子信息（陕西）.txt','a',encoding='utf-8')#打开文件
    f.write(data+'\n')#文件中写入data数据
    f.close()   
for num in plist:
    web_information(num)
#######################用占位符实现
for s in range(0,4400,44):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%99%95%E8%A5%BF&bcoffset=7&p4ppushleft=1%2C48&ntoffset=4&s={}&ajax=true'
    import urllib.request as r
    data=r.urlopen(url.format(s)).read().decode('utf-8','ignore')
    f=open('淘宝信息.txt','w',encoding='utf-8')
    f.write(data+'\n')
    f.close()
####保存为csv格式
def web_information(num):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%99%95%E8%A5%BF&bcoffset=7&p4ppushleft=1%2C48&ntoffset=4&s='+str(num)+'&ajax=true'
    import urllib.request as r
    data=r.urlopen(url).read().decode('gbk','ignore')
    f=open('淘宝裙子信息（陕西）2.csv','a',encoding='gbk')#打开文件
    f.write(data+'\n')#文件中写入data数据
    f.close()   
for num in plist:
    web_information(num)
    

    

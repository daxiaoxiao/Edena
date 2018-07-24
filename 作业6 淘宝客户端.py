# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import urllib.request as r
data=r.urlopen('https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json
data=json.loads(data)
def information(m): 
#商品：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》title变量
    print('商品：'+data['mods']['itemlist']['data']['auctions'][m]['title'])
#价格：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_price变量
    print('价格：'+data['mods']['itemlist']['data']['auctions'][m]['view_price'])
#邮费：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_fee变量
    print('邮费：'+data['mods']['itemlist']['data']['auctions'][m]['view_fee'])
#销量：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_sales变量
    print('销量：'+data['mods']['itemlist']['data']['auctions'][m]['view_sales'])
information(0) 
information(1)
information(2)
information(3)
print('+'*30)

ls=[]
def price():
    for i in range(0,36):
        m=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        ls.append(m)
    return ls
price()
n=sorted(ls)
print('商品价格从高到低为')
x=list(reversed(n))
print(x)

def free():
    for i in range(0,36):
        if float (data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.00:
            print('第{}件商品包邮'.format(i+1))
            print('商品名称为'+data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
            print('商品的售价为'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
            print('销量为'+data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
            print('店名为'+data['mods']['itemlist']['data']['auctions'][i]['nick'])
            print(' ')
            print(str('-')*20) 
free()





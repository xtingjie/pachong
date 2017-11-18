# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:33:29 2017

@author: xtingjie
"""

import requests
from bs4 import BeautifulSoup

def getSoup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def getFloor(soup):
    floors = soup.find_all('li', class_=' j_thread_list clearfix')
    return floors

def getTitle(floor):
    title = floor.find('a', class_="j_th_tit ").text
    return title

def getAuthor(floor):
    span = floor.find('span', class_="frs-author-name-wrap")
    author = span.find('a')
#    author = floor.find('a', class_="frs-author-name j_user_card ")
#    author = floor.find('span', attrs={'class': 'tb_icon_author '})
#    author = floor.find('span', attrs={'class': 'tb_icon_author '})

    return author.text

def getTime(floor):
    span = floor.find('span', class_="threadlist_reply_date pull_right j_reply_data")
    return span.text.replace(' ', '')

def get_pic_from_url(url):
    #从url以二进制的格式下载图片数据
    pic_content = requests.get(url,stream=True).content
    open('filename.mp4','wb').write(pic_content)

get_pic_from_url('http://tb-video.bdstatic.com/tieba-smallvideo-transcode/8_ee04bb4464cbad249a1230ae11246811_3.mp4')


url = 'http://tieba.baidu.com/f?kw=%E7%9\
4%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn=0'
soup = getSoup(url)
floors = getFloor(soup) 

for floor in floors:
    print(getTitle(floor) + '---' + getAuthor(floor) + getTime(floor))



   
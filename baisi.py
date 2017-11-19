# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:50:10 2017

@author: admin
"""

import requests
from bs4 import BeautifulSoup

def getSoup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def getFloor(soup):
    floors = soup.find_all('li', )
    return floors

def getNames(soup):
    t1 = soup.find_all('a', class_='u-user-name')
    t2 = []
    for name in t1:
        t2.append(name.text)
    return t2

def getTime(soup):
    t1 = soup.find_all('div', class_="u-txt")
    t2 = []
    for time in t1:
        t2.append(time.find('span').text)
    return t2

def getDuanzi(soup):
    t1 = soup.find_all('div', class_='j-r-list-c-desc')
    t2 = []
    for duanzi in t1:
        t3 = duanzi.find('a').text
        t2.append(t3)
    return t2
    
    
soup = getSoup('http://www.budejie.com/text/')
names = getNames(soup)
times = getTime(soup)
duanzis = getDuanzi(soup)

with open('baisi.txt', 'w') as f:
    for i in range(len(times)):
        f.write(names[i]+'   ')
        f.write(times[i]+'\n')
        f.write(duanzis[i]+'\n\n\n')

#f = open('baisi.txt', 'w') 
#for i in range(len(times)):
#    f.write(names[i]+'   ')
#    f.write(times[i]+'\n')
#    f.write(duanzis[i]+'\n\n\n')
#f.close()



#for floor in floors:
#    name = getName(floor)
#    print(name)

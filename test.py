# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
h = requests.get('https://weibo.com/u/2134671703?refer_flag=1001030101_&is_all=1')
soup = BeautifulSoup(h.content, 'lxml')
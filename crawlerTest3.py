import json
from urllib.parse import urlencode

import requests
from lxml import etree

import ssl

import urllib3

url = 'http://movie.douban.com/j/search_subjects'
header = {
    "User-Agent": 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=JBee6dlJHQw',
    'Host': 'movie.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


parameters = {
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'start':0
}
encodedParameters = urlencode(parameters)
newUrl = '{}?{}'.format(url,encodedParameters)
print(newUrl)
r1 = requests.get(newUrl,headers=header)
r1_decoded=r1.content.decode('utf-8')
print('get via requets:',r1_decoded);
with urllib3.PoolManager() as http:
    response = http.urlopen('GET',url=newUrl,headers=header)
    print(type(response))
    print('status:',response.status)
    print(response.data.decode('utf-8'))
    jsonO = json.loads(response.data.decode('utf-8'))
    print(jsonO['subjects'])
#ssl
# context = ssl._create_unverified_context()
# requests.get(url,headers=header,context=context)
from urllib.parse import urlencode
from urllib.request import urlopen,Request
from lxml import etree

url = 'http://www.autohome.com.cn/grade/carhtml/D.html'
parameters = { 'wd':'a'}
encodedParameters = urlencode(parameters)
newUrl = url+'?{}'.format(encodedParameters)
print(newUrl)

ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
r = Request(newUrl);
r.add_header('User-agent',ua)
response = urlopen(r)
print(response.info());
#print(response.read());

html = etree.HTML(response.read())
print(html.text)




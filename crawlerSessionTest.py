import requests
from lxml import etree
import ssl

url = 'https://www.baidu.com'
header= {
    "Cookie": "uv_firstv_refers=http%3A//www.xcar.com.cn/; _Xdwuv=599e6b9061d1e; _Xdwnewuv=1; _Xdwstime=time_to_replace; ad__city=475; _PVXuv=59926b90925b7; place_prid=1; place_crid=475; place_ip=221.219.136.213_1; uv_firstv_refer=%28%243%29///%28%2412%29/63; _locationInfo_=%7Burl%3A%22http%3A%2F%2Fbj.xcar.com.cn%2F%22%2Ccity_id%3A%22475%22%2Cprovince_id%3A%221%22%2C%20city_name%3A%22%25E5%258C%2597%25E4%25BA%25AC%22%7D; Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0=1501658839,1503548106; Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0=time_to_replace; BIGipServerpool-c26-xcar-dealerweb1-80=1237913354.20480.0000; QuickMsgQuickId=j248dealer.xcar.com.cn717"
,
    "User-Agent": 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
session = requests.session();
response1 = session.get(url, headers=header)
print(response1.cookies)
print(response1.request.headers)
print('==============request2==================')
response2 = session.get(url, headers=header)
print(response2.request.headers)


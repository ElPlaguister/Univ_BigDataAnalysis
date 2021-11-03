import os
import requests
import urllib
import mylib

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    
    KEY = str(key['dataseoul'])
    TYPE = 'json'
    SERVICE = 'SearchSTNBySubwayLineInfo'
    LINE_NUM = str(2)
    START_INDEX = str(1)
    END_INDEX = str(10)
    params = '/'.join([KEY, TYPE, SERVICE, START_INDEX, END_INDEX, '', '', LINE_NUM])
    _url = 'http://openAPI.seoul.go.kr:8088'
    url = '/'.join([_url, params])
    
    r = requests.get(url)
    stations = r.json()
    for e in stations['SearchSTNBySubwayLineInfo']['row']:
        print(u"{0:4s}\t{1:15s}\t{2:3s}\t{3:2s}".format(e['STATION_CD'], e['STATION_NM'], e['FR_CODE'], e['LINE_NUM']))
        
if __name__ =="__main__":
    doIt()

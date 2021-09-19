import os
import mylib
import urllib
import requests

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)

    SERVICE = 'ArpltnInforInqireSvc'
    OPERATION_NAME = 'getMinuDustFrcstDspth'
    params1 = os.path.join(SERVICE, OPERATION_NAME)

    _d = dict()
    _d['searchDate'] = '2021-08-10'
    params2 = urllib.parse.urlencode(_d)

    params = params1 + '?' + 'serviceKey=' + key['gokr'] + '&' + params2
    endpoint = 'http://apis.data.go.kr/B552584'
    url = "/".join([endpoint, params])

    data = requests.get(url).text
    print(data)

if __name__=='__main__':
    doIt()

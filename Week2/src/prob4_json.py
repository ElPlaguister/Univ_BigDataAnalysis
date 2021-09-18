import os
import requests
import mylib

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    endpoint = 'http://openAPI.seoul.go.kr:8088'
    KEY = str(key['dataseoul'])
    TYPE = 'json'
    SERVICE = 'CardSubwayStatsNew'
    START_INDEX = '1'
    END_INDEX = '5'
    USE_DT = '20210801'

    url = os.path.join(endpoint, KEY, TYPE, SERVICE, START_INDEX, END_INDEX, USE_DT)

    response = requests.get(url)
    sub = response.json()

    for e in sub['CardSubwayStatsNew']['row']:
        print("{0:5s}\t{1:10s}\t{2:9.1f}\t{3:9.1f}".format(e['LINE_NUM'], e['SUB_STA_NM'], e['RIDE_PASGR_NUM'], e['ALIGHT_PASGR_NUM']))

if __name__ == "__main__":
    doIt()

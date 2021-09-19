import os
import mylib
import requests

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    KEY = str(key['dataseoul'])
    TYPE = 'json'
    SERVICE = 'VwsmTrdarFlpopQq'
    START_INDEX = str(1)
    END_INDEX = str(10)
    STDR_YM_CD = str(2017)
    params = os.path.join(KEY, TYPE, SERVICE, START_INDEX, END_INDEX, STDR_YM_CD)
    endpoint = 'http://openAPI.seoul.go.kr:8088'
    url = "/".join([endpoint, params])
    r = requests.get(url)
    trade = r.json()
    for e in trade['VwsmTrdarFlpopQq']['row']:
        print(e['TRDAR_CD'], e['TRDAR_CD_NM'], e['TOT_FLPOP_CO'], e['ML_FLPOP_CO'])


if __name__ == '__main__':
    doIt()

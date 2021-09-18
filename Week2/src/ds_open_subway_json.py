import os
import requests
import urllib
import mylib

def printStations():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    KEY = str(key['dataseoul'])
    endpoint = 'http://openAPI.seoul.go.kr:8088'
    TYPE = 'json'
    SERVICE = 'SearchSTNBySubwayLineInfo'
    LINE_NUM = '2'

    start_index = 1
    end_index = 10
    list_total_count = 0
    while True:
        START_INDEX = str(start_index)
        END_INDEX = str(end_index)
        params = "/".join([KEY, TYPE, SERVICE, START_INDEX, END_INDEX,'','',LINE_NUM])
        url = "/".join([endpoint, params])
        r = requests.get(url)
        stations = r.json()
        if(start_index == 1):
            list_total_count = stations['SearchSTNBySubwayLineInfo']['list_total_count']
            print("- Total Count: ", list_total_count)
        for e in stations['SearchSTNBySubwayLineInfo']['row']:
            print("{0:4s}\t{1:15s}\t{2:3s}\t{3:2s}".format(e['STATION_CD'], e['STATION_NM'], e['FR_CODE'], e['LINE_NUM']))
        start_index += 10
        end_index += 10
        if end_index > list_total_count:
            print("----- Ending endIndex=", end_index)
            break

if __name__ == "__main__":
    printStations()
    


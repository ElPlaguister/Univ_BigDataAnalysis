
import lxml
import lxml.etree
import requests
import os
import mylib

def printStations():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    KEY = str(key['dataseoul'])
    endpoint = 'http://openAPI.seoul.go.kr:8088'
    TYPE = 'xml'
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
        data = requests.get(url).text
        tree = lxml.etree.fromstring(data.encode('utf-8'))

        if(start_index == 1):
            for node in tree.xpath('//list_total_count'):
                list_total_count = int(node.text)
                print("total_count=", str(list_total_count))

        for node in tree.xpath('//STATION_NM'):
            print(node.text, end=", ")
        start_index += 10
        end_index += 10
        if end_index > list_total_count:
            print("----- Ending endIndex=", end_index)
            break

if __name__ == "__main__":
    printStations()

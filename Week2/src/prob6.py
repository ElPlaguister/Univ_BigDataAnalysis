import os
import requests
import json
from pymongo import MongoClient
import mylib

Client = MongoClient('mongodb://localhost:27017')
_db = Client['ds_open_subwayPassengersDb'] # db
_table = _db['db_open_subwayTable'] # Collection

def saveJson(_fname, _data):
    import io
    with io.open(_fname, 'a', encoding='utf-8') as json_file:
        _j = json.dump(_data, json_file, ensure_ascii=False)
        json_file.write(str(_j) + "\n")

def readJson(_fname):
    for line in open(_fname, 'r').readlines():
        _j = json.loads(line)
        print(_j['id'])

def saveDB(_data):
    _table.insert_one(_data)

def readDB():
    for tweet in _table.find():
        print(tweet['id'], tweet['text'])

def saveFile(_fname, _data):
    fp = open(_fname, 'a')
    fp.write(_data + "\n")

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)

    endpoint = 'http://openAPI.seoul.go.kr:8088'
    KEY = str(key['dataseoul'])
    TYPE = 'json'
    SERVICE = 'CardSubwayTime'
    _startIndex = 1
    _endIndex = 5
    USE_DT = '202106'

    _maxIter = 20
    _iter = 0
    _jfname = 'src/ds_open_subwayTime.json'

    while _iter < _maxIter:
        url  = "/".join([endpoint, KEY, TYPE, SERVICE, str(_startIndex), str(_endIndex), USE_DT])
        subwayTime = requests.get(url)
        _json = subwayTime.json()
        print(_json)
        saveJson(_jfname, _json)
        saveDB(_json)
        _startIndex += 5
        _endIndex += 5
        _iter += 1

if __name__ == '__main__':
    doIt()

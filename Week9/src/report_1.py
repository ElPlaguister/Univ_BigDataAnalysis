import os
import requests
import json
from pymongo import MongoClient
import mylib

Client = MongoClient('mongodb://localhost:27017')
_db = Client['myDB']
_table = _db['report1']

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
    SERVICE = 'landActualPriceInfo'
    _startIndex = 1
    _endIndex = 50

    _maxIter = 100
    _iter = 0
    _jfname = 'src/LandActualPriceInfo.json'
    rows = []
    myJson = 0

    while _iter < _maxIter:
        url  = "/".join([endpoint, KEY, TYPE, SERVICE, str(_startIndex), str(_endIndex)])
        _json = requests.get(url).json()
        if(_iter == 0):
            print('apiSize: ', _json['landActualPriceInfo']['list_total_count'])
            myJson = _json
        if(_iter == _maxIter - 1):
            print('myDB Size: ', str(_maxIter * (_endIndex - _startIndex + 1)))
            print('last item: ', _json['landActualPriceInfo']['row'][-1])
        rows.extend(_json['landActualPriceInfo']['row'])
        #saveDB(_json)
        _startIndex += 50
        _endIndex += 50
        _iter += 1
    myJson['landActualPriceInfo']['row'] = rows
    saveJson(_jfname, myJson)

if __name__ == '__main__':
    doIt()

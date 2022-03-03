def getDict(keyPath):
    d = dict()
    f = open(keyPath, 'r')
    for line in f.readlines():
        row = line.split('=')
        key = row[0]
        d[key] = row[1].strip()
    return d

def getKey(keyPath = 'src/key.properties', keyId = 'dataseoul'):
    keyDict = getDict(keyPath)
    return keyDict[keyId]

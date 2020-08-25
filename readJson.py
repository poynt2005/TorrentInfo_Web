#coding = utf-8
from io import open
import os, json, time, shutil


def readJson(downloadtime = None, magnet = None, type = None):
    jsonFile = None

    with open(os.path.join(os.getcwd(), 'torrentfiles', 'history.json'), 'r', encoding='utf8') as f:
        jsonFile = json.loads(f.read())

    rst = False

    if type == 'store':
        expire = downloadtime + 21600

        fname = '%s.torrent' % int(downloadtime * 1000000)

        jsonFile.append({
            'fname': fname,
            'expire': expire,
            'magnet': magnet
        })

        rst = '/file/%s' % fname
    elif type== 'get':
        for item in jsonFile:
            if item['magnet'] == magnet:
                rst =  'file/%s' % item['fname']
                break

    toRemove = []
    nowtime = time.time()

    for idx in range(len(jsonFile)):
        if nowtime > jsonFile[idx]['expire']:
            os.remove(os.path.join(os.getcwd(), 'torrentfiles', jsonFile[idx]['fname']))
            toRemove.append(idx)

    for i in toRemove:
        jsonFile.remove(i)
    
    with open(os.path.join(os.getcwd(), 'torrentfiles', 'history.json'), 'w', encoding='utf8') as f:
        f.write(unicode(json.dumps(jsonFile, ensure_ascii=False)))

    return rst
    
def clearData():
    for i in os.listdir(os.path.join(os.getcwd(), 'torrentfiles')):
        filepath = os.path.join(os.getcwd(), 'torrentfiles', i)
        if not i == 'history.json' and not i.split('.')[-1] == 'torrent':
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)


    


    
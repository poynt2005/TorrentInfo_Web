#coding = utf-8
from flask import Flask,request,jsonify,redirect,send_file
from io import open
import os, time, readJson, torrentinfo

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, 
            static_url_path='',
            static_folder='dist'
)

@app.route('/', methods=['GET'])
def index():
    return redirect('/index.html')

@app.route('/torrent', methods=['POST'])
def turnToMagnet():
    files = request.files['file'].read()

    torrent = torrentinfo.torrentInfo('torrent')

    magnetLink = torrent.getMagnet(files)

    if not magnetLink:
        magnetLink = 'Error'

    return jsonify({
        'filetype': 'torrent',
        'magnet': magnetLink
    })

@app.route('/magnet', methods=['POST'])
def turnToTorrent():
    link = request.json['link']
    torrentRst = None

    jfile = readJson.readJson(magnet=link, type='get')
    if not jfile:
        downloadtime = time.time()

        torrent = torrentinfo.torrentInfo('magnet')
        torrentRst = torrent.getTorrent(link, os.path.join(os.getcwd(), 'torrentfiles'))

        if not torrentRst:
            return jsonify({
                'filetype': 'magnet', 
                'filename': 'Error', 
                'downloadLink': 'Error',
                'isExists': False
            })

        fname = '%s.torrent' % int(downloadtime * 1000000)

        with open(os.path.join(os.getcwd(), 'torrentfiles', fname), 'wb') as f:
            f.write(torrentRst['torrent_binary'])

        jfile = readJson.readJson(downloadtime=downloadtime, type='store', magnet=link, torrent_file_name=torrentRst['torrent_name'] + '.torrent')

    readJson.clearData()
    
    return jsonify({
        'filetype': 'magnet', 
        'filename': jfile['torrent_file_name'], 
        'downloadLink': jfile['fname'],
        'isExists': True
    })

@app.route('/file/<torrentFile>', methods=['GET'])
def sendTorrent(torrentFile):
    return send_file(os.path.join(os.getcwd(), 'torrentfiles', torrentFile))
 
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8080)


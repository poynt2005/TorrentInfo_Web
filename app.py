#coding = utf-8
from flask import Flask,request,jsonify,redirect
from TorrentInfo.getFile import Torrent2Magnet
from TorrentInfo.GetTorrentInfo import GetTorrentInfo as GTI

app = Flask(__name__, static_url_path='')
 
@app.route('/')
def index():
    return render_template('home.html')
	
@app.route('/magnet_process' , methods = ['POST'])
def magnet_process():

        if request.method == 'POST':
            link = request.form['magnet_link']
            print link
           
            a = Torrent2Magnet(link)
            binary = a.getTorrent()
            if binary:
                return binary
            else:
                return '0'

@app.route('/file_process' , methods = ['POST'])
def file_process():

    if request.method == 'POST':
        fs = request.files['file']
        
        a = GTI(fs.read())
        print(a.get_magnet())
        
        return jsonify({"link":a.get_magnet()})
 
if __name__ == "__main__":
    app.debug = True
    app.run()


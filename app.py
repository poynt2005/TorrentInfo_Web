#coding = utf-8
from flask import Flask,render_template,request,send_from_directory,url_for,send_file,jsonify
from TorrentInfo.getFile import Torrent2Magnet
from TorrentInfo.GetTorrentInfo import GetTorrentInfo as GTI
import os
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('home.html')
	
@app.route('/magnet_process' , methods = ['POST'])
def magnet_process():

        if request.method == 'POST':
            link = request.form['magnet_link']
            print link
            a = Torrent2Magnet(link)
            a.getTorrent()
            FilePath = os.path.dirname(os.path.realpath(__file__)).replace('\\' , '/') + '/src/' + a.getFileName()
            
            print FilePath
            
            return send_file(FilePath)

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

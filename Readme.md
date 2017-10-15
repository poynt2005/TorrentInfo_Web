# TorrentInfo Web
```
root                    contain "app.py"
  |---> src             contain torrent files convert from magnet
  |---> static          
  |       | ----> css   contain css file
  |       | ----> js    contain jQuery file
  |---> TorrentInfo     contain my module file
  |---> Upload          contain nothing = =
```
### __*(Require Python 2.7 with flask lib)*__ 
## Usage:
```
git clone "https://github.com/poynt2005/TorrentInfo_Web.git"
python TorrentInfo_Web/app.py
go to "127.0.0.1:5000"
```
## *home.html*
#### 1. "Upload Torrent" : Upload torrent and convert to magnet link below 
#### 2. "Magnet Link" : Convert Magnet link to torrent
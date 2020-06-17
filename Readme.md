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
### __*(Require Docker)*__ 
## Usage:
```
git clone "https://github.com/poynt2005/TorrentInfo_Web.git"
docker build -t <name> .
docker run -p 8080:8080 -p 6881:6881 -d <name>
```
## *home.html*
#### 1. "Upload Torrent" : Upload torrent and convert to magnet link below 
#### 2. "Magnet Link" : Convert Magnet link to torrent
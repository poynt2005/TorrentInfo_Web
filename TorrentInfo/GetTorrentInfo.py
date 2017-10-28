#coding = utf-8
import libtorrent
from urllib import urlencode

class GetTorrentInfo(object):
    def __init__(self , readbinary):
        self.bt = libtorrent.bdecode(readbinary)
    
    def get_magnet(self):
        info = libtorrent.torrent_info(self.bt)

        name_url_code = urlencode({'dn' : info.name()})

        url_link = 'magnet:?xt=urn:btih:%s&%s' % (info.info_hash(), name_url_code)
        return url_link

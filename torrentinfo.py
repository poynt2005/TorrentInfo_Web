#coding = utf-8
import libtorrent as lt
from urllib import urlencode
import time, os

class torrentInfo(object):
    def __init__(self, fileType):
        self.fileType = fileType

        if self.fileType == 'magnet':
            self.session = lt.session()
            
            self.session.add_extension('ut_metadata')
            self.session.add_extension('ut_pex_plugin')
            self.session.add_dht_router('router.utorrent.com', 6881)
            self.session.add_dht_router('router.bittorrent.com', 6881)
            self.session.add_dht_router('dht.transmissionbt.com', 6881)
            self.session.add_dht_router('router.bitcomet.com', 6881)
            self.session.add_dht_router('dht.aelitis.com', 6881)
            self.session.start_dht()
        if self.fileType == 'torrent':
            self.bt = None
    
    def getMagnet(self, binary):
        if not self.fileType == 'torrent':
            return False

        self.bt = lt.bdecode(binary)
        info = lt.torrent_info(self.bt)
        name_url_code = urlencode({'dn' : info.name()})
        url_link = 'magnet:?xt=urn:btih:%s&%s' % (info.info_hash(), name_url_code)
        return url_link

    def getTorrent(self, magnet_url, store_path, timeout=150):
        if not self.fileType == 'magnet':
            return False
        param = {
            'save_path': store_path,
            'duplicate_is_error': False,
            'storage_mode': lt.storage_mode_t.storage_mode_allocate,
        }

        torrent_handle = lt.add_magnet_uri(self.session, magnet_url, param)
        start_time = time.time()
        found = False

        while True:
            if torrent_handle.has_metadata():
                found = True
                break
            time.sleep(2)


            if not (time.time() - start_time) <= timeout:
                break
            
        if found:
            torrent_info = torrent_handle.get_torrent_info()
            f_s = lt.file_storage()

            for i in torrent_info.files():
                f_s.add_file(i)
            files = lt.create_torrent(f_s)
            files.set_comment(torrent_info.comment())
            files.set_creator(torrent_info.creator())

            return {
                'torrent_name': torrent_info.name(),
                'torrent_binary': lt.bencode(files.generate())
            }
        else:
            return False




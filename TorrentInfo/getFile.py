import libtorrent
import sys
import tempfile
import os
import time
import re
class Torrent2Magnet(object):
    def __init__(self , magnet_url):
        self.fileName = None
        if not re.match('^magnet\:\?xt\=urn\:btih\:.*' , magnet_url):
            print 'It is not a vailed magnet link'
            exit()
        else:
            self.current_dir =  os.path.dirname(os.path.realpath(__file__))
            self.magnet_url = magnet_url

            #start libtorrent session
            self.session = libtorrent.session()
            self.session.add_extension('ut_metadata')
            self.session.add_extension('ut_pex_plugin')
            self.session.add_dht_router('router.utorrent.com', 6881)
            self.session.add_dht_router('router.bittorrent.com', 6881)
            self.session.add_dht_router('dht.transmissionbt.com', 6881)
            self.session.add_dht_router('router.bitcomet.com', 6881)
            self.session.add_dht_router('dht.aelitis.com', 6881)
            self.session.start_dht()


    def getTorrent(self):
        param = {
            'save_path': self.current_dir,
            'duplicate_is_error': True,
            'storage_mode': libtorrent.storage_mode_t.storage_mode_allocate,
        }

        torrent_handle = libtorrent.add_magnet_uri(self.session, self.magnet_url, param)
        print 'Start Downloading metadata'

        found = False

        #counting time
        start_time = time.time()
        while True:
            if torrent_handle.has_metadata():
                found = True
                break
            time.sleep(2)

            #if getting torrent longer than 60 secs. Stop to find the torrent
            if not (time.time() - start_time) <= 120:
                found = False
                break
            print 'Each 2 sec.  Download Speed is : %f' % (libtorrent.peer_info().down_speed)
            continue

        if found:
            print 'Downloaded Success'

            torrent_info = torrent_handle.get_torrent_info()
            f_s = libtorrent.file_storage()

            #merge torrent files
            for i in torrent_info.files():
                f_s.add_file(i)
            files = libtorrent.create_torrent(f_s)
            files.set_comment(torrent_info.comment())
            files.set_creator(torrent_info.creator())

            #encode to binary
            torrent_binary = libtorrent.bencode(files.generate())

            #get torrent name
            torrent_name = torrent_info.name()
            self.fileName = torrent_name
            return torrent_binary
        else:
            return None

    def getFileName(self):
        if self.fileName:
            return self.fileName + '.torrent'

#coding = utf-8
import libtorrent
import sys
import tempfile
import os
import time
import re
class GetTorrentInfo(object):
    def __init__(self , readbinary):
        self.bt = libtorrent.bdecode(readbinary)
    
    def get_magnet(self):
        info = libtorrent.torrent_info(self.bt)
        name = ''
        if ' ' in info.name():
            name = info.name().replace(' ', '_')
        else:
            name = info.name()

        url_link = 'magnet:?xt=urn:btih:%s' % (info.info_hash())
        return url_link

    #check if the torrent has directories
    @staticmethod
    def hasDirectory(input_data):
        if re.match('.*path.*' , str(input_data)):
            return True
        else:
            return False

    def getFileName(self):
        #it's a dictionary data , get files' name
        info_dict = self.bt['info']
        if self.hasDirectory(info_dict):
            files_list = info_dict['files']
            result = []
            for i in files_list:
                result.append(i['path'])
            return result
        else:
            return info_dict['name']
        

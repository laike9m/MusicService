from __future__ import print_function
# coding:utf-8
import glob
import os
import eyed3

import sys
fse = sys.getfilesystemencoding()
files = [x for x in glob.glob(u"songs/*.mp3")]

with open("unicode.txt", 'wt') as uni:
    for f in files:
        song = eyed3.load(f)
        title = song.tag.title
        artist = song.tag.artist
        try:
            # 有些信息是按latin1 decode的, 变成\xcb\xea这样, 但实际上应该是gbk decode, 即两个字节应该一起读
            # 所以要先encode回bytes再用gbk decode
            # refer to http://stackoverflow.com/questions/23521361/how-to-convert-string-to-bytes-in-python-2
            title = title.encode('latin1').decode('gbk')
            artist = artist.encode('latin1').decode('gbk')
        except UnicodeEncodeError:
            pass
        uni.write(u'{:<30}'.format(title).encode('utf-8'))
        uni.write(artist.encode('utf-8') + '\n')


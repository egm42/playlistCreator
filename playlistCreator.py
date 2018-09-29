import pandas as pd
import xml.etree.cElementTree as ET
import os.path

class playlistCreator:
    table = pd.DataFrame()
    url = ''
    desc = ''

    def __init__(self):
        self

    def tableFromFile(self, filepath, url, description):
        extension = os.path.splitext(filepath)[1]
        if extension == '.csv':
            self.table = pd.read_csv(filepath)
        elif extension == '.xlsx':
            self.table = pd.read_excel(filepath)
        else:
            pass
        self.url = url
        self.desc = description

        return 0

    def xspfPlaylist(self, name):
        playlist = ET.Element('playlist', version='1', xmlns='http://xspf.org/ns/o/')
        ET.SubElement(playlist, 'title').text = name
        trackList = ET.SubElement(playlist, 'trackList')

        for index, row in self.table.iterrows():
            track = ET.SubElement(trackList, 'track')
            ET.SubElement(track, 'title')
            ET.SubElement(track, 'title').text = row[self.desc]
            ET.SubElement(track, 'location').text = row[self.url]

        tree = ET.ElementTree(playlist)
        return tree

    def vlcPlaylist(self):
        pass
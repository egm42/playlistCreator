import pandas as pd
import xml.etree.cElementTree as ET
import os.path

class playlistCreator:

    def __init__(self):
        self

    def tableFromFile(self, filepath, url, description):
        self.url = url
        self.desc = description

        extension = os.path.splitext(filepath)[1]
        if extension == '.csv':
            self.table = pd.read_csv(filepath)
        elif extension == '.xlsx':
            self.table = pd.read_excel(filepath)
        else:
            pass

        return 0

    def xspfPlaylist(self, name):
        root = ET.Element('playlist', version='1', xmlns='http://xspf.org/ns/o/')
        ET.SubElement(root, 'title').text = name
        trackList = ET.SubElement(root, 'trackList')

        for index, row in self.table.iterrows():
            track = ET.SubElement(trackList, 'track')
            ET.SubElement(track, 'title')
            ET.SubElement(track, 'title').text = row[self.desc]
            ET.SubElement(track, 'location').text = row[self.url]

        self.xmlTree = ET.ElementTree(root)

        return 0

    def vlcPlaylist(self):
        pass

    def saveToFile(self, directory, name):
        filepath = os.path.join(directory, name + '.xspf')

        self.xmlTree.write(filepath, encoding='UTf-8', xml_declaration=True)

        return 0
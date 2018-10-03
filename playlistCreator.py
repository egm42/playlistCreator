import pandas as pd
import xml.etree.cElementTree as ET
import os.path

class playlistCreator:

    # def __init__(self):
    #     self

    def tableFromFile(self, filepath):
        extension = os.path.splitext(filepath)[1]
        if extension == '.csv':
            self.table = pd.read_csv(filepath)
        elif extension == '.xlsx':
            self.table = pd.read_excel(filepath)
        else:
            pass

        return 0

    def setColumns(self):
        header = list(self.table)

        while True:
            for index, head in enumerate(header):
                print(str(index + 1) + '. ' + head)
            try:
                urlInt = int(input('Select column containing URL(enter #): '))
                descInt = int(input('Select column containing Description(enter #): '))
                self.url = header[urlInt - 1]
                self.desc = header[descInt - 1]
            except ValueError:
                print('Values entered are not integers. Retry input.')
            except IndexError:
                print('Values entered are out of range. Retry input.')
            else:
                break

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

    def m3uPlaylist(self):
        playlist = "#EXTM3U\n\n"
        for index, row in self.table.iterrows():
            playlist += "#EXTINF: , " + row[self.desc] + "\n"
            playlist += row[self.url] + "\n\n"

        self.playlistString = playlist

        return 0

    def saveToFile(self, filetype, directory, name):
        if filetype == 'xspf':
            filepath = os.path.join(directory, name + '.xspf')
            self.xspfPlaylist(self, name)
            self.xmlTree.write(filepath, encoding='UTf-8', xml_declaration=True)
        elif filetype == 'm3u':
            filepath = os.path.join(directory, name + '.m3u')
            self.m3uPlaylist(self)
            with open(filepath, 'w') as f:
                f.write(self.playlistString)

        return 0
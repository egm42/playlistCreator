from playlistCreator import playlistCreator as pc
import os.path


if __name__ == '__main__':
    filepath = input('Enter full filepath: ')
    name = input('Enter playlist name: ')

    pc.tableFromFile(pc, filepath, 'url', 'desc')
    xml = pc.xspfPlaylist(pc, name)

    newFilepath = os.path.join(os.path.dirname(filepath),name + '.xspf')
    xml.write(newFilepath, encoding='UTf-8', xml_declaration=True)
    print('Playlist saved as: ' + newFilepath)
from playlistCreator import playlistCreator as pc
import os.path

if __name__ == '__main__':
    filepath = input('Enter filepath: ')
    name = input('Enter playlist name: ')

    pc.tableFromFile(pc, filepath, 'url', 'desc')
    xml = pc.xspfPlaylist(pc, name)
    xml.write(os.path.splitext(filepath)[0]+'.xspf')
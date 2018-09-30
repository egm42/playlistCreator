from playlistCreator import playlistCreator as pc
import os.path


if __name__ == '__main__':
    filepath = input('Enter full filepath: ')
    name = input('Enter playlist name: ')
    directory = input('Enter folder to save file: ')

    pc.tableFromFile(pc, filepath, 'url', 'desc')
    pc.xspfPlaylist(pc, name)
    pc.saveToFile(pc, directory, name)
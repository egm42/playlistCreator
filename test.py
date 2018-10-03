from playlistCreator import playlistCreator as pc

if __name__ == '__main__':
    filetype = 'xspf'

    filepath = input('Enter full filepath: ')
    name = input('Enter playlist name: ')
    print('1. xspf\n2. m3u')
    selection = int(input('Enter number of filetype desired: '))
    if selection == 1:
        filetype = 'xspf'
    elif selection == 2:
        filetype = 'm3u'
    directory = input('Enter folder to save file: ')

    pc.tableFromFile(pc, filepath)
    pc.setColumns(pc)
    pc.saveToFile(pc, filetype, directory, name)

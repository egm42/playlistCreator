# playlistCreator
A python tool to create playlists from formatted files. This program will take in already formatted input files(e.g. CSV or XLSX) and create playlist file to use in media player applications(e.g. VLC).

### Prerequisites
System requirements
```
pandas
```

## Testing Example

### Currently Supported Filetypes

#### Input Files
```
.csv
.xlsx
``` 

#### Output Files
```
.xspf
.m3u
```
Note: the xspfPlaylist function currently exports an xml tree. The test file saves it as a .xspf file.

### Run Tests
Activate your virtual environment and/or run the following
```
python test.py
```

Enter the full filepath and new playlist's name when prompted.
```
Enter full filepath: {directory}\{file}.csv
Enter playlist name: {name}
1. xspf
2. m3u
Enter number of filetype desired: {1 or 2}
Enter folder to save file: {directory}
1. url       <--- example output
2. desc      <--- example output
Select column containing URL(enter #): {enter column #}
Select column containing Description(enter #): {enter column #}

```

A confirmation message will display if the program ran successfully. The new '.xspf' playlist will be saved in the same directory as the original file.
```
Playlist saved as: {directory}\{name}.{xspf or m3u}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* The internet for being a huge repository of knowledge
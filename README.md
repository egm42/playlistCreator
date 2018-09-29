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
```

A confirmation message will display if the program ran successfully. The new '.xspf' playlist will be saved in the same directory as the original file.
```
Playlist saved as: {directory}\{name}.xspf
```

## Authors
* **Luis Ruiz** - [playlistCreator](https://github.com/egm42/playlistCreator)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* The internet for being a huge repository of knowledge
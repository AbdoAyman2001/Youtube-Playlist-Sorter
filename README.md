# YouTube Playlist Sorter

If you've ever downloaded a YouTube playlist, you've probably noticed that the files are often saved with long and confusing names that don't give you any indication of the order of the videos in the playlist. This can be frustrating if you want to watch the videos in order or if you want to organize them in a specific way.

The YouTube Playlist Sorter is a Python script that helps you sort your downloaded YouTube playlists in the correct order. Here's how it works:

1. The script uses the YouTube Data API to fetch the playlist items with their information, including the titles of the videos in the playlist.
2. It then compares and matches the titles fetched with the real files that exist in the specified directory path. To do this, it uses the following algorithms:
   - Jaccard similarity
   - Jaro-Winkler distance
   - Levenshtein distance
   - Hamming distance
   - Cosine similarity
   - Soft TF-IDF similarity
3. Once the script has found a match between the video title and the file name, it renames the file with the new title and adds the order of the video (e.g. `#000`, `#001`, `#002`, etc.) to the file name to indicate its position in the playlist.

With the YouTube Playlist Sorter, you can easily organize your downloaded YouTube playlists and watch them in the order they were intended to be watched.



# Getting Started
## Prerequisites
Before running the YouTube Playlist Sorter script, you will need to have the following software installed on your computer:

- Python 3.7 or later
## Installation
To install the YouTube Playlist Sorter script, follow these steps:

1. Clone or download the repository to your local machine.
2. Navigate to the root directory of the project in your terminal.
3. Install the necessary dependencies by running 
```
pip install -r requirements.txt
```


## Usage
Before using the YouTube Playlist Sorter, you must have a Google API key. To obtain an API key, please follow the instructions [here](https://developers.google.com/youtube/registering_an_application).

Once you have obtained an ```API key```, follow these steps to use the YouTube Playlist Sorter:

Navigate to the directory where the script is installed.

Open the ```.env``` file and enter your API key in the ```API_KEY``` variable.

Open the main.py file and enter the link of the ```playlist opened in its specified page```, and the path of the directory where the unsorted downloaded playlist files are located in.

Run the following command in the terminal or command prompt to install the required dependencies:
```
pip install -r requirements.txt
```
Run the following command in the terminal or command prompt to execute the script:

```
python main.py
```
The script will prompt you to enter the URL of the YouTube playlist you want to sort ```AND MAKE SURE TO COPY THE URL OF THE PLAYLIST ITSELF OPENED IN ITS SPECIFIC PAGE```.

Once you have entered the playlist URL, the script will fetch the video data and compare the video titles with the files in the specified directory using various algorithms.

The script will rename the files in the directory based on the order of the videos in the playlist and add a number to the beginning of each file name to indicate its order in the playlist.
## Example
Here's an example of how to use the YouTube Playlist Sorter script:
```
$ cd /path/to/youtube-playlist-sorter
$ pip install -r requirements.txt
$ python main.py
```
## Credits
This script was developed by ```AbdoAyman2001```. Special thanks to ```YouTube Data API``` for providing the necessary tools to retrieve data from YouTube playlists.
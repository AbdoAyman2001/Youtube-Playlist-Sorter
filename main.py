import os
from utils import (format_position,
                   get_data_from_user,
                   MessageState,
                   ResponseState,
                   print_c)

from match_and_rename import compare_and_rename
from fetch_playlist import fetch_playlist_items

playlist_url = get_data_from_user(
    "Please Enter the playlist url : ",
    lambda message: (message.startswith(
        "https://www.youtube.com/playlist")) and "list" in message,
    "Please Provide valid url, go to the playlist customized page and copy the link")

items = fetch_playlist_items(playlist_url)
print("\nloading playlist videos from the web\n")

playlist_dir = get_data_from_user(
    "Please Enter the folder path of the playlist : ",
    lambda dir: os.path.exists(dir),
    "it seems like you have more files in this folder than the videos in the playlist")

files = os.listdir(playlist_dir)

if len(files) < len(items) :
    items= items[0:len(files)-1]
    print_c(f"""\n\t\t\tYou have only {len(files)} files in your folder,\n\t\t\tI will rename them only assuming that they are the first {len(files)} in the list\n""",
            MessageState.Warning)

for item in items:
    title = item['snippet']['title']
    position = item["snippet"]['position']
    response_state = compare_and_rename(title, position, files, playlist_dir)
    if response_state == ResponseState.Success:
        print_c(
            f"{format_position(position)} - {title} Renamed Successfully.", MessageState.Success)
    elif response_state == ResponseState.Error:
        print_c(
            f"{format_position(position)} - {title} Renamed Failed.", MessageState.Error)

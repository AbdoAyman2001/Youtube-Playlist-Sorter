import os
import requests
from utils import parse_url_for_playlist_id
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")

def merge_two_dicts(large_dict:dict,small_dict:dict):
    # merging the tokens
    large_dict["nextPageToken"] = small_dict.get("nextPageToken")
    large_dict["prevPageToken"] = small_dict.get("prevPageToken")

    # merging the items
    if large_dict.get("items") == None :
        large_dict["items"] = small_dict["items"]
    else :
        large_dict["items"] = large_dict["items"] + small_dict["items"]

    # merging pageInfo
    large_dict['pageInfo'] = small_dict["pageInfo"]


def fetch_playlist_items(playlist_url):
    playlist_id = parse_url_for_playlist_id(playlist_url)
    next_page_existed = False
    prev_page_existed = False
    data ={}
    while(not((not next_page_existed)and prev_page_existed)):
        headers ={
                "Accept": "application/json"
            }
        params  ={
            "part":"snippet",
            "fields":"items(snippet(title,position)),pageInfo,nextPageToken,prevPageToken",
            "playlistId":playlist_id,
            "key":API_KEY,
            "maxResults":50,
            "pageToken":""
            }
        if next_page_existed : 
            params["pageToken"] = data.get("nextPageToken") 
        resp = requests.get(
            "https://youtube.googleapis.com/youtube/v3/playlistItems",
            headers=headers,
            params=params
        )

        if(resp.status_code!=200): 
            print(resp.json())
            break
            
        resp_data :dict= resp.json()

        next_page_existed = bool(resp_data.get("nextPageToken"))
        prev_page_existed = bool(resp_data.get("prevPageToken"))

        merge_two_dicts(data,resp_data)

        if len(data.get("items")) == data["pageInfo"]["totalResults"] :
            break

    return data['items']

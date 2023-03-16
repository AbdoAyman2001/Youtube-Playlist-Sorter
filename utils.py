from enum import Enum
import colorama
from colorama import Fore
colorama.init()

class ResponseState(Enum):
    Success = "success"
    Error = "error"
    Warning = "warning"

class MessageState(Enum):
    Warning = "warning"
    Success = "success"
    Error = "error"

def get_data_from_user(message: str, validation_function,error_message):
    data = input(message)
    while not validation_function(data):
        print_c(error_message)
        data = input(message)
    return data

def parse_url_for_playlist_id(url):
    list_param = url.split("list=")[-1]
    if "&" not in list_param:
        return list_param
    return list_param.split("&")[0]

def format_position(number):
    if number<10:
        return "#00"+str(number)+" "
    elif number < 100:
        return "#0"+str(number)+" "
    else :
        return "#"+number+" "

def replace_symbols(text:str):
    forbidden_symbols ="#%&}{\\/?*<>$!’'\":@+-`|="
    for symbol in forbidden_symbols: 
        text = text.replace(symbol,"_",100)
    return text

def get_file_extension (file:str):
    return "."+file.split(".")[-1]

def print_c(message,state:MessageState):
    if(state == MessageState.Error):
        print(Fore.RED+message+Fore.RED)
    elif (state == MessageState.Success):
        print(Fore.GREEN + message + Fore.GREEN)
    elif (state == MessageState.Warning):
        print(Fore.YELLOW + message + Fore.YELLOW)

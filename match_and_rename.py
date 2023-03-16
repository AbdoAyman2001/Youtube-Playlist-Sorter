import os
from utils import (format_position,
                   get_file_extension,
                   replace_symbols,
                   print_c,
                   ResponseState,
                   MessageState)

from algorithms import (jaccard_similarity,
                        jaro_winkler_distance,
                        levenshtein,
                        hamming_distance,
                        cosine_similarity,
                        soft_tfidf_similarity
                        )

def find_title_in_files(title, files: list):
    options = {}
    for file in files:
        options[file] = (
            soft_tfidf_similarity(title, file) +
            jaccard_similarity(title, file) +
            hamming_distance(title, file) +
            levenshtein(title, file) +
            jaro_winkler_distance(title, file) +
            cosine_similarity(title, file)
        )

    found_file = min(options.items(), key=lambda x: x[1])
    found_file = found_file[0]
    return found_file


def compare_and_rename(title, position, files, playlist_dir):
    file = find_title_in_files(title, files)
    old_file_path = os.path.join(playlist_dir, file)
    file_order = format_position(position)
    file_extension = get_file_extension(file)
    new_filename = file_order+replace_symbols(title)+file_extension
    new_file_path = os.path.join(playlist_dir, new_filename)
    
    if (file.startswith("#")):
        print_c(f"{file} Already Renamed", MessageState.Warning)
        return ResponseState.Warning
    try:
        os.rename(old_file_path, new_file_path)
        return ResponseState.Success
    except:
        return ResponseState.Error

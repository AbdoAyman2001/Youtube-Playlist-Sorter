
def levenshtein(s1, s2):
    # create matrix
    rows = len(s1) + 1
    cols = len(s2) + 1
    matrix = [[0 for j in range(cols)] for i in range(rows)]
    
    # initialize matrix
    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j
    
    # fill matrix
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            matrix[i][j] = min(matrix[i-1][j] + 1, # deletion
                               matrix[i][j-1] + 1, # insertion
                               matrix[i-1][j-1] + cost) # substitution
    
    # return bottom right value
    return matrix[rows-1][cols-1]

def hamming_distance(str1, str2):
    # Find the length of the shorter string
    length = min(len(str1), len(str2))

    # Calculate the Hamming distance
    distance = 0
    for i in range(length):
        if str1[i] != str2[i]:
            distance += 1

    # Add the difference in length between the two strings, if any
    distance += abs(len(str1) - len(str2))

    return distance


def jaro_winkler_distance(s1, s2, prefix_weight=0.1, max_prefix_length=4):
    # Calculate Jaro Distance
    match_distance = (max(len(s1), len(s2)) // 2) - 1
    s1_matches = [False] * len(s1)
    s2_matches = [False] * len(s2)
    matches = 0
    transpositions = 0
    for i in range(len(s1)):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len(s2))
        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = True
            s2_matches[j] = True
            matches += 1
            break
    if matches == 0:
        return 0.0
    transpositions = 0
    k = 0
    for i in range(len(s1)):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1
    transpositions /= 2
    
    # Calculate Jaro-Winkler Distance
    jaro_distance = (matches / len(s1) + matches / len(s2) + (matches - transpositions) / matches) / 3
    prefix_length = 0
    for i in range(min(max_prefix_length, min(len(s1), len(s2)))):
        if s1[i] != s2[i]:
            break
        prefix_length += 1
    jaro_winkler_distance = jaro_distance + prefix_length * prefix_weight * (1 - jaro_distance)
    return jaro_winkler_distance


def jaccard_similarity(s1, s2):
    # convert strings to sets of tokens
    s1_tokens = set(s1.split())
    s2_tokens = set(s2.split())
    
    # calculate intersection and union of sets
    intersection = len(s1_tokens.intersection(s2_tokens))
    union = len(s1_tokens.union(s2_tokens))
    
    # calculate Jaccard similarity coefficient
    jaccard_coefficient = intersection / union
    
    return jaccard_coefficient



import math

def cosine_similarity(s1, s2):
    # convert strings to sets of tokens
    s1_tokens = set(s1.split())
    s2_tokens = set(s2.split())
    
    # create set of all tokens
    all_tokens = s1_tokens.union(s2_tokens)
    
    # create vector representations of strings
    s1_vector = [int(token in s1_tokens) for token in all_tokens]
    s2_vector = [int(token in s2_tokens) for token in all_tokens]
    
    # calculate dot product and magnitudes of vectors
    dot_product = sum([s1_vector[i] * s2_vector[i] for i in range(len(all_tokens))])
    s1_magnitude = math.sqrt(sum([x**2 for x in s1_vector]))
    s2_magnitude = math.sqrt(sum([x**2 for x in s2_vector]))
    
    # calculate cosine similarity
    cosine_similarity = dot_product / (s1_magnitude * s2_magnitude)
    
    return cosine_similarity


import math

def soft_tfidf_similarity(str1, str2):
    # tokenize the strings
    tokens1 = str1.lower().split()
    tokens2 = str2.lower().split()

    # get the set of unique words in both strings
    unique_words = set(tokens1 + tokens2)

    # calculate the term frequency of each word in each string
    tf1 = {}
    tf2 = {}

    for word in unique_words:
        tf1[word] = tokens1.count(word) / len(tokens1)
        tf2[word] = tokens2.count(word) / len(tokens2)

    # calculate the document frequency of each word
    df = {}

    for word in unique_words:
        df[word] = 0
        if word in tokens1:
            df[word] += 1
        if word in tokens2:
            df[word] += 1

    # calculate the Soft-TFIDF score for each word in each string
    soft_tfidf1 = {}
    soft_tfidf2 = {}

    for word in unique_words:
        idf = math.log((2 + 1) / (df[word] + 1)) + 1
        soft_tf1 = (1 + tf1[word]) / (1 + max(list(tf2.values())))
        soft_tf2 = (1 + tf2[word]) / (1 + max(list(tf1.values())))
        soft_tfidf1[word] = soft_tf1 * idf
        soft_tfidf2[word] = soft_tf2 * idf
    
    # calculate the Soft-TFIDF similarity between the two documents
    similarity = sum(soft_tfidf1[word] * soft_tfidf2[word] for word in unique_words)

    return similarity
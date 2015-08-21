"""Problem from Vicarious: Given a start and stop word, transform the start word one letter at a time so that it becomes the stop word, while each intermediary transformation must be an English word itself."""

# There are likely many more permutations than there are words in the dictionary.  Iterate across the dictionary looking for words of the same length.

from nltk import download           # Download dictionary of English words
from nltk.corpus import words       # Dictionary of English words
from string import ascii_lowercase  # Iterate through the alphabet
from collections import OrderedDict # Make the outcome deterministic by using an ordered dictionary

def iterate_level(start_word, same_length_words, graph):
    """Iterate one depth into the graph of generated word connections.  The start_words are the words whose connetions should be filled out.  A connection will be made with all words that are in the given same_length_words that are only one character different.  Returns a list of the words whose connections were added on this iteration."""
    added_connections = []
    if start_word not in graph:
        graph[start_word] = ([], [])
        added_connections += [start_word]
        for same_length_word in same_length_words:
            if one_character_different(start_word, same_length_word):
                graph[start_word] = (graph[start_word][0] + [same_length_word], graph[start_word][1])
    return added_connections

def one_character_different(word1, word2):
    """Return true if the two given words are only one character different from one import another.  False otherwise."""
    i = 0
    differences = 0
    for character1 in word1:
        if differences > 1:
            return False
        if character1 != word2[i]:
            differences += 1
        i +=1
    if differences == 1:
        return True
    else:
        return False

def transform_word(start_word, stop_word):
    """Given a starting word, transform it one letter at a time into the stop word where each intermediary transformation is also an English word."""
    word_connections = {} # A dictionary where keys map to tuples ([connections], [path back to the root node])
    download('words')               # Download the English dictionary
    if len(start_word) != len(stop_word):
        raise ValueError("This algorithm is only suitable for transforming words of the same length.")
    if start_word.lower() != start_word or stop_word.lower() != stop_word:
        raise ValueError("This algorithm only deals with lower case words.")
    if start_word not in words.words() or stop_word not in words.words():
        raise ValueError("It's expected that the beginning and ending words are English words.")

    # Create dictionary of all words that are the same length as the given word
    same_length_words = []
    for word in words.words():
        if len(word) == len(start_word):
            same_length_words += [word.lower()]
    
    start_words = OrderedDict({start_word : None})  # An ordered dictionary where the value is the word to be iterated on and the value is the path taken to get here in the graph

    while(len(start_words) > 0):
        item = start_words.popitem(last=False)  # Take the first item added to this dictionary to maintain breadth first search
        current_word = item[0]
        who_added_me = item[1]
        iterate_level(current_word, same_length_words, word_connections)
        if len(word_connections[current_word][0]) > 0:  # Update the path traveled to get here
            if who_added_me:
                word_connections[current_word] = (word_connections[current_word][0], word_connections[who_added_me][1] + [who_added_me])
        for new_connection in word_connections[current_word][0]:
            if new_connection == stop_word:
                print("It's possible to make the transformation with {}".format(word_connections[current_word][1] + [current_word] + [stop_word]))
                return word_connections[current_word][1] + [current_word] + [stop_word]
            if new_connection not in word_connections and new_connection not in start_words:
                start_words[new_connection] = current_word
        start_words.pop(current_word, None)

    print("There is no possible connection between {} and {}".format(start_word, stop_word))


"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_paths):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    all_text =""
    for f in file_paths:
        with open(f) as text:
            all_text += text.read()

    return all_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # empty dictionary
    chains = {}

    # making a list of words in the string 
    all_words = text_string.split()

    # giving us the word with it's index 
    for idx in range(len(all_words)-2):
        # print idx, all_words[idx + 1],all_words[idx + 2]
        # makes a key of word and the following word
       

        # checking to see if key is in dictionary. 
        #If exits, update value. If it doesn't exists, initiate value with empty list
        # appends first value to the list 
        
        # while idx < len(all_words)-3:
        key = (all_words[idx], all_words[idx+1])
        if key in chains:
            chains[key].append(all_words[idx + 2])
        else:
            chains[key] = [all_words[idx + 2]]
        # print key, all_words[idx+2]
        # chains.get(key, []).append(all_words[idx+2])



    return chains

def make_ngrams(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # empty dictionary
    chains = {}

    # making a list of words in the string 
    all_words = text_string.split()
    for idx in range(len(all_words)-n):
        key = tuple(all_words[idx:(idx + n)])
        if key in chains:
            chains[key].append(all_words[idx + n])
        else:
            chains[key] = [all_words[idx + n]]
    return chains


def make_text(chains, n):
    """Return text from chains."""

    init_words = choice(chains.keys()) 
    words = list(init_words)
    while True:
        try:
            key = tuple(words[-n:])
            value = choice(chains[key])
            words.append(value)
            if len(words) > 50:
                break
        except KeyError:
            break
    print " ".join(words)


# input_path = "green-eggs.txt"

# text_string = open_and_read_file(input_path)

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1:-1])
# print input_text
# Get a Markov chain
# chains = make_chains(input_text)
chains = make_ngrams(input_text, int(sys.argv[-1]))
# print chains
# # Produce random text
# random_text = make_text(chains)

# print random_text
make_text(chains, int(sys.argv[-1]))
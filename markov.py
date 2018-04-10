"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # all_text = ""
    with open(file_path) as text:
        all_text = text.read()
        # for line in text:
        #     line = line.strip()
        #     # words = line.split()
        #     all_text += (line + " ")

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


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# text_string = open_and_read_file(input_path)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# Get a Markov chain
chains = make_chains(input_text)
print chains
# # Produce random text
# random_text = make_text(chains)

# print random_text

import random

def get():
    f = open("words.txt", "r")
    file = (f.read())
    lines = file.splitlines()
    return lines


def words_of_length():
    
    
    
    with open("words_of_length.txt") as f:
        words = get()
        
        for word in words:
            if len(word)>3:
                f.write(word)
words_of_length()
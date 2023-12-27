import random

#reads file of words sourced online
def get():
    f = open("words.txt", "r")
    file = (f.read())
    lines = file.splitlines()
    return lines





#writes new file of words of length > 3
def correct_length():
    
    new = []
    
    words = get()
    outfile = open("words_of_length.txt", "w")
    
    for word in words:
        if len(word)>3:
            new.append(word)
            outfile.write(f"{word}\n")
    
    
    outfile.close()
    return new


def finder(letter, word):
    # IN letter word
    # OUT where
    locations = []
    
    for index, char in enumerate(word):
        if char == letter:
            
            locations.append(index)
    return locations
    



def game():
    
    words = correct_length()
    
    word = random.choice(words)

    
    count = 0
    
    guess = ['_ ' for _ in range(len(word))]
    
    while '_ ' in guess:
        
        letter = input("guess a letter :")
        count+=1
        
        if letter in word:
            letter_locations = finder(letter, word)
            
            for i in letter_locations:
                guess[i] = letter
        print(' '.join(guess), '\n\n')
    
    print(f"correct, you guessed '{word}' in {count} guesses")




def main():
    
    play = input("do you want to play handman [ Y / N ]")
    
    while play == 'Y':
        
        game()

        play = input("again? [ Y / N ]")
main()
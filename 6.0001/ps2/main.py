# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
		# FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
      if not char in letters_guessed:
        return False
    return True 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output = ""
    for char in secret_word:
      if not char in letters_guessed:
        output += " _"
      else:
        output += char
    return(output)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output = ""
    for char in string.ascii_lowercase:
      if not char in letters_guessed:
        output += char
    return(output) 
   

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(secret_word), " letters long")
    print("You have ", warnings, " warnings left")
    print("--------------------")
    while guesses > 0:
      print("You have ", guesses, " guesses left")
      print("Available letters: ", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ").lower()

      if not str.isalpha(guess): #check is a letter
        if warnings >= 1:
          print("Oops! That is not a valid letter. You have ", warnings, " left")
          print("--------------------")
          warnings -= 1
        else:
          guesses -= 1
          print("Oops! That is not a valid letter. You have 0 warnings left so you lose a guess")
          print("--------------------")
        guesses -= 1

      elif guess in letters_guessed: #check isn't already guessed
        print("Oops! You already guessed that letter.")
        if warnings >= 1:
          warnings -= 1
          print("You have warnings ", warnings, " left")
          print("--------------------")
        else:
          guesses -= 1
          print("You have 0 warnings left so you lose a guess")
          print("--------------------")

      else:
        letters_guessed.append(guess)
        if guess in secret_word:
          print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
          print("--------------------")
        else:
          print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
          if guess in ["a", "e", "i", "o", "u"]:
            guesses -= 2
          else:
            guesses -= 1
          print("--------------------")

      if is_word_guessed(secret_word, letters_guessed):
        score = guesses * len(secret_word)
        print("You won! Your score is: ", score)
        break
    if not is_word_guessed(secret_word, letters_guessed):
      print("Sorry, you ran out of guesses. The word was ", secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    my_word = my_word.replace(" ", "")
    while i <= len(my_word) - 1:
      if len(my_word) != len(other_word):
        return False
      if my_word[i] != "_" and other_word[i] != my_word[i]:
        return False
      if my_word[i] == "_" and other_word[i] in my_word:
        return False
      i += 1
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):
        possible_matches.append(other_word)
    if possible_matches != []:
      print(' '.join(possible_matches))
    else:
      print("No matches found")
      print("--------------------")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(secret_word), " letters long")
    print("You have ", warnings, " warnings left")
    print("--------------------")
    while guesses > 0:
      print("You have ", guesses, " guesses left")
      print("Available letters: ", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ").lower()
      
      if guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))

      elif not str.isalpha(guess): #check is a letter
        if warnings >= 1:
          print("Oops! That is not a valid letter. You have ", warnings, " left")
          print("--------------------")
          warnings -= 1
        else:
          guesses -= 1
          print("Oops! That is not a valid letter. You have 0 warnings left so you lose a guess")
          print("--------------------")
        guesses -= 1

      elif guess in letters_guessed: #check isn't already guessed
        print("Oops! You already guessed that letter.")
        if warnings >= 1:
          warnings -= 1
          print("You have warnings ", warnings, " left")
          print("--------------------")
        else:
          guesses -= 1
          print("You have 0 warnings left so you lose a guess")
          print("--------------------")

      else:
        letters_guessed.append(guess)
        if guess in secret_word:
          print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
          print("--------------------")
        else:
          print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
          if guess in ["a", "e", "i", "o", "u"]:
            guesses -= 2
          else:
            guesses -= 1
          print("--------------------")

      if is_word_guessed(secret_word, letters_guessed):
        score = guesses * len(secret_word)
        print("You won! Your score is: ", score)
        break
    if not is_word_guessed(secret_word, letters_guessed):
      print("Sorry, you ran out of guesses. The word was ", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #secret_word = "apples"
    hangman_with_hints(secret_word)

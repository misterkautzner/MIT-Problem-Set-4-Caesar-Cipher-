# 6.00 Problem Set 4
#
# Name: John Kautzner
# Collaborators: None
# Time: 7:00
#
# Caesar Cipher Skeleton
#

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.

    code = {}

    code.update({' ':chr(put_in_range(32, shift))})

    for i in range(97, 123):
        code.update({chr(i):chr(put_in_range(i, shift))})

    for i in range(65, 91):
        code.update({chr(i):chr(put_in_range(i, shift))})

    return code



def test_build_coder_3():
    """
    Tests dictionary created by build_coder(3) against what it should be.
    
    Returns an affirmative message if all values in the build_coder(3) dict are correct.
    Returns incorrect values and a negative message if the dictionary isn't correct.

    Note: Doesn't return negative message or missing values if values are missing, so it can check a
          partial dict.
    """

    trial = {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}

    bc_dict = build_coder(3)
    same = True

    print

    for key in bc_dict:
        if(bc_dict[key] != trial[key]):
            same = False
            print "trial[", key, "] = ", trial[key], "  bc_dict[", key, "] = ", bc_dict[key]

    if(same == False):
        return "Dictionaries are NOT the same."

    return "It checks out.  Dictionaries ARE the same."
    

def put_in_range(ord_number, shift):
    """
    Returns appropriate ord() number given an ord() number and the shift.
    Useful for the numbers that go out of character range when shifted.

    shift:    -27 < int < 27
    """
    assert shift > -27
    assert shift < 27
    
    if(shift < 0):      # Converts negative shifts into a positive shift
        shift += 27
    
    if(ord_number in range(65, 91)):  # Capital range
       small = 65
       big = 90

    else:       # Lowercase range
       small = 97
       big = 122
    

    if(ord_number + shift == big + 1):  # When it maps to ' '
        return 32

    if(ord_number + shift > big + 1):   # When the mapping exceeds the end of the alphabet
        return ord_number + shift - 27



 #   elif(ord_number + shift < small):  # When the mapping falls short of the alphabet
  #      if(ord_number + shift == small - 1): # Maps to ' '
   #         return 32

    if(ord_number == 32):
        if(shift > 0):
            return 96 + shift

        else:
            return 32
                               
  #  else:
   #     return big + shift

    else:                           # Normal (within range)
        return ord_number + shift



    

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.

    assert shift >= 0
    return build_coder(shift)

    # I'm not sure what the difference between these to functions is supposed to be
    #   other than the fact that this one only accepts positive values.
    

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.

    shift = -(shift)
    return build_coder(shift)



def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.

    newText = ''

    for character in text:
        if(character in coder):
            newText += coder[character]

        else:
            newText += character

    return newText
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.

    return apply_coder(text, build_coder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO

    

    key = 0
    maxWords = 0
    word = ''
    currentWords = 0
    k = ''

    for s in range(0, 27):
        dText = apply_coder(text, build_decoder(s)) + ' '
       # print dText #

        for character in dText:
            if(character == ' ' or character in set(string.punctuation)):
                if(is_word(wordlist, word)):
                   # print
                   # print "word = ", word
                    currentWords += 1
                    word = ''
                   # print currentWords
                    
            else:
                word += character

        if(currentWords > maxWords):
            maxWords = currentWords
            key = s

        word = ''
        currentWords = 0

   # print
   # print apply_coder(text, build_decoder(key))
    return key



def test_find_bs(times, n):
    """
    Tests find_best_shift() with a chosen number of ciphertexts (each with n words)
    Prints keys and plaintexts

    times:  int
    n:  int
    """

    print
    
    for t in range(0, times + 1):
        cText = random_cT(wordlist, n)
       # print "cText = ", cText
        s = find_best_shift(wordlist, cText)
        print "pText = ", apply_shift(cText, -s)
        print

def random_cT(wordlist, n):
    """
    Returns random ciphertext whose plaintext has n words

    n:  int
    """

    s = random_string(wordlist, n) + " "
    shift = random.randint(0, 26)
    return apply_shift(s, shift)[:-1]
   
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.

    for s in shifts:
       # print "untouched = ", text[:s[0]], "   changed = ", apply_shift(text[s[0]:], s[1])
        text = text[:s[0]] + apply_shift(text[s[0]:], s[1])

    return text
 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    ### TODO.

    return find_best_shifts_rec(wordlist, text, 0)

def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)

    find_best_shifts_rec(wordlist, 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?', 0)
    """
    ### TODO.

    shifts = []

    for shift in range(0, 27):
        
        s = text[:start] + apply_shift(text[start:], shift)
        print "shift = ", shift, "    ", s

        word = ''
        
        for i in range(start, len(s)):
            
            if(s[i] == ' ' and is_word(wordlist, s[start:i])):
                print
                print "s[start:i] = ", s[start:i]
                #find_best_shifts_rec(wordlist, s, i+1)

              #  print "s = ", s
               # print "i+1 = ", i+1

                value = find_best_shifts_rec(wordlist, s, i+1)
                
                if(value != None):
                    shifts = [(i+1, shift)] + find_best_shifts_rec(wordlist, s, i+1) # start instead of i? or i+1?
                    print "shifts = ", shifts
                    return shifts

                else:
                    print "Breaker 1"
                    break
            

            if(s[i] != ' ' and is_word(wordlist, s[start:])):
                print "s[start:] = ", s[start:]
                print
                print "returning [(", start, ",", shift, ")]"
                print
                print
                return [(start, shift)]

       # if(s[i] != ' ' and not is_word(wordlist, s[start:])):
        #    print "Breaker 2"
         #   break

            
    print
    print
    print "Here it comes!!!"
    print
    print
        
    for t in shifts:
        print "t = ", t
        if(t[1] == 0):
            shifts.remove(t)

    
    print "Final s = ", s
    return None

"""
    shifts = []

    for shift in range(0, 27):
        s = text[:start] + apply_shift(text[start:], shift)
        print "shift = ", shift, "    ", s

        word = ''

        for i in range(start, len(s)):
            print "i = ", i, "    s[i] = ", s[i]
            if(s[i] in set(string.punctuation)):
              print
              print "Punctuation!!!"
              print
              
            if((s[i] == ' ' or s[i] in set(string.punctuation)) and is_word(wordlist, word)):
                print
                print "word = ", word
                print
                shifts += find_best_shifts_rec(wordlist, s, i + 1)
                
                if(find_best_shifts_rec(wordlist, s, i + 1) == None):
                    
                    break

                else:
                   shifts = [(i, shift)] + shifts
                   print "shifts = ", shifts
                   return shifts

                            
            else:
                word += s[i]
                #print "shift = ", shift, "   word = ", word
            

            if(s[i] != ' ' and is_word(wordlist, s[start:])):
                print  "s[start:] = ", s[start:]
                print
                print "The end!!!!"
                print
                print
                return [(start, shift)]

            
    print
    print
    print "Here it comes!!!"
    print
    print
        
    for t in shifts:
        print "t = ", t
        if(t[1] == 0):
            shifts.remove(t)

    
    print "Final s = ", s
    return None

shifts = [(2, 21), (11, 9), (17, 11), (20, 0), (29, 0), (30, 0)]
"""
    


def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.



    
#What is the moral of the story?
#
#
#
#
#


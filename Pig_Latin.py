# pyglatin bitches

string = input('Enter a word: ')

# string_ascii = [ord(letter) for letter in string]

def convert_to_pyg(string):
    for i in string:
        if i in 'aeiou':
            vowel_index = string.index(i)
            consonant = string[:vowel_index]
            pigged_string = string[vowel_index:] + consonant + 'ay'
            return pigged_string

def separate_words(string):
    pigs = [convert_to_pyg(word) for word in string.split() if ' ' in string]
    print(' '.join(pigs))
### Second Challenge ###

"""
is it an anagram?:
Write a function, it takes to params a string, return true or false if they are an anagram
-An anagram is a different word that uses the same letters as another word
-You don't need to check that both words exist
-2 Identical words aren't an anagram
"""

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower(): return False
    return sorted(first_word.lower()) == sorted(second_word.lower())
print(is_anagram("Hello","hellow"))
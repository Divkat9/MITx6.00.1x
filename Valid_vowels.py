from re import search

def vowel_count(string):
    vowels = ["a", "e", "i", "o", "u"]
    return len([i for i in string if i in vowels])

print(vowel_count("apple"))




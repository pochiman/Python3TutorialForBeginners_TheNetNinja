from random import shuffle

def jumble(word):
    anagram = list(word)  # This turns a word into a list of characters. ['b', 'e', 'e', 't', 'r', 'o', 'o', 't']
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# for loop method
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

# map method
print (list(map(jumble, words)))  # It's gonna cycle through words and it's going to perform this jumble function
                                  # on each one of these individual items that then it's going to spit them back out.

# comprehension method
print([jumble(word) for word in words])

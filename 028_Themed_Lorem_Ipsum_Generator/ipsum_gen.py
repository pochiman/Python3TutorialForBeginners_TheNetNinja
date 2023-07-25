'''

We're going to read from ipsum.txt
- then we're going to separate this into a list and each word is going to be in this list as an element 
- then we're going to run this list through some kind of map function whereby we're going to associate 
each word with a ninja word as well and output that to a new list 
- so we're going to have some randomly injected ninja themed words within this ipsum text and we're going 
- to then write that text to this ninja_ipsum file right here.

'''

from random import randint

ninja_words = [
    'Aki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haibo', 
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko' 
]

def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f'{word} {ninja_words[random_pos]}'


paragraphs = int(input('How many paragraphs of ninja ipsum: '))

with open('028_Themed_Lorem_Ipsum_Generator/ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()  

    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))
        with open('028_Themed_Lorem_Ipsum_Generator/ninja_ipsum.txt', 'a') as ipsum_ninja:
            ipsum_ninja.write(' '.join(ninja_text) + '\n\n')

'''

We're going to read it and once we've read that, we're going to get a string and we're going to split that string 
and that's going to put each word as an element into a list so this now is going to be a list of words.

Then we'll cycle through those words and somehow associate each word with a random ninja word.

So each time around through one of these paragraphs we want to associate these ipsum words with some ninja words to mix it up.


SUMMARY:
- First of all, we're asking the user how many paragraphs they want and we're converting that to an integer.
- Then we're opening ipsum.txt and we're reading that text and we're splitting up that string that we get back into an items list.
- So this items list is going to be a list of those individual words inside that vanilla lorem ipsum text.

- Then we're going to use a for loop to cycle through how many paragraphs we have requested (3) and each time around, what we're doing
is we're saying this variable ninja_text is going to be equal to a list.
- Then we're going to map the current items (the original list of words).
- We're going to pass each of those items into this ninjarize() function which is getting a random integer (between 0 and 13 in this case) 
to select a random ninja word then we're placing that ninja word next to the original vanilla lorem ipsum word, placing those two together 
in a string and we're returning that string so those returned strings are then stored in this ninja_text list right here.

- Then we're opening this ninja_ipsum text file. We're saying we want to amend to that file each time around so we can write to it.
- We refer to that as ipsum_ninja then we say we want to write to it and we want to join everything together inside this ninja_text list 
so every set of words inside this list right here we're joining together and the connector is going to be this ' ' space so in between 
each set of words there's going to be a ' ' space then we're adding on these line breaks at the end of all of that paragraph so the 
next paragraph is a couple of lines down so we're cycling through that and doing that for as many times as we requested.
- Then we get this ninja_ipsum.txt file.

'''                              
'''

'w' --- needs to be added to write to a file since by default, the write.txt file is read only.
'a' --- needs to be added to amend to a file.

'''

with open('027_Writing_Files/files/write.txt', 'w') as write_file:
    write_file.write('Hey there ninjas, python is awesome')

# junk

with open('027_Writing_Files/files/write.txt', 'a') as write_file:
    write_file.write('\nI love it so much, I dream in python')

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlwats forgive your enemies - nothing annoys them so much'
]

with open('027_Writing_Files/files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)  # writelines expects as an argument inside this function some kind of list then 
                                   # it's going to cycle through that list and write out each element to the document.
                                   
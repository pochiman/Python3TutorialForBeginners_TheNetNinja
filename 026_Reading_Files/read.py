ipsum_file = open('026_Reading_Files/files/ipsum.txt')

for line in ipsum_file:
    print(line.rstrip())  # rstrip strips out line breaks

ipsum_file.seek(0)  # sets the cursor to the very start of the file
    
lines = ipsum_file.readlines()  # stores lines in a list
print(lines)

ipsum_file.seek(50)  # sets the start counter at char 50
file_text = ipsum_file.read(100)  # reads 100 char starting from char 50
print(file_text)

ipsum_file.close()

# alternate way to read files - auto closes file
def sequence_filter(line):
    return '>' not in line

with open('026_Reading_Files/files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))

'''

Apply this filter to this list:
- filter --- then we pass in the function we want to use to filter this list --- sequence_filter
- then we pass in what list we want to run through this filter --- lines --- so we're filtering those now
- then we typecast this filter into a list because otherwise it returns some kind of filter object --- list

- so first of all we're reading the lines from this file with it open 
- then we're using this sequence_filter on the lines, passing each line in one at a time 
- we're looking for this > closing angle bracket
- if it is not in the line, then we're going to keep that in the list
- if it is in the line, we're going to take it away because we don't want these > things in the final list 
so we're filtering out those lines
- then we're typecasting that filter into a list and printing it to the console. 

'''
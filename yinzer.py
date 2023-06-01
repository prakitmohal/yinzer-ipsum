import random

# figure out what our enum is
def getEnum(enum,length):

	newEnum = enum

	while(enum == newEnum):

		newEnum = random.randint(0,length-1)

	return newEnum

# read in the text file
file = open("wordlist.txt", "r")
wordlist = file.readlines()
file.close()

# strip out extraneous line breaks
for line in wordlist:
	line = line.strip()

# we don't want to repeat words that's awkward
length = len(wordlist)
enum = 0

# Parameters: 1 Paragraph, 5 Sentences, each sentence has 7-9 phrases
for x in range(5):

	# Capitalize the first word
	enum = getEnum(enum,length)
	firstWord = wordlist[enum].strip()
	firstWord = firstWord[0].upper() + firstWord[1:]
	print(firstWord, end=' ')

	# Get the next set of words
	for y in range(random.randint(7,9)-2):

		enum = getEnum(enum,length)
		print(wordlist[enum].strip(), end=' ')

	# Print the last word
	enum = getEnum(enum,length)
	print(wordlist[enum].strip(), end='. ')

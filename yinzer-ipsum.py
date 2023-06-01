import random

# repeating words suck, lets prevent that
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

length = len(wordlist)
enum = 0

print()
paragraphs = int(input("How many paragraphs do yinz need n'at?: "))
print()

# loop over number of paragraphs
for i in range(paragraphs):

	# Parameters: 5 Sentences, each sentence has 8 phrases
	for x in range(5):

		# Capitalize the first word
		enum = getEnum(enum,length)
		firstWord = wordlist[enum].strip()
		firstWord = firstWord[0].upper() + firstWord[1:]
		print(firstWord, end=' ')

		# Get the next set of words
		for y in range(6):

			enum = getEnum(enum,length)
			print(wordlist[enum].strip(), end=' ')

		# Print the last word
		enum = getEnum(enum,length)
		print(wordlist[enum].strip(), end='. ')

	print("\n")



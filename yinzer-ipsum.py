import random
import requests

# repeating words suck, lets prevent that
def getEnum(enum,length):

	newEnum = enum
	while(enum == newEnum):
		newEnum = random.randint(0,length-1)
	return newEnum

# read in the text file
url = 'https://raw.githubusercontent.com/prakitmohal/yinzer-ipsum/main/wordlist.txt'
response = requests.get(url)
rawdata = response.text

# strip out extraneous line breaks
index = 0
wordlist = {}

for line in rawdata.split('\n'):
	wordlist[index] = line
	index = index + 1

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

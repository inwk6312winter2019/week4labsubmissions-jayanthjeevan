import string

fp=open('watson.txt')
name=fp.read()
for line in name.split():
	word=line.strip(string.punctuation)
	print(word.lower())

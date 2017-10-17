import sys
my_words = 'Hello world my name is Deepak Panta. Hello this means that my name has D in it and it is awesome to see it '.split(' ')
for line in my_words:
	line = line.strip()
	words = line.split()
	for word in words:
		print ('{}\t{}'.format(word,1))
		
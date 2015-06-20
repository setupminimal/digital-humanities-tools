#! /usr/bin/env python

def clean(word):
	word = word.lower()
	word = word.replace("'", "").replace('"', "").replace(".", "")
	word = word.replace(",", "").replace(";", "").replace("!", "")
	word = word.replace("?", "").replace("(", "").replace(")", "")
	word = word.replace(":", "")
	return word

file = raw_input("What file should we replace words in? ")
repl = raw_input("Where is the list of words to replace? ")
word = raw_input("And what should we replace them with? ")
outp = raw_input("And where should we put the result when we finish? ")

with open(file) as f:
	file = f.read()

words = file.split()

with open(repl) as f:
	repl = f.read()

repl = repl.split()
with open(outp, "w") as f:
	for item in words:
		if clean(item) in repl:
			f.write(word+" ")
		else:
			f.write(item+" ")

print "All done!"

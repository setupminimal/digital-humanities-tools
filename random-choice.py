def clean(word):
    word = word.lower()
    word = word.replace("'", " ").replace('"', " ").replace(".", " ")
    word = word.replace(",", " ").replace(";", " ").replace("!", " ")
    word = word.replace("?", " ").replace("(", " ").replace(")", " ")
    word = word.replace(":", " ").replace("[", " ").replace("]", " ")
    return word

with open(raw_input("File to pick from: ")) as f:
    text = clean(f.read()).split()

text = (x for x in text if x != "xx")
text = [x for x in text if len(x) > 0]

max = int(raw_input("How many words do you want? "))

import random

print "Observe the following randomly selected words:"
for i in xrange(0,max):
    x = random.randint(0, len(text) - 1)
    print "("+str(x)+"): "+text[x]

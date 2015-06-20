x = input("What file should I look through? ")
num = input("What word number do you want? ")

with open(x) as f:
	text = f.read()

x += "word"+str(num)+".txt"

text = text.split()
result = text[num - 1: num + 3]
result = " ".join(result)

with open(x, "w") as f:
	f.write(result)

print "Here are the words around word number "+str(num)+": "
print result

print "I've saved them in "+x

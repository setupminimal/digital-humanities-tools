import csv

def clean(word):
  word = word.lower()
  word = word.replace("'", "").replace('"', "").replace(".", "")
  word = word.replace(",", "").replace(";", "").replace("!", "")
  word = word.replace("?", "").replace("(", "").replace(")", "")
  word = word.replace(":", "")
  return word

stopwords = ["a"]

with open(raw_input("The location of the stopword file: ")) as f:
  stopwords = f.read().split()

stopwords = set(stopwords)

with open(raw_input("File to parse: ")) as f:
  text = f.read().replace("[", " [").replace("]", "] ")

phrases = text.split("xx")
text = text.split()

paragraph = "inital"
phrase = 0
with open(raw_input("Output file name (ends w/ .csv): "), "w") as out:
  output = csv.writer(out, quotechar='"', doublequote=True, quoting=csv.QUOTE_NONNUMERIC)
  for word in text:
    if word.startswith("[") and word.endswith("]"):
      paragraph = word[1:len(word) - 1]
    elif word == "xx":
      phrase += 1
    elif word not in stopwords:
      output.writerow([clean(word), paragraph, phrases[phrase]])

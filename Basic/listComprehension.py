##list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
#with simple list
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)
#with list comprehension
word_lengths2 = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths2)

##Exercise : Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)
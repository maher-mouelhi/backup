sentence = input("give sentence ")
words = sentence.split(' ')
for i in range(len(words)-1,-1,-1):
    print(str(words[i]),end=' ')


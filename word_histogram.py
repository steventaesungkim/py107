#User inputs a sentence and the dictionary will collect and tally up how many times each word is used in the sentence.

sen = input("Input a sentence and it will count the words in the sentence: ").upper()
word = []
dictionary = {}
num = []


for w in str.split(sen):
    if w not in word:
        word.append(w)
for w in word:
    num.append(sen.count(w))
for w in range(len(word)):
    dictionary[word[w]] = num[w]

print(dictionary)
print()

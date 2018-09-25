#User inputs a word and the dictionary collect and tally up how many times each letter in the alphabet was used in the word.

# user = input("banana".upper())


# def letter_count(letter, count):
#     counter = 0
#     for letter in user:
#         counter += (letter == count)
#         bank.append(bank[letter : count])
#     return counter

# print(bank)
# print(bank[letter : count])

# for count in user:
#     if user == alpha[count]:
#         bank.append(alpha[user])
#         counter = 0
#         while counter < bank[counter]:
#             word_count = bank[counter].value()
#         counter += 1
    

# print(word_count)

# user = "banana"

# bank = []

# for user in alpha:
#     wordcount = user.count(alpha)

# print(wordcount)
# for letter in user:
#     bank.append(letter)
#     count = 0
#     while count < user.count(letter):
#         double = letter + letter
#     count += 1
# print(bank, end="")
# # for repeat in user:
# #     if
# 
########## - FINAL
word = input("Input a word and it will count the letters in the word: ").upper()
bank = []
counter = {}
num = []

for letter in word:
    if letter not in bank:
        bank.append(letter)
for index in bank:
    num.append(word.count(index))
for i in range(len(bank)):
    counter[bank[i]] = num[i]

print(counter)
print()


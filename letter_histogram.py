#User inputs a word and the dictionary collect and tally up how many times each letter in the alphabet was used in the word.

user = input("banana".upper())

bank = []

def letter_count(letter, count):
    counter = 0
    for letter in user:
        counter += (letter == count)
        bank.append(bank[letter : count])
    return counter

print(bank)
print(bank[letter : count])



# for count in user:
#     if user == alpha[count]:
#         bank.append(alpha[user])
#         counter = 0
#         while counter < bank[counter]:
#             word_count = bank[counter].value()
#         counter += 1
    

# print(word_count)

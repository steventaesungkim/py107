#User inputs a word and the dictionary collect and tally up how many times each letter in the alphabet was used in the word.

user = input("banana".upper())

bank = []

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","s","t","v","w","x","y","z"]

for count in user:
    if user == alpha[count]:
        bank.append(alpha[user])
        counter = 0
        while counter < bank[counter]:
            word_count = bank[counter].value()
        counter += 1
    

print(word_count)

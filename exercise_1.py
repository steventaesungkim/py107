#Practice with dictionaries.

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#1 Print elizabeth's phone number.
print(phonebook_dict["Elizabeth"])
print()

#2 Add an entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict["Kareem"] = "938-489-1234"

print(phonebook_dict, end="")
print()

#3 Delete Alice's phone entry.
del phonebook_dict["Alice"]

print(phonebook_dict, end= "")
print()

# 4 Change Bob's phone number to '968-345-2345'.


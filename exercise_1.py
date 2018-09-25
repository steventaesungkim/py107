#Practice with dictionaries.
#######
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#1 Print elizabeth's phone number.
print("Elizabeth's number: ", phonebook_dict["Elizabeth"])
print()

#2 Add an entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict["Kareem"] = "938-489-1234"

print("Kareem and Kareem's number added: ", phonebook_dict)
print()

#3 Delete Alice's phone entry.
del phonebook_dict["Alice"]

print("Alice phone entry is deleted: ", phonebook_dict)
print()

# 4 Change Bob's phone number to '968-345-2345'.
phonebook_dict["Bob"] = "968-345-2345"

print("Bob's number has been changed: ", phonebook_dict)
print()

#5 Print all the Phone entries
print("Print out all the entries: ", phonebook_dict)
print()


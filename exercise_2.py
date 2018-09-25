#Exercise 2 - Nesting dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#1 Write a python expression that gets the email address of Ramit.
print("Email address for Ramit: ", ramit["email"])
print()

#2 Write a python expression that gets the first of Ramit's interests.
print("First interest of Ramit: ", ramit["interests"][0])
print()

#3 Write a python expression that gets the email address of Jasmine.
for i in ramit["friends"]:
    if i["name"] == "Jasmine":
        print("Jasmine's email is: ", i["email"])
print()

#4 Write a python expression that gets the second of Jan's two interests.
for i in ramit["friends"]:
    if i["name"] == "Jan":
        print("Jan's second interest is: ", i["interests"][1])
print()


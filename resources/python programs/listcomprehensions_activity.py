names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in lowercased]

# bonus_case = [name.lower().title() for name in names]
bonus_case = [nameData.title() for nameData in [name.lower() for name in names]]

invitations = [f"Dear {name}, please come to the wedding this Saturday!" for name in bonus_case]
# invitations = [f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
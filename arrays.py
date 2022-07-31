letters = ['a','b','c','d','e','f','g']
print(letters)
print("Replace some values")
letters[2:5] = ['C','D','E']
print(letters)
print("now remove them")

letters[2:5] = []

print(letters)

print("Clear the list by repleacing all the elements with an empty list")
letters[:] = []
print(letters)

print("New section")

letters = ['a','b','c']
print("The array contains", len(letters))


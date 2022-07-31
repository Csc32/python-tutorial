#Arrays Methods

print("Count method")

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']

print(fruits.count("apple"))

print(fruits.count("tangerine"))

#index method
print("-" * 30)
print("Index Mehtod")
print("The index of banana is: ", fruits.index('banana'))
print("The index of the second banana is: ", fruits.index('banana', 4)) #find the next banana starting a position

print("-" * 30)
print("insert method")
fruits.insert(3,"berry")
print(fruits)

print("-" * 30)
print("remove method")
fruits.remove("banana")
print(fruits)

print("-" * 30)
print("sort method")

fruits.sort()
print(fruits)

print(type(fruits))
#print(dir(fruits))

print("-" * 30)

print("List as stack")

#Append() and pop() method

stack = [ 3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(stack)

print("-" * 30)

print("List as queues")

from collections import deque
queue = deque(['Erick','Jhon','Michael'])
queue.append('Terri')
queue.append("Grand")
print(queue.popleft())
print(queue.popleft())
print(f"The list are have the next peopels: {queue}")



print("-" * 30)

print("List comprehensions")

squares = []

for x in range(10):
    squares.append(x ** 2)
    print(squares, "\n")
    
print("-" * 30)
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

#or equivalent
squares = [x ** 2 for x in range(10)]
print("-" * 30)
print(squares)

print("-" * 30)

print([(x,y) for x in [5,6,3] for y in [3,1,4] if x != y  ])

print("-" * 30)

vec = [-4, -2, 0, 2, 4 ]
#create new list with values doubled

print([x ** 2 for x in vec])
#filter the list to exlude negatives numbers
print([x for x in vec if x >= 0])
#Apply a function to all elements
print([abs(x) for x in vec])
print("-" * 30)
#call a method  on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(weapon.strip() for weapon in freshfruit)

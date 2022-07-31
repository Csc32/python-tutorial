# For statements

names = ['Carlos','Pedro','juan']

for name in names:
    print("Welcome", name, len(name))

#create a sample collection

users = {'Hans':'active','Leo':'inactive', 'Jose': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(users)

#Strategy : Create a new collection

actives_users = {}

for user, status in users.items():
    if status == 'active':
        actives_users[user] = status


print(actives_users)
 
#Range function
for i  in range(5):
     print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100,-30)))


names2 = [{'name':'jhon', "age": 12},{'name':'Calros', "age": 15},{'name':'Maria', "age": 18}]

for i in range(len(names2)):
    print(i, names2[i])
print("-"*40)

##Search prime numbers
print("Search prime numbers")
for n in range(2,20):
    for x in range(2,n):
        if n % x == 0:  
            print(n,"Equals",x,'*',n//x)
            break   
    else:
        #Loop fell through without finding a factor
        print(n,'is a prime number')

print("-"*40)

#Continuen statement

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a odd number",num)


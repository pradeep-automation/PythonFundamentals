print("-------------------For Loop------------------------------")
# For Loop
fruits = ["apple", "banana", "cherry", "Pineapple"]
for fruit in fruits:
    if fruit == 'cherry':
        print('Found the cherry')
        break
    print(fruit)

for fruit in fruits:
    if fruit == 'cherry':
        print('Ignoring the cherry')
        continue
    print(fruit)

print("-------------------While Loop------------------------------")
# while loop
count = 0
while count < 5:
    count += 1
    print("This is", count)
print("-------------------Checking function------------------------------")
name = "Pradeep Ramola"


def greet(arg):
    print("Hello,", arg)


greet(name)

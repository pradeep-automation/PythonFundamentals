language = 'Python'
lang = 'Python'

print(language is lang)

if language == lang:
    print('Language is python')
else:
    print('Language is not python')

print("-------------------------------------------------")
l1 = [1, 4, 2]
l2 = [1, 4, 2]
l3 = l1
print(l1 is l2)
print(l1 == l2)
print(l3 is l1)

print("-------------------------------------------------")

# and
# or
# not

user = 'Admin'
loggedin = False

if user == 'Admin' and loggedin:
    print('Welcome to the jungle!!!!!')
elif user is not 'Admin':
    print('Kya hai ye')
elif not loggedin:
    print('Please login to the Jungle first!!!!')
else:
    print('stay in your Metro city please')

my_msg = 'Bobby\'s World!!!'
print(my_msg)

your_msg = '''Peppa pig was good \
cartoon 5 years back....'''
print(your_msg)

msg = 'Hello World'
print(len(msg))
print(msg[0])
print("Value of 6th char", msg[6] )
#print(msg[11]) # indexerror
print(msg[0:7])  # Includes starting index and excludes the ending index value
print(msg[:5])
print(msg[6:15])    # still valid even if we give incorrect ending index value
print(msg[6:])

greetings = "hello"
name = "Pradeep"
name.replace("p","k")
print(name)
new_name = name.replace("p", "k")
print(new_name)
print(name)
name = name.replace("Pradeep", "Anku")
print(name)
print("####################################")
print(greetings.count("l"))
print(greetings.find("l"))
print(greetings.rfind("l"))
print(greetings.find('H'))
print("####################################")
joining = greetings + name
print(joining)
joining_new = greetings + ',' + name
print(joining_new)
welcome_msg = greetings + ', ' + name + '. Welcome!'
print(welcome_msg)
welcome_msg_formatted = '{} {}. Welcome!!!!'.format(greetings, name.upper())
print(welcome_msg_formatted)
print("####################################")
print(greetings + '{}'.format(name))
print("################# F Strings###################")

welcome_msg_f = f'{greetings.capitalize()} {new_name.upper()}. Welcome!!!!'
print(welcome_msg_f)


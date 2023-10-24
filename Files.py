# File Objects

# f = open('file_demo.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()
# my_list = []
with open('file_demo.txt','r') as f:
    txt = f.read()
    my_list = txt.split(' ')
    # for char in txt:
    #     my_list.append(char)
print(my_list)





import textwrap

# print(textwrap.shorten("Hello  world!", width=12))

# st = "     spacious     "
st = "wwpw.example.com"
print(st.strip(".ompecw."))

# # print(pal)
# chal = "PeedeeP"
#
# def is_palindrome(dal):
#     res = ""
#     for char in dal:
#         if char.isalnum():
#             res = res+"".join(char)
#     l = 0
#     r = len(res)-1
#     while l<r:
#         if res[l] != res[r]:
#             return False
#         l += 1
#         r -= 1
#     return True
#
#
# print(is_palindrome(dal))
#
# dal = "Python #321is si123 $nohtyP$$$$$"
# d = "321"
# print(dal.index(d,17))

class MyClass:
    _x = ["First"]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


my = MyClass()
print(my.x)
my.x = "Last"
print(my.x)



ls = ["apple","dog", "cat"]
print(ls)
my_dict = {1:"app",2:"shape"}
my_dict.update({3:"tweet"})
# print(my_dict[5]) # gives keyerror if not present
print(my_dict.get(5))  # gives None if not present





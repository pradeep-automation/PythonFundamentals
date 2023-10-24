# output----
def print_triangle(st):
    k = 5
    for i in range(5):
        # for j in range(1):
        print(st * k, end="")
        k -= 1
        print()


def equilateral_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), "*" * (2 * i - 1))


print_triangle("*")
print("$"*30)
equilateral_triangle(5)

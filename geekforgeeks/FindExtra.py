def find_extra(a:list,b,n):
    for i in range(n):
        if i> len(b)-1 or a[i] != b[i]:

            return a[i]
    return


M = 4
C=[1,2,3,4]
D=[1,2,3]

print(find_extra(C,D,M))





N = 7
A= [2,4,6,8,9,10,12]
B = [2,4,6,8,10,12]
M = 4
C=[1,2,3,4]
D=[1,2,3]

# print(find_extra(C,D,M))


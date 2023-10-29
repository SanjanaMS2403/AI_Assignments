n=int(input("Enter no. of elements in list:"))
L=[]
Lp=[]
for i in range(n):
    m=int(input("Enter element:"))
    L.append(m)
for x in L:
    if x>0:
        Lp.append(x)
    else:
        pass
print("Input:",L)
print("Output:",Lp)


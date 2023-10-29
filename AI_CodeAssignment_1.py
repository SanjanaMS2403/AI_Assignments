#Fibonacci numbers
n=int(input("Enter Number:"))
n1=0
n2=1
n3=n2  
c=1
while c<=n:
    print(n3,end=" ")
    c+=1
    n1,n2=n2,n3
    n3=n1+n2
else:
    pass

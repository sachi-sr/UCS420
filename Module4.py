#4.1
for x in range(7,71,7):
    print(x, end=" ")
print("\n")
for x in range(1,11):
    print(x*9, end=" ")
print("\n")
#4.2
n=input("Enter a number:")
n=int(n)
for x in range(1,11):
    print(x*n, end=" ")
print("\n")
#4.3
sum=0
n=int(input("Enter a number:"))
for x in range(1,n+1):
    sum+=x
print(sum)    
s=0

#-----------------------------

print("range(10)  --> ",list(range(10)))
print("range(10,20)  --> ",list(range(10,20)))
print("range(-10,-20,2)--> ",list(range(-10,-20,2)))
print("range(-10,-20,-2)-->",list(range(-10,-20,-2)))
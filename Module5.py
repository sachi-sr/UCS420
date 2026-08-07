#5.1
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
if  a > b:
	print (a," is greater than ",b)
elif a==b:
	print(a,"is equal to",b)
else:
	print (a," is less than ",b)
#5.2
n=int(input("Enter a Number: "))
if n%2==0:
	print(n," is even")
else:
	print(n,"is odd")

#5.3

n=int(input("Enter a No: "))
f=0
for i in range(2,n//2+1):
	if n% i==0:
		f=1
		break
if f==0:
	print("Prime")
else:
	print("Not Prime")
#5.4
a=input("Enter first string: ")
b=input("Enter second string: ")
if a==b:
	print("a is equal to b")
elif a>b:
	print("a is greater than b")
else:
	print("a is less than b")

#A-5.1
n=int(input("Enter a number:"))
s=0
for i in range (1,n+1):
	if i%7==0 and i%9==0:
		s=s+i
print(s)
s=0
n = int(input("Enter a number: "))

sum_prime = 0

for i in range(2, n + 1):
    prime = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            break

    if prime:
        sum_prime += i

print("Sum of all prime numbers from 1 to", n, "is:", sum_prime)
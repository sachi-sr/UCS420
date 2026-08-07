#6.1
def Add(a,b):
	c=a+b
	return c

print ("Add(10,20) -->", Add(10,20))
print ("Add(20,50) -->", Add(20,50))
print ("Add(80,200) -->", Add(80,200))

#6.2
def IsPrime(n):
	for i in range(2, n//2 + 1):
		if n%i==0:
			return 0
	return 1

print ("IsPrime(20)  --> ", IsPrime(20))
print ("IsPrime(23)  --> ", IsPrime(23))
print ("IsPrime(200) --> ", IsPrime(200))
print ("IsPrime(37)  --> ", IsPrime(37))
#6.3
def AddN(n):
	s= sum(range(n+1))
	return s

print ("AddN(10)  --> ", AddN(10))
print ("AddN(20)  --> ", AddN(20))
print ("AddN(50)  --> ", AddN(50))

#A-6.1
def sum(n):
	s=0
	for i in range(1,n+1):
		if i%2!=0:
			s+=i
	return s
n=input("Enter a number: ")
n=int(n)
print("Sum of all odd number from 1 to",n,"is: ",sum(n))

def primee(n):
    sum_prime = 0
    for i in range(2, n + 1):
        prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break

        if prime:
            sum_prime += i

    return sum_prime
n=input("Enter a number: ")
n=int(n)
print("Sum of prime numbers from 1 to ",n," is",primee(n) )

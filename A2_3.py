import random
random.seed(1024170398)
numbers = []
for i in range(100):
    number = random.randint(100, 900)
    numbers.append(number)

print("Random numbers:")
print(numbers)

odd_number = []
for number in numbers:
    if number % 2 != 0:
        odd_number.append(number)

print("Number of odd numbers:", len(odd_number))
print("Odd numbers:", odd_number)

evenno = []
for number in numbers:
    if number % 2 == 0:
        evenno.append(number)

print("Number of even numbers:", len(evenno))
print("Even numbers:", evenno)

primeno = []
for number in numbers:
    if number > 1:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primeno.append(number)

print("Number of prime numbers:", len(primeno))
print("Prime numbers:", primeno)

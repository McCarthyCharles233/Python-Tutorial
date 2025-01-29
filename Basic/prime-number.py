n = int(input("Type in a number: "))

if n <= 1:
    print("This number is not a prime number")
else:
    is_prime = True
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            is_prime = False
        break
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")






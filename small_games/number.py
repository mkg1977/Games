n = int(input("Put the number: "))

is_prime = True
for i in range(2, n+1):
    if n % i == 0:
        is_prime = False
    
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = []

for namber in numbers[1:]:
    is_prime = True
    for i in range(2, namber // 2 + 1):
        if namber % i == 0:
            not_primes.append(namber)
            break
    else:
        primes.append(namber)

print(primes, not_primes, sep="\n")






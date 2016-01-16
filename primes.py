# Example imperative primes program in python

prime_count = 1
primes = [2]
candidate_prime = 3
number_of_primes = 100
while prime_count < number_of_primes:
    for known_prime in primes:
        if candidate_prime % known_prime == 0:
            break # test_value is not a prime
        elif known_prime * known_prime > candidate_prime:
            # test_value is prime!
            primes.append(candidate_prime)
            prime_count += 1
            break
    candidate_prime += 1

print primes

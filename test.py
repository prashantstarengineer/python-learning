def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage
if __name__ == "__main__":
    # Test single number
    number = 17
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    
    # Find primes in a range
    start = 1
    end = 20
    primes = find_primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

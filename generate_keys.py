#RSA Cipher and Key Creating Program
#
import random

def get_primes(start, stop):

    if start >= stop:
        return []
    primes = [2]                            #Initial prime number is 2
    
    for n in range(3, stop + 1, 2):         # From prime #3 to stop value plus one. Step 2 because even numbers are never prime. 
        for p in primes:                    # For each value n, it checks it against each prime that we've discovered so far.
            if n % p == 0:                  # If the number is disivble it is not a prime.
                break
        else:                               # Otherwise it is recorded as prime.
            primes.append(n)

    while primes and primes[0] < start:     # Deletes all numberes less than the starting number.
        del primes[0]

    return primes

def co_primes(a,b):                         # To test whether two numbers are coprime. Comprime if they share no common factor except 1

    for n in range(2, min(a,b) + 1):        # Checks all values until less than the smaller coprime.
        if a % n == b % n == 0:             # Tests all numbers less than the smaller prime for common factors
            return False
    return True


def make_key_pair(length):                  # Creates the public/private key pair

    if length < 4:
        raise ValueError("Cannot generate a key length less than 4. (got {!r})".format(length))   # Key is stronger if it has atleast 4 bits

# Need to find a number 'n' which is the muliple of two primes, 'p' and 'q'
    n_min = 1 << (length - 1)
    n_max = ( 1 << length) - 1               # The << shifts the left number by x amount of bits to the right

# Key is stronger if the two primes p and q have similar bit length.

    start = 1 << (length // 2 - 1)          
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start,stop)
    
# Now that we have a list of available primes, randomly choose two 

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes if n_min <= q * p <= n_max]

        if q_candidates:
            q = random.choice(q_candidates)
            break
        else:
            print("Could not find a value for q")
# Choose a value for 'e' which is less than (p - 1) * (q - 1) and is also coprime.
    n = p * q
    phi_n = (p - 1) * (q - 1)
    eVal= []
    
    for num in range(3, phi_n, 2):          # Encryption (N,e)     
        if co_primes(num,phi_n):
            eVal.append(num)                # Stores all coprimes of e less than phi_n 
            
        if num == phi_n:
            break
            
    #else:
        #print("Cannot find 'e' with ",p," and ",q,".")
        
    e = random.choice(eVal)

# Find d so that (d * e % phi_n) = 1
    dVal = []
    for num1 in range(3,phi_n,2):
        if num1 * e % phi_n == 1:
            dVal.append(num1)
            
        if num1 == phi_n:
            break
    #else:
        #raise AssertionError("Cannot find 'd' with p={!r} and q={!r}".format(p,q))
    d = random.choice(dVal)

    return e,d,n


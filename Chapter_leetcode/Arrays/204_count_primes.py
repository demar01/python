
#Sieve of Eratosthenes

class Solution:
  def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2: return 0

    primes = [True] * n
    primes[0] = primes[1] = False
    for num in range(2, int(math.sqrt(n)) + 1):
        if primes[num]:
            primes[num**2:n:num] = [False] * len(primes[num**2:n:num])

    return sum(primes)

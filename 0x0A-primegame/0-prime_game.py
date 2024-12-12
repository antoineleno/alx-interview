def isWinner(x, nums):
    """
    Determines the winner of each game round and the overall winner.

    Args:
        x (int): The number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ('Maria' or 'Ben').
             None if there is no clear winner.
    """
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(max_n):
        """Generate a list of prime counts up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False

        prime_count = [0] * (max_n + 1)
        count = 0
        for i in range(1, max_n + 1):
            if is_prime[i]:
                count += 1
            prime_count[i] = count

        return prime_count

    max_num = max(nums)
    prime_count = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if count of primes is odd
            maria_wins += 1
        else:  # Ben wins if count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


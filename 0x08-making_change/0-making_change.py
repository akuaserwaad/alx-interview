#!/usr/bin/python3
"""change comes from within"""


from collections import deque


def makeChange(coins, total):
    """Function that determines the fewest number of coins needed"""
    if total <= 0:
        return 0

    # Initialize a queue for BFS (current sum, number of coins used)
    queue = deque([(0, 0)])  # (current_sum, num_coins_used)
    visited = set([0])  # To track the visited sums
    # Start BFS
    while queue:
        current_sum, num_coins = queue.popleft()
        # Explore adding each coin to the current sum
        for coin in coins:
            new_sum = current_sum + coin

            # If we hit the total, return the number of coins used
            if new_sum == total:
                return num_coins + 1

            # If we havent visited the new sum, add it to the queue
            if new_sum < total and new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, num_coins + 1))
    # If we never hit the total, return -1
    return -1

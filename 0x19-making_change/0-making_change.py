#!/usr/bin/python3
"""
function that determines the fewest number of coins to make change
"""


def makeChange(coins, total):
    """
    parameters:
        coins : list of available coins
        total : total value to return
    returns:
        least amount of coins possible
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1
    coins = sorted(coins)
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    if dynamic[total] == float('inf'):
        return -1
    return dynamic[total]

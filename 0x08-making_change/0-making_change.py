#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """this functions determines the fewest number of coins needed to meet
    a given amount total - using coins of different values"""
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    curTotal = 0
    minCoins = 0
    for coin in coins:
        bal = (total - curTotal)//coin
        curTotal += bal*coin
        minCoins += bal
        if curTotal == total:
            return minCoins
    return -1

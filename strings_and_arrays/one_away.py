# One Away: There are three type of edits that can be performed on strings: Insert a character, remove a character, or replace a character. Give two strings, write a function to check if they are one edit (or zero edits) away.
# - pale, ple   -> true
# - pales, pale -> true
# - pale, bale  -> true
# - pale, bake  -> false


def one_away(a, b):
    if a == b:
        return True

    if abs(len(a) - len(b)) > 1:
        return False

    diff = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff < 2

    longer = a if len(a) > len(b) else b
    shorter = a if len(a) < len(b) else b

    i = 0
    j = 0
    diff = 0
    while i < len(longer) - 1:
        if longer[i] != shorter[j]:
            diff += 1
            i += 1
        i += 1
        j += 1
    return diff < 2


def max_profit(prices):
    if not prices:
        return 0

    maxProfit = 0
    minPurchase = prices[0]
    for i in range(1, len(prices)):
        maxProfit = max(maxProfit, prices[i] - minPurchase)
        minPurchase = min(minPurchase, prices[i])
    return maxProfit


print(max_profit([7, 1, 5, 3, 6, 4]))

import sys
'''
f(n) = s - f(n) + f(n-1) 
'''
# def coinChange(arr, n):
#     ways_index = [i for i in range(0, n+1)]
#     ways = [0 for i in range(0, n+1)]
#     # print(ways_index)
#     # print(ways)
#     ways[0] = 1
#     #iterate for each coin in the coin array
#     temp = 0
#     for coin in arr:
#         for j in ways_index:
#             if coin <= j:
#                 ways[j] = ways[j - coin] + ways[j]
#                 # if (j > 0 and (ways[j] > temp)):
#                 #     temp = ways[j]
#                 #     print("position: " + str(j) + " value: " + str(coin))
#     print(ways)

def coinChange(arr, n, coins:[]):
    if n == 0:
        print(coins)
        return 1
    elif n < 0:
        return 0
    
    if len(arr) <= 0 and n >= 1:
        return 0

    return coinChange(arr[1:], n, coins + []) + coinChange(arr, n-arr[0], coins + [arr[0]])
                    
    
if __name__ == "__main__":
    arr = [1,2,3]
    print(coinChange(arr, 6, []))
    #print(sum(possList))
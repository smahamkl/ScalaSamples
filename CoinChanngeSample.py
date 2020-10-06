import sys
'''
f(n) = s - f(n) + f(n-1) 
'''
def coinChange(arr, n):
    ways_index = [i for i in range(0, n+1)]
    ways = [0 for i in range(0, n+1)]
    # print(ways_index)
    # print(ways)
    ways[0] = 1
    #iterate for each coin in the coin array
    temp = 0
    for coin in arr:
        for j in ways_index:
            if coin <= j:
                ways[j] = ways[j - coin] + ways[j]
                # if (j > 0 and (ways[j] > temp)):
                #     temp = ways[j]
                #     print("position: " + str(j) + " value: " + str(coin))
    print(ways)
                    
    


if __name__ == "__main__":
    arr = [1,2,3]
    coinChange(arr, 5)
    #print(sum(possList))

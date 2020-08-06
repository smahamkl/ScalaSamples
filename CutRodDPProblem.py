import sys, math

def max(a, b):
    if a > b:
        return a
    else:
        return b

def cutRod(arr, n):
    max_val = -sys.maxsize
    if n==0:
        return 0
    else:
        for i in range(n):
            max_val = max(max_val, (arr[i] + cutRod(arr, n -i -1)))
    
    return max_val

def cutRodMemoization(arr, n):
    v = [0 for x in range(n+1)]
    if n==0:
        return 0
    else:
        for i in range(1, n+1):
            max_val =  -sys.maxsize
            for j in range(i):
                max_val = max(max_val, arr[j] + v[i - j - 1])
            v[i] = max_val
        
        return v[n]
        #print(v)
    
    return max_val

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20] 
    size = len(arr) 
    #print("Maximum Obtainable Value is", cutRod(arr, size))
    print("Maximum Obtainable value using memoization technique is", cutRodMemoization(arr, size))
import sys

def powerSet(set, set_size):
    power_set_size = 2 ** set_size
    #print(power_set_size)
    for i in range(0, power_set_size):
        for j in range(0, set_size):
            if i & (1 << j) > 0:
                print(set[j], end = "")
        print("")

if __name__ == "__main__":
    arr = ['a', 'b', 'c']
    powerSet(arr, len(arr))
    print(7 & 4)
import timeit

# two sum in O(n) time O(n) space
def Solution(arr, targ):
    target = {}
    for num in arr: 
        if num in target:
            return (targ, target[num], num, target[num]*num)
        diff = targ - num
        target[diff] = num

    return -1

# three sum in O(N^2) time, O(n) space complexity
def Solution2(arr, targ):
    arr = sorted(arr)
    
    for i in range(len(arr)):
        target = {}
        for j in range(i, len(arr)):
            if arr[j] in target:
                return (targ, arr[i], target[arr[j]], arr[j], target[arr[j]]*arr[j]*arr[i])
            diff = targ - arr[i] - arr[j]
            target[diff] = arr[j]
    
    return -1

# 3sum in quadratic time constant space 
def Solution2_Variant(arr, targ):
    arr = sorted(arr)
    for i in range(len(arr)):
        j = i + 1
        k = len(arr)-1
        while j < k:
            res = arr[i] + arr[j] + arr[k]
            if res < targ:
                j += 1
            elif res > targ:
                k -= 1
            else:
                return (targ, arr[i], arr[j], arr[k], res)
    
    return -1

def readInput():
    f = open('day1-inp.txt')
    inp = [int(line.rstrip("\n")) for line in f]
    return inp


def main():
    inp = readInput()
    SETUP_CODE = """
from __main__ import readInput, Solution, Solution2, Solution2_Variant
inp = readInput()
"""

    out = Solution(inp,2020)

    print("Part 1")        
    print(out)
    print(f'answer is {out[3]}')

    TWOSUM_CODE = "Solution(inp, 2020)"

    print("\nPart 2")
    out = Solution2(inp, 2020)
    print(out)
    print(f"answer is {out[4]}\n") 

    print("Part 2 Variant")
    out = Solution2_Variant(inp, 2020)
    print(out)
    print(f"answer is {out[4]}\n")

    THREESUM_CODE = "Solution2(inp, 2020)"
    THREESUM2_CODE = "Solution2_Variant(inp, 2020)"

    print("2sum: " + str(timeit.timeit(setup=SETUP_CODE, stmt=TWOSUM_CODE, number=10000)))
    print("Linear Space 3sum: " + str(timeit.timeit(setup=SETUP_CODE, stmt=THREESUM_CODE, number=10000)))
    print("Constant Space 3sum: " + str(timeit.timeit(setup=SETUP_CODE, stmt=THREESUM2_CODE, number=10000)))


main()
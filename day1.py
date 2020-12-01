def Solution(arr, targ):
    target = {}

    for num in arr: 
        if num in target:
            return (targ, target[num], num, target[num]*num)
        diff = targ - num
        target[diff] = num
    
    return -1

f = open('day1-inp.txt')
inp = [int(line.rstrip("\n")) for line in f]
out = Solution(inp,2020)        
print(out)
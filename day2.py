import timeit

def Solution(arr):
    count = 0
    for s in arr:
        frags = s.split(" ") # range , letter:, password string 
        low, high = frags[0].split("-")
        letter = frags[1][0]
        freq = 0
        for ch in frags[2]:
            if ch == letter:
                freq += 1
        if freq >= int(low) and freq <= int(high):
            count += 1
    return count

def Solution2(arr):
    count = 0
    for s in arr:
        frags = s.split(" ")
        low, high = map(int, frags[0].split("-"))
        letter = frags[1][0]
        pw = frags[2]
        if low >= 1 and high <= len(pw):
            if pw[low-1] == letter and not pw[high-1] == letter:
                count += 1
            elif not pw[low-1] == letter and pw[high-1] == letter:
                count += 1

    return count
    

def readInput():
    f = open('day2-inp.txt')
    inp = [line.rstrip("\n") for line in f]
    return inp

def main():
    inp = readInput()

    SETUP_CODE = """
from __main__ import readInput, Solution, Solution2
inp = readInput()
"""

    sol1_time = timeit.timeit(setup=SETUP_CODE, stmt="Solution(inp)", number=1000)
    sol2_time = timeit.timeit(setup=SETUP_CODE, stmt="Solution2(inp)", number=1000)

    print(f"Part 1: {Solution(inp)} done in {sol1_time}s")
    print(f"Part 2: {Solution2(inp)} done in {sol2_time}s")

main()
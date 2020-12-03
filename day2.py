import parsing

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
    
def main():
    inp = parsing.readInput('day2-inp.txt')

    SETUP_CODE = """
from __main__ import Solution, Solution2
import parsing
inp = parsing.readInput("day2-inp.txt")
"""

    sol1_time = parsing.timer("Solution(inp)", setup_code=SETUP_CODE, iters=1000)
    sol2_time = parsing.timer("Solution2(inp)", setup_code=SETUP_CODE, iters=1000)

    print(f"Part 1: {Solution(inp)} done in {sol1_time}s")
    print(f"Part 2: {Solution2(inp)} done in {sol2_time}s")

main()
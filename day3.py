import parsing

def Solution(inp):
    count = 0
    x = 0
    for line in inp:
        #print(f"{x} {x % len(line)} {line[x % len(line)]}")
        if line[x % len(line)] == "#":
            count += 1
        x += 3
        continue
    return count

def Solution2(inp, r, d):
    count = 0 
    x = 0
    for i in range(len(inp)):
        line = inp[i]
        if i % d != 0:
            continue
        if line[x % len(line)] == "#":
            count += 1
        x += r
    return count

def main():
    inp = parsing.readInput("day3-inp.txt")
    SETUP_CODE = """
from __main__ import Solution
import parsing
inp = parsing.readInput("day3-inp.txt")
"""
    sol1 = Solution(inp)
    sol1_time = parsing.timer("Solution(inp)", setup_code=SETUP_CODE, iters=100)
    print(sol1)
    print(sol1_time)

    sol2 = Solution2(inp, 1, 1)
    sol2_2 = Solution2(inp, 3, 1)
    sol2_3 = Solution2(inp, 5, 1)
    sol2_4 = Solution2(inp, 7, 1)
    sol2_5 = Solution2(inp, 1, 2)
    print(sol2 * sol2_2 * sol2_3 * sol2_4 * sol2_5)

def testing():
    inp = parsing.readInput("day3-inp-sample.txt")
    sol1 = Solution(inp)
    print(sol1)
    sol2 = Solution2(inp, 1, 1)
    sol2_2 = Solution2(inp, 3, 1)
    sol2_3 = Solution2(inp, 5, 1)
    sol2_4 = Solution2(inp, 7, 1)
    sol2_5 = Solution2(inp, 1, 2)
    print(f"{sol2} {sol2_2} {sol2_3} {sol2_4} {sol2_5}")

main()
#testing2()
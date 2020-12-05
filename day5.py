from parsing import readInput

def Solution(arr):
    maxSeat = float("-inf")
    seats = []
    for line in arr:
        rowStart, rowEnd = 0, 127
        colStart, colEnd = 0, 7
        rowMid = (rowStart+rowEnd)//2
        colMid = (colStart+colEnd)//2 
        for ch in line:
            if ch == "B":
                rowStart = rowMid
            elif ch == "F":
                rowEnd = rowMid
            elif ch == "R":
                colStart = colMid
            elif ch == "L":
                colEnd = colMid
        seat = rowEnd * 8 + colEnd
        seats.append(seat)
        if seat > maxSeat:
            maxSeat = seat
    return (maxSeat, seats)

def Solution2(arr):
    for seat in arr:
        if (not (seat+1) in arr) and (seat + 2 in arr):
            return seat + 1
    return -1 

def main():
    inp = readInput("day5-inp.txt")
    print(len(inp))
    soln1 = Solution(inp)
    print(soln1[0])
    soln2 = Solution2(soln1[1])
    print(soln2)

main()



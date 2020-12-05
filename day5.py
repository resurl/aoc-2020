from parsing import readInput

def Solution(arr):
    maxSeat = float("-inf")
    seats = []
    for line in arr:
        rowStart, rowEnd = 0, 127
        colStart, colEnd = 0, 7
        for ch in line:
            if ch == "B":
                rowStart = (rowStart+rowEnd)//2
            elif ch == "F":
                rowEnd = (rowStart+rowEnd)//2
            elif ch == "R":
                colStart = (colStart+colEnd)//2
            elif ch == "L":
                colEnd = (colStart+colEnd)//2
        seat = rowEnd * 8 + colEnd
        seats.append(seat)
        if seat > maxSeat:
            maxSeat = seat
    return (maxSeat, seats)

def Solution2(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == 2:
            return arr[i] + 1
    return -1 
            
            

def main():
    inp = readInput("day5-inp.txt")
    print(len(inp))
    soln1 = Solution(inp)
    print(soln1[0])
    soln2 = Solution2(soln1[1])
    print(soln2)

main()



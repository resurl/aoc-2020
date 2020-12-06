def Solution(arr):
    count = 0
    for group in arr:
        answers = set(group)
        count += len(answers)
    return count

def Solution2(arr):
    count = 0
    for group in arr:
        alphabet = {}
        for answer in group:
            for ch in answer:
                alphabet[ch] = alphabet.get(ch, 0) + 1
        for key in alphabet.keys():
            if alphabet.get(key) == len(group):
                count += 1
    return count

def readInput2():
    f = open("day6-inp.txt")
    inp = []
    group = []
    for line in f:
        if line == "\n" or line == "":
            inp.append(group)
            group = []
        if line.strip() != "": group.append(line.strip())
    inp.append(group)
    return inp

def readInput():
    f = open("day6-inp.txt")
    inp = []
    group = ""
    for line in f:
        if line == "\n" or line == "":
            inp.append(group)
            group = ""
        group += line.strip()
    inp.append(group)
    return inp

def main():
    inp = readInput()
    print(Solution(inp))
    print(Solution2(readInput2()))
    
main()
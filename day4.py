enum = {
    "byr" : 0,
    "iyr" : 1,
    "eyr" : 2,
    "hgt" : 3,
    "hcl" : 4,
    "ecl" : 5,
    "pid" : 6,
    "cid" : 7
}

def readInput():
    f = open("day4-inp.txt")
    inp = []
    passport = ""
    for line in f:
        if line == "" or line == "\n":
            inp.append(passport.strip())
            passport = ""
        passport += line.rstrip("\n") + " "
    inp.append(passport.strip())
    return inp

def Solution(arr):
    count = 0
    for entry in arr:
        fieldValid = 0
        fields = entry.split(" ")
        for field in fields:
            k = field[:3]
            fieldValid |= (1 << enum[k])
            #print(bin(1<<enum[k]))

        if fieldValid == 255 or fieldValid == 127:
            count += 1
    return count

def Solution2(arr):
    count = 0
    for entry in arr:
        fieldValid = 0
        fields = entry.split(" ")
        for field in fields:
            k = field[:3]
            v = field[4:]
            if validateField(k,v): fieldValid |= (1 << enum[k])

        if fieldValid == 255 or fieldValid == 127:
            count += 1
    return count

def validateField(k,v):
    # today i learned that python doesn't have switch statements lol
    print(f"{k} {v} {v[len(v)-2:]}")
    switch = [
        lambda x: int(x) >= 1920 and int(x) <= 2002,
        lambda x: int(x) >= 2010 and int(x) <= 2020,
        lambda x: int(x) >= 2020 and int(x) <= 2030,
        lambda x: (x[len(x)-2:] == "cm" or x[len(x)-2:] == "in")
              and ((int(x[:len(x)-2]) >= 150 and int(x[:len(x)-2]) <= 193) if x[len(x)-2:] == "cm" else (int(x[:len(x)-2]) >= 59 and int(x[:len(x)-2]) <= 76)),
        lambda x: x[0] == "#" and len(x[1:]) == 6 and str(x[1:]).isalnum(),
        lambda x: x in {"amb","blu","brn","gry","grn","hzl","oth"},
        lambda x: len(x) == 9 and str(x).isnumeric(),
        lambda x: True
    ]
    return switch[enum[k]](v)
    

def main():
    inp = readInput()
    print(Solution(inp))
    print(Solution2(inp))

main()

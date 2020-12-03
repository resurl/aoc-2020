import timeit

def readInput(file_path):
    f = open(file_path)
    inp = [line.rstrip("\n") for line in f]
    return inp

def timer(func, setup_code="", iters=1000):
    runtime = timeit.timeit(setup=setup_code, stmt=func, number=iters)
    return runtime
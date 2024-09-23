
NUM = 3571
def getnum(input):
    val = 0
    if isinstance(input, (int, float)):
        val = input
    elif isinstance(input, str):
        ops = 0
        for char in input:
            val += ord(char) * (10 ** ops)
            ops += 1
    return val
    
def ex1(key):
    val = 0
    if isinstance(key, tuple):
        val = sum(getnum(item) for item in key)
    else:
        val = getnum(key)
    return val % NUM
    
def main():
    print(ex1(1))
    print(ex1('abc'))
    print(ex1('cba'))
    print(ex1(('a', 1)))

if __name__ == "__main__":
    main()
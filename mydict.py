#!/usr/bin/env python3

# this is a "hash" #
# this is a "bang" !
# together, this is known as as "shebang" line

def getnum(input):
    val = 0
    if isinstance(input, (int, float)):
        val = input
    elif isinstance(input, str):
        ops = 0
        for index, char in enumerate(input, 1):
            val += ord(char) * index
            ops += 1
    else:
        raise TypeError(f'Unhashable value: {input}')

    return val

def myhash(key):
    val = 0
    if isinstance(key, tuple):
        val = sum(getnum(item) for item in key)
    else:
        val = getnum(key)
    return val

def main():
    print(myhash(1))
    print(myhash('abc'))
    print(myhash('cba'))
    print(myhash(('a', 1)))

if __name__ == "__main__":
    main()

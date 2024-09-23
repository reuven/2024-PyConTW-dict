#!/usr/bin/env python3

# this is a "hash" #
# this is a "bang" !
# together, this is known as as "shebang" line

class HashTable():
    def __init__(self, mylist):
        self.data = [None for _ in range(8)]
        for key, keyhash in mylist:
            self.data[keyhash % len(self.data)] = key
    
def getnum(input):
    val = 0
    if isinstance(input, int):
        val = input
    elif isinstance(input, float):
        val = getnum(str(float)) * 10    # treat a float as a string, more or less
    elif isinstance(input, str):
        for index, char in enumerate(input, 1):
            val += ord(char) * index
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
    tests = [1, '1', 'abc', ('a', 1)]
    val = [(item, myhash(item)) for item in tests]
    ret = HashTable(val)

if __name__ == "__main__":
    main()
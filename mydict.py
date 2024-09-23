#!/usr/bin/env python3

# this is a "hash" #
# this is a "bang" !
# together, this is known as as "shebang" line

class HashTable():
    def __init__(self, list_of_pairs):
        self.data = [None for _ in range(8)]

        # (1) Iterate over list_of_pairs, where each tuple is a (key, value)
        # (2) Calculate myhash(key), and get the modulus based on len(self.data)
        # (3) Place the (key, value) tuple in that location in our list

        for key, value in list_of_pairs:
            self.__setitem__(key, value)

    def __getitem__(self, key):
        idx = myhash(key) % len(self.data)
        while idx < len(self.data):
            # If `None` is there, then raise `KeyError` (just like a real dict)
            if self.data[idx] is None:
                raise KeyError(f'{key} not found')
            elif self.data[idx][0] == key:
                return self.data[myhash(key) % len(self.data)][1]
            else:
                idx += 1
            
    def __setitem__(self, key, value):
        idx = myhash(key) % len(self.data)
        while self.data[idx] is not None:
            idx = (idx + 1) % len(self.data)
        self.data[idx] = (key, value)


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

    pairs = [('a', 10), ('b', 20), ('c', 30), ('hello out there', 40)]
    ret = HashTable(pairs)
    print(ret.data)   # this should show our key-value pairs, but hashed
    print(ret['a'])    # this should show 10

if __name__ == "__main__":
    main()
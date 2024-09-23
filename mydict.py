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
            self[key] = value

    def __getitem__(self, key):
        idx = myhash(key) % len(self.data)
        while idx < len(self.data):
            # If `None` is there, then raise `KeyError` (just like a real dict)
            if self.data[idx] is None:
                raise KeyError(f'{key} not found')
            elif self.data[idx][0] == key:
                return self.data[myhash(key) % len(self.data)][1]
            else:
                idx = (idx + 1) % len(self.data)

    def __setitem__(self, key, value):
        if self.data.count(None)<len(self.data)//3:
            print(f'\tRehashing!')
            # None not enough, so rehash and resize
            # print(f'\tBefore rehashing, size is {len(self)=}')
            self.rehashAndResize()
            # print(f'\tAfter rehashing, size is {len(self)=}')

        self.place_pair_safely(self.data, key, value)

    @staticmethod
    def place_pair_safely(list_of_pairs, key, value):
        idx = myhash(key) % len(list_of_pairs)
        while list_of_pairs[idx] is not None and key != list_of_pairs[idx][0]:
            idx = (idx + 1) % len(list_of_pairs)
        list_of_pairs[idx] = (key, value)

        # print(f'\tAdded {key}:{value}')

    def __len__(self):
        return len([1
                    for one_item in self.data
                    if one_item is not None])


    def items(self):
        for one_element in self.data:
            if one_element is None:
                continue
            yield one_element

    def __iter__(self):
        for one_element in self.data:
            if one_element is None:
                continue
            yield one_element

    # remove the key-value pair with the given key
    def pop(self, key):

        idx = myhash(key) % len(self.data)
        while self.data[idx] is not None and key != self.data[idx][0]:
            idx = (idx + 1) % len(self.data)

        if self.data[idx] is None:
            raise KeyError(f'Key {key} is not found')
        else:
            value = self.data[idx][1]
            self.data[idx] = None
            return value

    def rehashAndResize(self):
        # double data size
        # need keep the original data and rehash
        # print(f'Before, {self.data=}')
        new_data = [None] * len(self.data) * 2
        # print(f'After, {self.data=}')

        for one_element in self.data:
            if one_element is None:
                continue

            key, value = one_element    # we know it's (key, value) and can be unpacked
            self.place_pair_safely(new_data, key, value)

        self.data = new_data

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
    print(ret['b'])
    print(ret['c'])


    for one_key in 'defghijkl':
        ret[one_key] = ord(one_key)

    print('*' * 60)
    print(len(ret))
    print(ret.data)
    ret['this should show up'] = 'hello'
    print(len(ret))
    print(ret.data)

    print('*' * 60)

    print(f'*** Iterating over ret.items()')
    for key, value in ret.items():
        print(key, value)

    print(f'*** Iterating over ret')
    for key,value in ret:
        print(key, value)

    print(f'*** Trying to pop')
    print(len(ret))
    print(ret.pop('a'))
    print(len(ret))

    # print(f'*** Trying to pop')
    # print(len(ret))
    # print(ret.pop('not there'))
    # print(len(ret))

if __name__ == "__main__":
    main()

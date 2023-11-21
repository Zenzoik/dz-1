def groupAnagrams(arr):
    types = {}
    for word in arr:
        sort = ''.join(sorted(word))
        if sort in types:
            types[sort].append(word)
        else:
            types[sort] = [word]
    res = list(types.values())
    return res
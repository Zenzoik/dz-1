def find_even_index(arr):
    user = arr
    for i in range(0, len(user)):
        if sum(user[:i]) == sum(user[i+1:]):
            return i
    return -1
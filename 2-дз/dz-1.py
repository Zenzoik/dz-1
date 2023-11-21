def largest_radial_sum(arr, d):
    num = len(arr)//d
    res = []
    tmp = []
    counter = 0
    while counter != num:
        print(counter, num)
        for i in range(counter, len(arr), num):
            tmp.append(arr[i])
        res.append(sum(tmp))
        print(tmp, res)
        tmp.clear()
        counter+=1
    return max(res)
def high_and_low(nums):
    lst = [int(num) for num in nums.split()]
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item_to_insert
    return (str(lst[-1])+ " "+ str(lst[0]))
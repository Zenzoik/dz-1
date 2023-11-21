def descending_order(nums):
    user_input = list(str(nums))
    for i in range(1, len(user_input)):
        item_to_insert = user_input[i]
        j = i - 1
        while j >= 0 and user_input[j] > item_to_insert:
            user_input[j + 1] = user_input[j]
            j -= 1
        user_input[j + 1] = item_to_insert
    res = ''.join(reversed(user_input))
    return int(res)
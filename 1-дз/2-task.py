def hanoi(disk):
    num = disk
    if num < 0:
        return 0
    else:
        return(2**num - 1)
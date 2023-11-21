def find_nb(m):
    i=1
    couter = 0
    while m != 0:
        m-=i**3
        if m < 0:
            return -1
        i+=1
        couter+=1
    if m == 0:
        return couter
def land_perimeter(arr):
    perim = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
                if arr[i][j] == 'X':
                    perim +=4
                    if i>0 and arr[i-1][j] == 'X':
                        perim -= 2
                    if j>0 and arr[i][j-1] == 'X':
                        perim -=2
    return(f"Total land perimeter: {perim}")
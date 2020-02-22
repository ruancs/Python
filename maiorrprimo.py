def maior_primo(n):
    x=0
    y=n

    while y>=1: 
        for x in range(2, y + 1): 
            if y % x == 0:
                break

        if x == y: 
            return x

        y = y - 1

    return 1 

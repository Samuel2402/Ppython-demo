def flip(d,a):         #d == direction a == cubes
    if d =='L':
        return sorted(a, reverse = True)
    else:
        return sorted(a)
    
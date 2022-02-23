

def add(a, b, c, d):
    dem = b
    if b != d:
        a *= d
        c *= b
        dem *= d
    num = a + c
    return tuple((num, dem))



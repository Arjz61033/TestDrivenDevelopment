def volume_cube(l):
    if type(l) not in [int, float]:
        raise TypeError('Length of cuboid should be an integer or a float')
    if l==0:
        raise Exception('Length cannot be zero')
    # if l<=0:
    #     raise Exception('Length cannot be zero or negative')
    return (l*l*l)
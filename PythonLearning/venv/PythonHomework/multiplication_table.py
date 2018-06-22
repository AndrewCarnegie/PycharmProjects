for i in range(1, 10):
    for j in range(1, i+1):
        print('{0} X {1} = {2:2d}'.format(j, i, j*i), end='  ')
    print()
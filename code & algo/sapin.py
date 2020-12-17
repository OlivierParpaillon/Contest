def triangle_shape(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()




def triangle_shape2(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(4*i+3):
            print('*', end='')
        print()



def triangle_shape3(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(6*i+5):
            print('*', end='')
        print()




triangle_shape(4)
triangle_shape2(4)
triangle_shape3(4)
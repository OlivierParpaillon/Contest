# -*- coding:latin1 -*

"""
    Contest project 1 : Christmas Tree
    Olivier PARPAILLON
    Iliass RAMI
    17/12/2020
    python 3.7.7
"""
# Python program to generate branch christmas tree

# Generating branch christmas tree


def triangle_branch(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')



def triangle_branch2(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(4*i+3):
            print('*', end='')



def triangle_branch3(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(6*i+5):
            print('*', end='')


def tree_shape():



# triangle_shape(4)
# triangle_shape2(4)
# triangle_shape3(4)

# -*- coding:latin1 -*

"""
    Contest project 1 : Christmas Tree part.1
    Olivier PARPAILLON
    Iliass RAMI
    17/12/2020
    python 3.7.7
"""
# Python program to generate branch christmas tree

# Generating the first branch of the christmas tree

def branch1():

    nb_space = 15
    star_top = 1
    nb_branch = 4

    for i in range(nb_branch):
        print(" " * nb_space, "*" * star_top)
        nb_space -= 1
        star_top += 2

# Generating the middle branch of the christmas tree

def branch2():

    nb_space = 14
    star_top = 3
    nb_branch = 4

    for i in range(nb_branch):
        print(" " * nb_space, "*" * star_top)
        nb_space -= 2
        star_top += 4

# Generating the last branch of the christmas tree
def branch3():

    nb_space = 13
    star_top = 5
    nb_branch = 4

    for i in range(nb_branch):
        print(" " * nb_space, "*" * star_top)
        nb_space -= 3
        star_top += 6


branch1(), branch2(), branch3()


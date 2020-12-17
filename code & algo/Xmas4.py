# -*- coding:latin1 -*

"""
    Contest project 1 : Christmas Tree part.2
    Olivier PARPAILLON
    Iliass RAMI
    17/12/2020
    python 3.7.7
"""
# Python program to generate branch christmas tree. We split the tree in 3 branches.

# We generate the first branch of the christmas tree : branch1. We will use the same variables for the whole code : only values will change.
# nb_blank represents the number of blanks between the "*" ; star_top represents the number of "*" on the top of the tree ; 
# and nb_branch defines the number of times we repeat the operation.

def branch1():

    nb_blank = 15
    star_top = 1
    nb_branch = 4

    for i in range(nb_branch):
        print(" " * nb_blank, "*" * star_top)
        nb_blank -= 1
        star_top += 2

# We generate the middle branch of the christmas tree. Same variables but we add 4 to star_top and we remove 2 from nb_blank
# We add Christmas balls in this branch : the first line of the branch is modified.
def branch2():

    nb_blank = 12
    star_top = 7
    nb_branch = 3
    
    print(" " * 12, "0", "*" * 3, "0")

    for i in range(nb_branch):
        print(" " * nb_blank, "*" * star_top)
        nb_blank -= 2
        star_top += 4

# We generate the last branch of the christmas tree. We use the same variables but we remove 3 from nb_blank and we add 6 to star_top
# We add Christmas balls in this branch too : the first line of the branch is modified
def branch3():

    nb_blank = 10
    star_top = 11
    nb_branch = 3
    
    print(" " * 8, "0", " " * 3 + "*" * 5, " " * 2, "0")

    for i in range(nb_branch):
        print(" " * nb_blank, "*" * star_top)
        nb_blank -= 3
        star_top += 6

# To add ornaments on the tree we need to change the trunk function. 
# We add another function called ornament that will print the begin of the trunk with ornaments.

def ornament():
 
    nb_blank = 5
    star_top = 5
    trunk_height = 1

    for i in range(trunk_height):
        print(" " * nb_blank, "| " * 4 + "*" * star_top + " |" *4)
    for i in range(trunk_height):
        print(" " * nb_blank, "0 " * 4 + "*" * star_top + " 0" *4)
  
# We generate the trunk of the tree.
# It will only print the last line of the trunk.

def trunk():

    nb_blank = 13
    star_top = 5
    nb_branch = 1

    for i in range(nb_branch):
        print(" " * nb_blank, "*" * star_top)
        
# Main function to start the program.        
def main():
    branch1(), branch2(), branch3() , ornament(), trunk()

main()



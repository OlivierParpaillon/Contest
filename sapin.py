def print_segment(segment_size, total_width):
    for line_size in range(1, segment_size + 1, 2):
        print((line_size * "*").center(total_width))

def print_tree(size):
    for segment_size in range(3, size + 1, 2):
        print_segment(segment_size, size)

print("Choisissez la taille de votre Arbre de Noël :")
tree_size = int(input())
print_tree(tree_size)
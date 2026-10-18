from pathlib import Path

# triangles_file = Path(__file__).parent / "67_triangles.txt"
triangles_file = Path(__file__).parent / "67_triangles_small.txt"

### read triangles --> binary tree
tree = []
with open(triangles_file, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        tree.append([int(s) for s in line.strip().split(" ")])
len_tree = len(tree)


# ### DEBUG
# for l in tree:
#     print(l)
# print(f"{len(tree)=}")


### TODO - recursively check all branches
def find_max(
        depth: int,
        index: int,
        current_max: int,
    ) -> int:

    ### end of tree --> negative inf.
    try:
        current_value = tree[depth][index]
    except IndexError:
        return 0

    current_max += current_value

    ### Traverse both branches
    left_max = find_max(depth + 1, index, current_max)
    right_max = find_max(depth + 1, index + 1, current_max)

    ### return max of all 3
    return max(current_max, left_max, right_max)

result = find_max(0, 0, 0)
print(result)

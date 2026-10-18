from pathlib import Path


### read triangles
# triangles_file = Path(__file__).parent / "67_triangles.txt"
triangles_file = Path(__file__).parent / "67_triangles_small.txt"
tree = []
with open(triangles_file, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        tree.append(line.strip().split(" "))


### DEBUG
for l in tree:
    print(l)


### TODO - construct binary tree


### TODO - recursively check all branches

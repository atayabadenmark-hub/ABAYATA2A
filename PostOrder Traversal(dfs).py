from tree_node import build_name_tree

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

if __name__ == "__main__":
    root = build_name_tree()
    print("PostOrder Traversal (Left -> Right -> Root):")
    postorder(root)
    print()
from tree_node import build_name_tree

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

if __name__ == "__main__":
    root = build_name_tree()
    print("InOrder Traversal (Left -> Root -> Right):")
    inorder(root)
    print()
from tree_node import build_name_tree

def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

if __name__ == "__main__":
    root = build_name_tree()
    print("PreOrder Traversal (Root -> Left -> Right):")
    preorder(root)
    print()
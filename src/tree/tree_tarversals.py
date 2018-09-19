from src.tree.node import Node


def in_order(node):
    if node:
        in_order(node.left)
        print(node.data),
        in_order(node.right)


def pre_order(node):
    if node:
        print(node.data),
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data),


if __name__ == "__main__":
    root = Node(9)
    root.left = Node(8)
    root.right = Node(7)
    root.left.left = Node(6)
    root.left.right = Node(5)

    print("InOrder")
    in_order(root)

    print("PreOrder")
    pre_order(root)

    print("postOrder")
    post_order(root)

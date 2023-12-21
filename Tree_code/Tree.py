class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def append(self, key):
        self.root = self._append(self.root, key)

    def _append(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self._append(node.left, key)
        elif key > node.key:
            node.right = self._append(node.right, key)
        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.key = self._min_value(node.right)
            node.right = self._remove(node.right, node.key)

        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

# Example Usage:
tree = BinaryTree()
tree.append(5)
tree.append(3)
tree.append(7)
tree.prepend(1)
tree.prepend(4)

print("Original Tree:")
# Binary tree visualization
#         5
#        / \
#       3   7
#      / \
#     1   4

# Output In-Order Traversal: 1 3 4 5 7

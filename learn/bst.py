class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, data):
        return self.search_at(self.root, data)

    def search_at(self, root, data):
        if not root:
            return None

        if data == root.data:
            return root
        elif data <= root.data:
            return self.search_at(root.left, data)
        else:
            return self.search_at(root.right, data)

    # position will be 0 when there is no parent, and -1 if the searched element is on left of the parent, else 1
    def search_with_parent(self, root, data, parent=None, position=0):
        if not root:
            return root, parent, position

        if data == root.data:
            return root, parent, position
        elif data <= root.data:
            return self.search_with_parent(root.left, data, root, -1)
        else:
            return self.search_with_parent(root.right, data, root, 1)

    def set_at(self, parent, position, node):
        if not parent:
            self.root = node
        else:
            if position == -1:
                parent.left = node
            else:
                parent.right = node

    # assumes that node will never be None
    def delete_at(self, parent, position, node):
        left = node.left
        right = node.right

        if not left:
            self.set_at(parent, position, right)
        elif not right:
            self.set_at(parent, position, left)
        else:
            # find successor
            successor_parent = node
            successor = right
            successor_position = 1
            while successor.left:
                successor_parent, successor, successor_position = successor, successor.left, -1
            node.data = successor.data
            self.delete_at(successor_parent, successor_position, successor)

    def delete(self, data):
        node, parent, position = self.search_with_parent(self.root, data)
        # can't delete if couldn't found the node
        if not node:
            raise Exception(f"not found: {data}")
        self.delete_at(parent, position, node)

    def insert_with_loop(self, data):
        node = Node(data)

        if not self.root:
            self.root = node
            return

        prev = None
        current = self.root
        while current:
            prev = current
            if node.data <= current.data:
                current = current.left
            else:
                current = current.right

        if node.data <= prev.data:
            prev.left = node
        else:
            prev.right = node

    def insert(self, data):
        self.root = self.insert_at(self.root, Node(data))

    def insert_at(self, root, node):
        if not root:
            return node
        if node.data <= root.data:
            root.left = self.insert_at(root.left, node)
        else:
            root.right = self.insert_at(root.right, node)
        return root

    def in_order(self):
        self.in_order_from(self.root)

    def in_order_from(self, root):
        if not root:
            print("- ", end="")
            return

        self.in_order_from(root.left)
        print(root.data, end=" ")
        self.in_order_from(root.right)

    def pre_order(self):
        self.pre_order_from(self.root)

    # pre order could be seen as print will always be pre traversing childrens
    def pre_order_from(self, root):
        if not root:
            return

        print(root.data, end=" ")
        self.pre_order_from(root.left)
        self.pre_order_from(root.right)

    # post order could be seen as print will always be post traversing childrens
    def post_order(self):
        self.post_order_from(self.root)

    def post_order_from(self, root):
        if not root:
            return

        self.post_order_from(root.left)
        self.post_order_from(root.right)
        print(root.data, end=" ")


def main():
    bst = BST()
    bst.insert_with_loop(5)
    bst.insert_with_loop(3)
    bst.insert_with_loop(4)
    bst.insert_with_loop(2)
    bst.insert_with_loop(7)
    bst.insert_with_loop(8)
    bst.insert_with_loop(9)
    bst.in_order()
    print("")
    bst.delete(2)
    bst.in_order()
    print("")

    bst.delete(5)
    bst.in_order()
    print("")

    bst.delete(4)
    bst.in_order()
    print("")

    bst.delete(3)
    bst.in_order()
    print("")

    bst.delete(8)
    bst.in_order()
    print("")

    bst.delete(7)
    bst.in_order()
    print("")

    bst.delete(9)
    bst.in_order()


main()

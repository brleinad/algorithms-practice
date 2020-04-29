class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Node({self.value})'

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        #node = self.root
        #while node:
        #    if (self.preorder_search(node, find_val)):
        #        return True
        #    node = node.right
        #return False
        return self.preorder_search(self.root, find_val)


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, '')

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        node = start
        right_nodes = []
        if node.value == find_val:
            return True
        parent_node = node
        while node.left:
            if node.right:
                right_nodes.append(node.right)
            parent_node = node
            node = node.left
            if node.value == find_val:
                return True

        if right_nodes:
            right_nodes.reverse()
            for right_node in right_nodes:
                if self.preorder_search(right_node, find_val):
                    return True

        return False
        

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        node = start
        right_nodes = []
        if not node.left  and not node.right :
            return str(start)
        traversal = traversal + str(start)
        while node.left:
            parent_node = node
            if node.right:
                right_nodes.append(node.right)
            node = node.left
            traversal = '-'.join((traversal, str(node)))
        if right_nodes:
            right_nodes.reverse()
            for right_node in right_nodes:
                traversal = '-'.join((traversal, self.preorder_print(right_node, traversal)))
        return traversal

#   1
# 2   3
#4 5

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print('1-2-4-5-3')
print(tree.print_tree())

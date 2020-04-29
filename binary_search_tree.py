class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Node({self.value})'

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, '')

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
            for right_node in reversed(right_nodes):
                traversal = '-'.join((traversal, self.preorder_print(right_node, traversal)))
        return traversal

    def insert(self, new_val):
        """Insert a new node to the BST"""
        return self.innode_insert(self.root, new_val)
    
    def innode_insert(self, node, new_val):
        """Helper method to insert node to BST"""
        if new_val > node.value:
            if not node.right:
                node.right = Node(new_val)
                return
            else:
                self.innode_insert(node.right, new_val)
        else:
            if not node.left:
                node.left = Node(new_val)
                return
            else:
                self.innode_insert(node.left, new_val)
        return 
         

    def search(self, find_val):
        """Search BST for a value"""
        return self.innode_search(self.root, find_val)
        
    def innode_search(self, node, find_val):
        """Recursively search in a node"""
        if node.value == find_val:
            return True
        if node.value > find_val:
            if node.right:
                return self.innode_search(node.right, find_val)
            return False
        if node.value < find_val:
            if node.left:
                return self.innode_search(node.left, find_val)
            return False
        return False


   
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.print_tree())
#    4
#  2   5
# 1 3

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

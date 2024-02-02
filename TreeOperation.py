class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements   

    def post_order_traversal(self):
        elements = []
         

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        elements.append(self.data)    

        return elements     
    

    def find_min(self):
        min=self.data

        if self.left:
            min=self.left.find_min()
        else:
           return min  
        return min   
    
    def find_max(self):
        max=self.data

        if self.right:
            max=self.right.find_max()
        else:
           return max  
        return max   
    
    def find_sum(self):
        left_sum = self.left.find_sum() if self.left else 0
        right_sum = self.right.find_sum() if self.right else 0
        return self.data + left_sum + right_sum  

    def delete(self, val):
        if val< self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val >self.data:
            if self.right:
                self.right=self.right.delete(val)
        else: 
            if self.left is None and self.right is None:  
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left   
            """
            ######moving min value from right sub tree
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
            """

            ######moving max value from left sub tree
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self    










def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


"""
countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
print("pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
print("post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
print("minimum value is",numbers_tree.find_min())
print("maximum value is",numbers_tree.find_max())
print("sum of all values is",numbers_tree.find_sum())
"""

#numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree = build_tree([30,20,10])
print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
print(numbers_tree.search(5))
#print("after deleting 23:",numbers_tree.in_order_traversal())
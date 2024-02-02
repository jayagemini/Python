class solution:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def maxDepthDFS(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepthDFS(root.left),self.maxDepthDFS(root.right))




    def maxDepthBFS(self, root):
        if not root:
            return 0
        
        level=0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)    


            level+=1    

        return level



    def maxDepthIterative(self, root):
        stack=[[root,1]]
        result=0
        
        
        while stack:
            node,depth=stack.pop()

            if node:
                result=max(result,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
            

        return result


    root = [3,9,20,null,15,7]
    print (maxDepthDFS(self, root))
    print (maxDepthBFS(self, root))
    print (maxDepthIterative(self, root))




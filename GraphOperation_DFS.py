from collections import deque


graph = {
'A' : ['B','C','D'],
'B' : ['E'],
'C' : ['D','E'],
'D' : [],
'E' : []
}

visited =set () #list of visited nodes


def dfs_recursion(visted, graph, root):
    if root not in visited:
        print (root)
        visited.add(root)
        for neighbors in graph[root]:
            dfs_recursion(visted, graph, neighbors)



def dfs_stack(node,graph):
    visited_stack=[]
    if node not in graph:
        print("Node is not present in the graph")
        return
    stack=[]    
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited_stack:
            print (current)
            visited_stack.append(current)
            
            for neighbors in graph[current]:
                stack.append(neighbors)






print ("Following is the Breadth-First Search")   

dfs_recursion(visited,graph,'A')
print ("Following is the Depth-First Search")   
dfs_stack('A',graph)




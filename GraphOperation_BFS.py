graph = {
'5' : ['3','7'],
'3' : ['2','4'],
'7' : ['8'],
'2' : [],
'4' : ['8'],
'8' : []
}

visited =[] #list of visited nodes
queue=[] #initialize a queue

def bfs(visted, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m= queue.pop(0)
        print (m,end = " ")

        for neighbors in graph[m]:
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors) 

print ("Following is the Breadth-First Search")   

bfs(visited,graph,'5')




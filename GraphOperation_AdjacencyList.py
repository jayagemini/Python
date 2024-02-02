class Vertex:
	def __init__(self,n):
		self.name=n
		self.neighbors=list()
	def add_neighbor(self,v,weight):
		if v not in self.neighbors:
			self.neighbors.append((v,weight))
			
	    
class Graph:
	vertices={}
	def add_vertex(self,vertex):
		if isinstance(vertex,Vertex) and vertex not in self.vertices:
			self.vertices[vertex.name]=vertex
			return True
		else:
			return False
	def add_edge(self,u,v,weight):
		if u in list(self.vertices.keys()) and v in list(self.vertices.keys()):
			self.vertices[u].add_neighbor(u,weight)
			self.vertices[v].add_neighbor(v,weight)
			return True
		else:
			return False
	def print_graph(self):
		for key in list(self.vertices.keys()):
			print(key+' - '+ str(self.vertices[key].neighbors))	


g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	print( edge[:1])
	print(edge[1:])
	g.add_edge(edge[:1], edge[1:],0)

g.print_graph()
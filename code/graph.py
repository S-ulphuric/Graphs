class Graph(object):
	def __init__(self, graph_dict=None):
		if graph_dict == None:
			graph_dict = {}
		self.__graph_dict = graph_dict

	def vertices(self):
		return list(self.__graph_dict.keys())

	def edges(self):
		return self.__generate_edges()

	def add_vertex(self, vertex):
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def add_edge(self, edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
		edges = []
		for vertex in self.__graph_dict:
			for neighbour in self.__graph_dict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __str__(self):
		res = "vertices: "
		for k in self.__graph_dict:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self.__generate_edges():
			res += str(edge) + " "
		return res

	def find_path(self, start_vertex, end_vertex, path=[]):
		graph = self.__graph_dict
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return path
		if start_vertex not in graph:
			return None
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_path(vertex, end_vertex, path)
				if extended_path:
					return extended_path
		return None

	def find_all_paths(self, start_vertex, end_vertex, path=[]):
		graph = self.__graph_dict
		path = path  + [start_vertex]
		if start_vertex == end_vertex:
			return [path]
		if start_vertex not in graph:
			return []
		paths = []
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_paths = self.find_all_paths(vertex, end_vertex, path)
				for p in extended_paths:
					paths.append(p)
		return paths

	def vertex_degree(self, vertex):
		adj_vertices = self.__graph_dict[vertex]
		degree = len(adj_vertices) + adj_vertices.count(vertex)
		return degree

	def find_isolated_vertices(self):
		graph = self.__graph_dict
		isolated = []
		for vertex in graph:
			print(isolated, vertex)
			if not graph[vertex]:
				isolated += [vertex]
		return isolated

	def delta(self):
		min = 100000000
		for vertex in self.__graph_dict:
			vertex_degree = self.vertex_degree(vertex)
			if vertex_degree < min:
				min = vertex_degree
		return min

	def Delta(self):
		max = 0
		for vertex in self.__graph_dict:
			vertex_degree = self.vertex_degree(vertex)
			if vertex_degree > max:
				max = vertex_degree
		return max

	def degree_sequence(self):
		seq = []
		for vertex in self.__graph_dict:
			seq.append(self.vertex_degree(vertex))
		seq.sort(reverse=True)
		return tuple(seq)

	@staticmethod
	def is_degree_sequence(sequence):
		return all( x>=y for x, y in zip(sequence, sequence[1:]) )

	@staticmethod
	def erdoes_gallai(dsequence):
		if sum(dsequence) % 2:
			return False
		for k in range(1, len(dsequence) + 1):
			left = sum(dsequence[:k])
			right = k * (k-1) + sum([min(x,k) for x in dsequence[k:]])
			if left > right:
				return False
		return True

	def density(self):
		g = self.__graph_dict
		V = len(g.keys())
		E = len(self.edges())
		return 2.0 * E / (V * (V - 1))

	def is_connected(self, vertices_encountered = None, start_vertex=None):
		if vertices_encountered is None:
			vertices_encountered = set()
		gdict = self.__graph_dict
		vertices = list(gdict.keys())
		if not start_vertex:
			start_vertex = vertices[0]
		vertices_encountered.add(start_vertex)
		if len(vertices_encountered) != len(vertices):
			for vertex in gdict[start_vertex]:
				if vertex not in vertices_encountered:
					if self.is_connected(vertices_encountered, vertex):
						return True
		else:
			return True
		return False

	def diameter(self):
		v = self.vertices()
		pairs = [ (v[i], v[j]) for i in range(len(v)-1) for j in range(i+1, len(v)) ]
		smallest_paths = []
		for (s,e) in pairs:
			paths = self.find_all_paths(s,e)
			smallest = sorted(paths, key=len) [0]
			smallest_paths.append(smallest)

		smallest_paths.sort(key=len)

		diameter = len(smallest_paths[-1]) - 1
		return diameter

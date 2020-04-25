# Graphs
#A simple implementation of graphs in Python3

##Paths in Graphs

###Adjacent vertices:
Two vertices are adjacent when they are both incident to a common edge.

###Path in an undirected Graph:
A path in an undirected graph is a sequence of vertices P = ( v1, v2, ..., vn ) ∈ V x V x ... x V such that vi is adjacent to v{i+1} for 1 ≤ i < n. Such a path P is called a path of length n from v1 to vn.

###Simple Path:
A path with no repeated vertices is called a simple path.

##Degree

The degree of a vertex v in a graph is the number of edges connecting it, with loops counted twice. The degree of a vertex v is denoted deg(v). The maximum degree of a graph G, denoted by Δ(G), and the minimum degree of a graph, denoted by δ(G), are the maximum and minimum degree of its vertices. 

###The degree sum formula (Handshaking lemma):
![Degree sum formula](assets/lemma.jpg)

##Degree Sequence

The degree sequence of an undirected graph is defined as the sequence of its vertex degrees in a non-increasing order.

Isomorphic graphs have the same degree sequence. However, two graphs with the same degree sequence are not necessarily isomorphic.

There is the question whether a given degree sequence can be realized by a simple graph. The Erdös-Gallai theorem states that a non-increasing sequence of n numbers di (for i = 1, ..., n) is the degree sequence of a simple graph if and only if the sum of the sequence is even and the following condition is fulfilled: 
![Degree sequence formula](assets/deg_seq.jpg)

##Graph Density

The graph density is defined as the ratio of the number of edges of a given graph, and the total number of edges, the graph could have. In other words: It measures how close a given graph is to a complete graph.
The maximal density is 1, if a graph is complete. This is clear, because the maximum number of edges in a graph depends on the vertices and can be calculated as:
max. number of edges = ½ * |V| * ( |V| - 1 ).

On the other hand the minimal density is 0, if the graph has no edges, i.e. it is an isolated graph.
For undirected simple graphs, the graph density is defined as: 
![Graph Density formula](assets/gra_den.jpg)

A dense graph is a graph in which the number of edges is close to the maximal number of edges. A graph with only a few edges, is called a sparse graph. The definition for those two terms is not very sharp, i.e. there is no least upper bound (supremum) for a sparse density and no greatest lower bound (infimum) for defining a dense graph.

The precisest mathematical notation uses the big O notation:

Sparse Graph: Dense Graph:
A dense graph is a graph G = (V, E) in which |E| = Θ(|V|2). 

##Connected Graphs

A graph is said to be connected if every pair of vertices in the graph is connected. The example graph on the right side is a connected graph.

It possible to determine with a simple algorithm whether a graph is connected:

    1. Choose an arbitrary node x of the graph G as the starting point
    2. Determine the set A of all the nodes which can be reached from x.
    3. If A is equal to the set of nodes of G, the graph is connected; otherwise it is disconnected. 

##Distance and Diameter of a Graph

The distance "dist" between two vertices in a graph is the length of the shortest path between these vertices. No backtracks, detours, or loops are allowed for the calculation of a distance.

The eccentricity of a vertex s of a graph g is the maximal distance to every other vertex of the graph:
e(s) = max( { dist(s,v) | v ∈ V })
(V is the set of all vertices of g)

The diameter d of a graph is defined as the maximum eccentricity of any vertex in the graph. This means that the diameter is the length of the shortest path between the most distanced nodes. To determine the diameter of a graph, first find the shortest path between each pair of vertices. The greatest length of any of these paths is the diameter of the graph.

##Output when out.py is executed:
![Output of out.py](assets/out.jpg)
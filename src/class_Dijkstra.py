import math

class Dijkstra:
  """
  Implementation of Dijkstra's shortest path algorithm for weighted graphs.
  
  This class finds the shortest path from a source vertex to all other vertices
  in a weighted, undirected graph using Dijkstra's algorithm.
  
  Attributes:
    distances (dict): Distance from start vertex to each vertex
    visited (dict): Boolean status of whether each vertex has been visited
    predecessors (dict): Previous vertex in the shortest path for each vertex
    
  Example:
    >>> from class_Graph import Graph
    >>> g = Graph()
    >>> g.add_vertex('A')
    >>> g.add_vertex('B')
    >>> g.add_edge('A', 'B', 5)
    >>> dijkstra = Dijkstra(g, 'A')
    >>> dijkstra.find_min_unvisited(g)
    'A'
  """
  
  def __init__(self, graph, start_vertex):
    """
    Initialize Dijkstra's algorithm with a graph and starting vertex.
    
    Sets up the initial state:
    - All distances to infinity except start vertex (distance 0)
    - All vertices marked as unvisited
    - All predecessors set to None
    
    Args:
      graph (Graph): The graph object containing vertices and edges
      start_vertex (str): The vertex to start the algorithm from
      
    Note:
      The start_vertex must exist in the graph's adjacency list.
    """
    self.distances = {}
    self.visited = {}
    self.predecessors = {}
    for vertex in graph.adj_list.keys():
      self.distances[vertex] = math.inf
      self.visited[vertex] = False
      self.predecessors[vertex] = None
    self.distances[start_vertex] = 0

  def __str__(self):
    """
    Return string representation of the current algorithm state.
    
    Returns:
      str: Formatted string showing distances, visited status, and predecessors
    """
    return f"Distances: {self.distances}\n\nVisited: {self.visited}\n\nPredecessors: {self.predecessors}"
  
  def find_min_unvisited(self, graph):
    """
    Find the unvisited vertex with the minimum distance from start vertex.
    
    This is the core of Dijkstra's algorithm - selecting the next vertex
    to process based on shortest known distance.
    
    Args:
      graph (Graph): The graph object to search vertices in
      
    Returns:
      str or None: The vertex with minimum distance, or None if all visited
      
    Note:
      Returns None when all vertices have been visited or when no path exists
      to remaining unvisited vertices.
    """
    current_distance = math.inf
    min_unvisited_vertex = None
    for vertex in graph.adj_list.keys():
      if not self.visited[vertex] and self.distances[vertex] < current_distance:
        current_distance = self.distances[vertex]
        min_unvisited_vertex = vertex
    return min_unvisited_vertex
      
  def update_neighbors(self, graph, min_unvisited_vertex):
    """
    Update distances to neighbors of the current vertex if shorter paths are found.
    
    This method implements the relaxation step of Dijkstra's algorithm,
    checking if going through the current vertex provides a shorter path
    to its neighbors.
    
    Args:
      graph (Graph): The graph object containing adjacency information
      min_unvisited_vertex (str): The current vertex being processed
      
    Side Effects:
      - Updates self.distances for neighbors if shorter paths found
      - Updates self.predecessors to track the shortest path tree
    """
    for neighbor, weight in graph.adj_list[min_unvisited_vertex]:
      new_distance = self.distances[min_unvisited_vertex] + weight
      if new_distance < self.distances[neighbor]:
        self.distances[neighbor] = new_distance
        self.predecessors[neighbor] = min_unvisited_vertex

  def mark_visited(self, min_unvisited_vertex):
    """
    Mark a vertex as visited in Dijkstra's algorithm.
    
    Once a vertex is visited, its shortest distance from the start vertex
    is finalized and will not change.
    
    Args:
      min_unvisited_vertex (str): The vertex to mark as visited
    """
    self.visited[min_unvisited_vertex] = True

  def reconstruct_path(self, start_vertex, end_vertex):
    """
    Reconstruct the shortest path from start vertex to end vertex.
    
    Uses the predecessors dictionary built during the algorithm execution
    to trace back the shortest path recursively.
    
    Args:
      start_vertex (str): The starting vertex of the path
      end_vertex (str): The destination vertex of the path
      
    Returns:
      list: List of vertices representing the shortest path from start to end
      
    Example:
      >>> path = dijkstra.reconstruct_path('A', 'F')
      >>> print(path)
      ['A', 'P', 'O', 'N', 'H', 'G', 'F']
      
    Note:
      If no path exists, the method may return an incomplete path.
      Always check that dijkstra algorithm completed successfully first.
    """
    if start_vertex == end_vertex:
      return [start_vertex]
    
    path = self.reconstruct_path(start_vertex, self.predecessors[end_vertex])
    return path + [end_vertex]
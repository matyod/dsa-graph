class Graph:
  """
  A weighted undirected graph implementation using adjacency list representation.
  
  This class provides methods to create and manipulate a graph structure
  suitable for algorithms like Dijkstra's shortest path.
  
  Attributes:
    adj_list (dict): Adjacency list where keys are vertices and values are 
                    lists of tuples (neighbor, weight)
  
  Example:
    >>> g = Graph()
    >>> g.add_vertex('A')
    >>> g.add_vertex('B')
    >>> g.add_edge('A', 'B', 5)
    >>> print(g)
    {'A': [('B', 5)], 'B': [('A', 5)]}
  """
  
  def __init__(self):
    """
    Initialize an empty graph with an empty adjacency list.
    """
    self.adj_list = {}

  def __str__(self):
    """
    Return string representation of the graph's adjacency list.
    
    Returns:
      str: String representation of the adjacency list dictionary
    """
    return f"{self.adj_list}"  

  def add_vertex(self, vertex):
    """
    Add a new vertex to the graph.
    
    Args:
      vertex (str): The identifier for the new vertex
      
    Returns:
      str or None: Error message if vertex already exists, None otherwise
      
    Example:
      >>> g = Graph()
      >>> g.add_vertex('A')
      >>> g.add_vertex('A')  # Trying to add duplicate
      "❌ Error: Vertex 'A' already exist."
    """
    if vertex in self.adj_list:
      return f"❌ Error: Vertex '{vertex}' already exist."
    self.adj_list[vertex] = []

  def add_edge(self, u, v, weight):
    """
    Add a weighted edge between two vertices in the undirected graph.
    
    This method adds the edge in both directions since the graph is undirected.
    If the edge already exists, it won't be added again.
    
    Args:
      u (str): First vertex
      v (str): Second vertex  
      weight (int): Weight of the edge between u and v
      
    Note:
      Both vertices must already exist in the graph before adding an edge.
      
    Example:
      >>> g = Graph()
      >>> g.add_vertex('A')
      >>> g.add_vertex('B')
      >>> g.add_edge('A', 'B', 10)
    """
    if (v, weight) not in self.adj_list[u]:
      self.adj_list[u].append((v, weight))
    if (u, weight) not in self.adj_list[v]:
      self.adj_list[v].append((u, weight))

# import json
# import time
# import logging
import math
from models.graph import Graph
from algorithms.dijkstra import Dijkstra

class Pathfinder:
  def __init__(self):
    pass

  def build_graph_from_data(self, graph_data):
    new_graph = Graph()

    # Two-pass loading: vertices first, then edges
    for vertex in graph_data["vertices"]:
      new_graph.add_vertex(vertex["id"])

    for vertex in graph_data["vertices"]:
      for neighbor in vertex["neighbors"]:
        new_graph.add_edge(vertex["id"], neighbor[0], neighbor[1])

    return new_graph

  # Main public method
  def find_shortest_path(self, start_vertex, end_vertex, graph_data, tenant_id=None):
    graph = self.build_graph_from_data(graph_data)

    if start_vertex not in graph.adj_list:
      return self.format_response(False, None, "Start vertex does not exist.")
    
    if end_vertex not in graph.adj_list:
      return self.format_response(False, None, "End vertex does not exist.")

    dijkstra = Dijkstra(graph, start_vertex)

    while True:
      # Find the unvisited vertex with minimum distance
      min_unvisited_vertex = dijkstra.find_min_unvisited(graph)

      # Check if all vertices has been processed
      if min_unvisited_vertex == None:
        # Algorithm completed. All vertices processed
        break

      # Early terminate if reached target
      if min_unvisited_vertex == end_vertex:
        break

      # Update current vertex's distance to neighbors
      dijkstra.update_neighbors(graph, min_unvisited_vertex)

      # Mark current vertex as visited
      dijkstra.mark_visited(min_unvisited_vertex)

    if dijkstra.distances[end_vertex] == math.inf:
      return self.format_response(False, None, f"No path found from {start_vertex} to {end_vertex}.")

    shortest_path = dijkstra.reconstruct_path(start_vertex, end_vertex)

    return self.format_response(True, {
      "shortest_path": shortest_path,
      "distance": dijkstra.distances[end_vertex]
      })

  def format_response(self, success, data=None, error=None):
    return {
      "success": success,
      "data": data,
      "error": error
    }

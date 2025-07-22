# import json
# import time
# import logging
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
    pass

  def format_response(self, success, data=None, error=None):
    return {
      "success": success,
      "data": data,
      "error": error
    }

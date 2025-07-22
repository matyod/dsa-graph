# import json
# import time
# import logging
from models.graph import Graph
from algorithms.dijkstra import Dijkstra

class Pathfinder:
  def __init__(self):
    pass

  def build_graph_from_data(self, graph_data):
    pass

  # Main public method
  def find_shortest_path(self, start_vertex, end_vertex, graph_data, tenant_id=None):
    pass

  def format_response(self, success, data=None, error=None):
    return {
      "success": success,
      "data": data,
      "error": error
    }

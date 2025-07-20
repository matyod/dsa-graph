import os
import json
from src.graph import Graph
from src.dijkstra import Dijkstra

# Get the path to the graph data file
current_file_root = os.path.dirname(os.path.abspath(__file__))
data_file_name = 'data/graph_data.json'
data_file_dir = os.path.join(current_file_root, data_file_name)

# Load graph data from JSON file
with open(data_file_dir) as f:
  vertices_data = json.load(f)

# Initialize empty graph
g = Graph()

# Two-pass loading: vertices first, then edges
for vertex in vertices_data["vertices"]:
  g.add_vertex(vertex['id'])

for vertex in vertices_data["vertices"]:
  for neighbor in vertex["neighbors"]:
    g.add_edge(vertex['id'], neighbor[0], neighbor[1])

# Set up Dijkstra's algorithm
start_vertex = "A"
end_vertex = "Q"
dijkstra = Dijkstra(g, start_vertex)
print(f"Dijkstra: {dijkstra}\n")

# Main algorithm loop
while True:
  # Find the unvisited vertex with minimum distance
  min_unvisited_vertex = dijkstra.find_min_unvisited(g)
  
  # Check if all vertices have been processed
  if min_unvisited_vertex == None:
    print("Algorithm complete. All vertices processed.\n")
    break
  # else:
  #   print(f"Minimum unvisited vertex: {min_unvisited_vertex}\n")

  # Early termination if reached target
  if min_unvisited_vertex == end_vertex:
    print(f"Shortest path from {start_vertex} to {end_vertex} distance: {dijkstra.distances[end_vertex]}\n")
    break

  # Update distances to neighbors of current vertex
  dijkstra.update_neighbors(g, min_unvisited_vertex)
  # print(f"Updated distances: {dijkstra.distances}\n")

  # Mark current vertex as visited
  dijkstra.mark_visited(min_unvisited_vertex)
  # print(f"Updated visited: {dijkstra.visited}\n")

# Reconstruct and display the shortest path
path = dijkstra.reconstruct_path(start_vertex, end_vertex)
display = "Path: "
for v in path:
  if v == path[-1]:
    display += f"{v}"
  else:
    display += f"{v} → "
print(display)

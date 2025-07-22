import os, json, sys
from config import DATA_DIRECTORY
from models.graph import Graph
from algorithms.dijkstra import Dijkstra

# for x in sys.path:
#   print(x)

# Get the path to the graph data file
data_file = os.path.join(DATA_DIRECTORY, 'graph_data.json')

# Load graph data from JSON file
with open(data_file) as f:
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

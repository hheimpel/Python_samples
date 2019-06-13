from itertools import combinations
import numpy as np

def tri_area(v1, v2, v3):
  return np.linalg.norm(np.cross(v1-v2, v1-v3))/2
  
def biggest_triang_int(point_list, center, radius):
  #Filter points outside of sphere
  points_within_sphere = [np.array(point) for point in point_list if np.linalg.norm(np.array(point)-np.array(center)) < radius]

  #list of possible triangle areas
  possible_vertices = list(combinations(points_within_sphere, 3))
  areas = [tri_area(p[0], p[1], p[2]) for p in possible_vertices]
  try:
    max_area = max(areas)
  except ValueError:
    return []

  triangles = []
  for index, value in enumerate(areas):
    if value == max_area:
      triangles.append([list(p) for p in possible_vertices[index]])
  if len(triangles) == 1:
    return [len(possible_vertices), max(areas), triangles[0]]
  else:
    return [len(possible_vertices), max(areas), triangles]
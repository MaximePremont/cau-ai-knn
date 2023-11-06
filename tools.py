# cau-ai-knn, by Maxime PREMONT

import math

def euclidean_distance_4d(point1, point2):
  x1, y1, z1, t1 = point1
  x2, y2, z2, t2 = point2
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2 + (t2 - t1) ** 2)
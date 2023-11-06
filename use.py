# cau-ai-knn, by Maxime PREMONT

from knn import Knn
import sys
from point import Point

# Init
knn = Knn()
f = open("knn.model", "r")
k = knn.load_points(f)
f.close()
knn.find_types()

if len(sys.argv) < 5:
  print('Usage: python3 use.py <x> <y> <z> <t>')
  exit(1)

point = Point(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), '?')
knn.find_type(k, point)
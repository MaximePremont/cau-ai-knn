# cau-ai-knn, by Maxime PREMONT

from point import Point
from tools import euclidean_distance_4d

class Knn:
  def __init__(self):
    self.points = []
    self.types = []

  def find_type(self, k, point):
    distances = []
    for p in self.points:
      distance = euclidean_distance_4d((p.x, p.y, p.z, p.t), (point.x, point.y, point.z, point.t))
      distances.append((distance, p.type))

    distances.sort(key=lambda x: x[0])
    distances = distances[:k]
    counts = []
    for t in self.types:
      counts.append((t, 0))
    for d in distances:
      for i in range(len(counts)):
        if d[1] == counts[i][0]:
          counts[i] = (counts[i][0], counts[i][1] + 1)
          break
    counts.sort(key=lambda x: x[1], reverse=True)
    print('point = {}, type = {}'.format(point, counts[0][0]))
    return counts[0][0]


  def find_best_k(self):
    rates = []
    for k in range(1, len(self.points)):
      correct_count = 0
      for point in self.points:
        if self.find_type(k, point) == point.type:
          correct_count += 1
      rates.append((k, correct_count / len(self.points)))
      print('> k = {}, correct rate = {}'.format(k, correct_count / len(self.points)))
    rates.sort(key=lambda x: x[1], reverse=True)
    best = rates[0]
    while best[0] < 3:
      print('cleaning k = {}'.format(best[0]))
      rates.pop(0)
      best = rates[0]
    print('=> best k = {}, correct rate = {}'.format(best[0], best[1]))
    return best[0]

  def write_points(self, f):
    for p in self.points:
      f.write(str(p) + '\n')

  def load_points(self, f):
    lines = f.readlines()
    k = -1
    for line in lines:
      if (line.startswith('k=')):
        k = int(line[2:])
        break
      point = Point(0, 0, 0, 0, '')
      point.init_by_str(line)
      self.points.append(point)
    return k

  def find_types(self):
    for point in self.points:
      found = 0
      for type in self.types:
        if point.type == type:
          found = 1
          break
      if found == 0:
        self.types.append(point.type)
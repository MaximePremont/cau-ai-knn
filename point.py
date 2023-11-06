# cau-ai-knn, by Maxime PREMONT

class Point:
  def __init__(self, x, y, z, t, type):
    self.x = x
    self.y = y
    self.z = z
    self.t = t
    self.type = type
  def init_by_str(self, str):
    data = str.split(',')
    self.x = float(data[0])
    self.y = float(data[1])
    self.z = float(data[2])
    self.t = float(data[3])
    self.type = data[4].replace('\n', '')
  def __str__(self):
    return '{},{},{},{},{}'.format(self.x, self.y, self.z, self.t, self.type)
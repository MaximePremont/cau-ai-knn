# cau-ai-knn, by Maxime PREMONT

from knn import Knn

knn = Knn()
f = open("iris.data", "r")
knn.load_points(f)
f.close()
knn.find_types()

f = open("knn.model", "w")

knn.write_points(f)
k = knn.find_best_k()

f.write('k={}'.format(k))

f.close()
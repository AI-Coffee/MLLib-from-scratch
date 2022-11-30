import numpy as np
from sklearn.cluster import KMeans as sk_KMeans
from cluster.KMeans import KMeans

X = np.array([[58, 27],
              [3, 53],
              [73, 55],
              [55, 34],
              [58, 79],
              [17, 42],
              [48, 96],
              [99, 87],
              [28, 25],
              [1, 87],
              [52, 46],
              [4, 17],
              [58, 54],
              [64, 2],
              [71, 63],
              [33, 18],
              [22, 69],
              [53, 94],
              [83, 6],
              [4, 68],
              [42, 49],
              [19, 60],
              [94, 30],
              [36, 85],
              [98, 88],
              [34, 6],
              [74, 76],
              [8, 50],
              [72, 88],
              [16, 59],
              [94, 69],
              [77, 6],
              [94, 74],
              [30, 56],
              [43, 98],
              [67, 51],
              [20, 5],
              [30, 20],
              [0, 95],
              [43, 17],
              [10, 61],
              [27, 99],
              [83, 8],
              [40, 40],
              [67, 86],
              [52, 87],
              [80, 5],
              [82, 95],
              [90, 54],
              [59, 79],
              [10, 44],
              [65, 0],
              [53, 49],
              [96, 34],
              [12, 24],
              [28, 1],
              [17, 16],
              [41, 80],
              [48, 16],
              [83, 67],
              [56, 75],
              [84, 4],
              [22, 17],
              [24, 20],
              [79, 17],
              [63, 71],
              [66, 87],
              [88, 75],
              [89, 44],
              [10, 53],
              [74, 91],
              [8, 45],
              [72, 50],
              [64, 14],
              [26, 87],
              [88, 5],
              [94, 77],
              [26, 12],
              [43, 23],
              [82, 68],
              [14, 91],
              [2, 12],
              [34, 93],
              [46, 10],
              [57, 20],
              [29, 56],
              [77, 29],
              [29, 69],
              [47, 69],
              [70, 86],
              [40, 60]])

print('-------------With k-means++')
kmeans_1 = KMeans(n_clusters=3, max_iter=10000)
kmeans_1.fit(X, visualized=True)
print(kmeans_1._centroids)
print('-------------Without k-means++')
kmeans_2 = KMeans(n_clusters=3, max_iter=10000, init='random')
kmeans_2.fit(X, visualized=True)
print(kmeans_2._centroids)
sk_kmeans = sk_KMeans(n_clusters=3, max_iter=10000)
sk_kmeans.fit(X)
print('-------------With scikit-learn')
print(sk_kmeans.cluster_centers_)
print(np.sum(np.min(np.sum((X - sk_kmeans.cluster_centers_[:, np.newaxis]) ** 2, axis=2) ** (1 / 2), axis=0)))

import tensorflow as tf
import numpy as np

class Cluster():
    def __init__(self, num_clusters, steps = 1000):
        self.num_clusters = num_clusters
        self.kmean = tf.contrib.learn.KMeansClustering(num_clusters = self.num_clusters, model_dir = "/home/chung/Desktop/Music/tmp")
        self.steps = steps

    def fit(self, data):
        def input_fn():
            X = tf.constant(data, tf.float32)
            return (X, None)

        self.kmean.fit(input_fn = input_fn, steps = self.steps)
        # self.kmean.export_savedmodel("/home/chung/Desktop/Music/tmp", )

    def centroid(self):
        return self.kmean.clusters()

    def prediction(self, data):
        def input_fn():
            X = tf.constant(data, tf.float32)
            return (X, None)

        predict_group = self.kmean.predict(input_fn=input_fn, as_iterable=True)
        group = []
        for t in predict_group:
            group.append(t['cluster_idx'])

        return np.array(group)

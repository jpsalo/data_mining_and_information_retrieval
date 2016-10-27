from sklearn import cluster
import numpy as np

import graph
import utilities


# http://sujitpal.blogspot.hu/2014/08/topic-modeling-with-gensim-over-past.html
# http://stackoverflow.com/a/6657095/7010222
def kmeans_cluster_analysis(data, x_attribute, y_attribute, data_set_name, attributes, target_variable=None):
    MAX_CLUSTERS = 10

    numbers_of_clusters = range(1, MAX_CLUSTERS + 1)

    data_numpy_array = data.as_matrix()
    x_attribute_name = attributes[x_attribute]
    y_attribute_name = attributes[y_attribute]

    kmeans = kmeans_clustering(data_numpy_array, numbers_of_clusters)
    inertias = [clustering.inertia_ for clustering in kmeans]
    elbow = find_elbow(kmeans, numbers_of_clusters, inertias, MAX_CLUSTERS)
    print('elbow ' + str(numbers_of_clusters[elbow]))

    clustering_elbow = graph.generate_clustering_elbow(numbers_of_clusters, inertias, elbow, data_set_name)
    utilities.process_plot(clustering_elbow, 'k-means_elbow', data_set_name)

    cluster_scatter_plot = graph.generate_cluster_scatter_plot(data_numpy_array, kmeans[elbow], data_set_name,
                                                               str(numbers_of_clusters[elbow]), x_attribute, y_attribute,
                                                               x_attribute_name, y_attribute_name)
    utilities.process_plot(cluster_scatter_plot, 'cluster', data_set_name, [x_attribute_name, y_attribute_name])


def kmeans_clustering(data, clusters):
    kmeans = [cluster.KMeans(n_clusters=number_of_clusters).fit(data) for number_of_clusters in clusters]

    return kmeans


def find_elbow(kmeans, clusters, inertias, MAX_CLUSTERS):
    diff = np.zeros(MAX_CLUSTERS)
    diff2 = np.zeros(MAX_CLUSTERS)
    diff3 = np.zeros(MAX_CLUSTERS)

    for clustering in kmeans:
        number_of_clusters = clustering.get_params()['n_clusters']
        if number_of_clusters > 1:
            diff[number_of_clusters - 1] = inertias[number_of_clusters - 1] - inertias[number_of_clusters - 2]
        if number_of_clusters > 2:
            diff2[number_of_clusters - 1] = diff[number_of_clusters - 1] - diff[number_of_clusters - 2]
        if number_of_clusters > 3:
            diff3[number_of_clusters - 1] = diff2[number_of_clusters - 1] - diff2[number_of_clusters - 2]

    return np.argmin(diff3[3:]) + 3

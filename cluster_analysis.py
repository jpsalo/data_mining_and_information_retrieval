from sklearn import cluster

import graph
import utilities


def kmeans_cluster_analysis(data, clusters, x_attribute, y_attribute, data_set_name, attributes):
    data_numpy_array = data.as_matrix()
    x_attribute_name = attributes[x_attribute]
    y_attribute_name = attributes[y_attribute]

    kmeans = kmeans_clustering(data_numpy_array, clusters)
    cluster_scatter_plot = graph.generate_cluster_scatter_plot(data_numpy_array, kmeans, data_set_name,
                                                               'k-Means Clusters', x_attribute, y_attribute,
                                                               x_attribute_name, y_attribute_name)
    utilities.process_plot(cluster_scatter_plot, 'cluster', data_set_name, [x_attribute_name, y_attribute_name])


def kmeans_clustering(data, clusters):
    kmeans = cluster.KMeans(n_clusters=clusters)
    kmeans.fit(data)

    return kmeans

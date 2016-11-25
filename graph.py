import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram

matplotlib.style.use('ggplot')


# UNIVARIATE STATISTICS


# NOMINAL, ORDINAL
# Frequencies
def generate_frequency(values, data_set_name, title, x_label, x_tick_labels=None):
    title = title + '\n' + data_set_name

    fig = plt.figure()
    plot = values.plot.bar(title=title)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')
    if x_tick_labels is not None:
        plt.xticks(np.arange(len(values)), x_tick_labels)
    return fig


# QUANTITATIVE

# Distributions
def generate_histogram(data, attribute, data_set_name, title, x_label, log_scale=False):
    title = title + '\n' + data_set_name
    values = data[attribute]

    fig = plt.figure()
    # http://stackoverflow.com/a/21033789
    plot = values.plot.hist(title=title, bins=20, bottom=0.1, logy=log_scale)
    plot.set_xlabel(x_label)
    y_label = 'Frequency (log)' if log_scale else 'Frequency'
    plot.set_ylabel(y_label)
    return fig


# Standard deviation
def generate_standard_deviation(data, attribute, data_set_name, title, log_scale=False):
    title = title + '\n' + data_set_name
    values = data[attribute]
    means = values.mean()
    errors = values.std()
    fig, ax = plt.subplots()
    plot = pd.Series(means).plot.bar(title=title, yerr=errors, ax=ax, logy=log_scale)
    if log_scale:
        plot.set_ylabel('log')
    return fig


# Location
def generate_box_plot(data, attribute, data_set_name, x_label, hide_fliers=False, log_scale=False):
    values_df = pd.DataFrame(data[attribute])
    title = ('Quartiles (without outliers)' if hide_fliers else 'Quartiles') + '\n' + data_set_name

    fig = plt.figure()

    plot = values_df.boxplot(return_type='axes', showfliers=not hide_fliers)
    if log_scale:
        plot.set_yscale('log')
        plot.set_ylabel('log')
    plt.xticks([1], [x_label])

    plot.set_title(title)
    return fig


# BIVARIATE STATISTICS


def generate_scatter_plot(data, x_attribute, y_attribute, data_set_name, title, x_label, y_label):
    title = title + '\n' + data_set_name
    plot = data.plot.scatter(x=x_attribute, y=y_attribute)
    plot.set_title(title)
    plot.set_ylabel(y_label)
    plot.set_xlabel(x_label)
    return plot


# http://stackoverflow.com/a/13674286
# https://blog.mafr.de/2012/03/11/time-series-data-with-matplotlib/
# http://stackoverflow.com/a/17004818
def generate_time_series(data, x_attribute, y_attribute, data_set_name, title, x_label, y_label):
    title = title + '\n' + data_set_name
    fig, ax = plt.subplots()
    ax.plot_date(x=data[x_attribute], y=data[y_attribute])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return fig


def generate_scatter_matrix(data, title):
    plot = pd.scatter_matrix(data, diagonal='hist')
    plt.suptitle(title)  # http://stackoverflow.com/a/39787437/7010222
    return plot


# CLUSTERING


def generate_clustering_elbow(numbers_of_clusters, inertias, elbow, data_set_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(numbers_of_clusters, inertias, 'b*-')
    ax.plot(numbers_of_clusters[elbow], inertias[elbow], marker='o', markersize=12, markeredgewidth=2, markeredgecolor='r',
            markerfacecolor='None')
    plt.grid(True)
    plt.xlabel('Number of clusters')
    plt.ylabel('Average within-cluster sum of squares')
    plt.title('Elbow for k-means clustering' + '\n' + data_set_name)
    return fig


def generate_cluster_scatter_plot(data, kmeans, data_set_name, number_of_clusters, x_attribute, y_attribute, x_label, y_label):
    title = 'k-means cluster with k=' + number_of_clusters + '\n' + data_set_name
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    fig, ax = plt.subplots()

    colors = labels.astype(np.float)
    ax.scatter(data[:, x_attribute], data[:, y_attribute], c=colors)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', alpha=1, s=200)

    return fig


def generate_dendrogram(linkage_matrix, data_set_name):
    title = 'Hierarchical Clustering Dendrogram' + '\n' + data_set_name
    # calculate full dendrogram
    fig = plt.figure(figsize=(20, 10))
    plt.title(title)
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    dendrogram(
        linkage_matrix,
        leaf_rotation=90.,  # rotates the x axis labels
    )

    return fig

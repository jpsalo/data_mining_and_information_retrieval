import matplotlib.pyplot as plt
import pandas as pd

import cluster_analysis
import config

# Read the files
blogs = pd.read_csv(config.BLOGS['path'], header=None)
posts = pd.read_csv(config.POSTS['path'])

cluster_analysis.kmeans_cluster_analysis(blogs, 55, 50, config.BLOGS['name'], config.BLOGS['attributes'])

# For presentation and debug
# http://stackoverflow.com/a/25163682
if config.DEBUG_MODE:
    plt.show()

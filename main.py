import matplotlib.pyplot as plt
import pandas as pd

import univariate_analysis
import bivariate_analysis
import cluster_analysis
import frequent_pattern_mining
import config

# Read the files
# blogs = pd.read_csv(config.BLOGS['path'], header=None)
# posts = pd.read_csv(config.POSTS['path'])
# 
# univariate_analysis.analyze_blogs(blogs)
# univariate_analysis.analyze_posts(posts)
# 
# bivariate_analysis.analyze_blogs(blogs)
# bivariate_analysis.analyze_posts(posts)
# 
# cluster_analysis.kmeans_cluster_analysis(blogs, 55, 50, config.BLOGS['name'], config.BLOGS['attributes'])
# 
# cluster_analysis.hierarchical_clustering_analysis(blogs, config.BLOGS['name'])

clickstream = config.CLICKSTREAM['path']
clickstream_csv = config.CLICKSTREAM['path_csv']

fraction = .2
minimum_support = .4
frequent_pattern_mining.frequent_itemsets_apriori(clickstream, config.CLICKSTREAM['name'], fraction, minimum_support)
frequent_pattern_mining.frequent_itemsets_fp_growth(clickstream_csv, config.CLICKSTREAM['name'], fraction,
                                                    minimum_support)

# For presentation and debug
# http://stackoverflow.com/a/25163682
if config.DEBUG_MODE:
    plt.show()

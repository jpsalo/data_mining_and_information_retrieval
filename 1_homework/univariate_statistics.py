import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

posts = pd.read_csv('~/Dropbox/koulu/data_mining_and_information_retrieval/HN_posts_year_to_Sep_26_2016.csv')
posts_sample = posts.sample(n = 100)

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL

# Lengths of the blog post titles

titles = posts['title']

title_lengths = list(map(lambda x: len(x), titles))

df = pd.Series(title_lengths).value_counts().sort_index()

plt.figure(1)
plot = df.plot.bar(title ='Lengths of the titles')
plot.set_xlabel('Length (characters)')
plot.set_ylabel('Frequency')

# QUANTITATIVE

# Distributions

# Number of comments the posts received

comments = posts['num_comments'].value_counts().sort_index()

plt.figure(2)
plot = comments.plot.hist(title = 'Number of comments the posts received', bins=20)
plot.set_xlabel('Comments')
plot.set_ylabel('Frequency')

# http://stackoverflow.com/a/25163682
plt.show()

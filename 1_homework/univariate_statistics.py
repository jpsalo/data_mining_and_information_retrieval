import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

posts = pd.read_csv('~/Dropbox/koulu/data_mining_and_information_retrieval/HN_posts_year_to_Sep_26_2016.csv')
posts_sample = posts.sample(n = 100)

plt.figure()

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL

# Lengths of the blog post titles

titles = posts['title']

title_lengths = list(map(lambda x: len(x), titles))

df = pd.Series(title_lengths).value_counts().sort_index()

plot = df.plot.bar(title ='Lengths of the titles')
plot.set_xlabel('Length (characters)')
plot.set_ylabel('Frequency')

plt.show()

plt.figure()

# QUANTITATIVE

# Distributions

# Number of comments the posts received

comments = posts_sample['num_comments'].value_counts().sort_index()

plot = comments.plot.bar(title ='Number of comments the posts received')
plot.set_xlabel('Comments')
plot.set_ylabel('Frequency')

# http://stackoverflow.com/a/25163682
plt.show()

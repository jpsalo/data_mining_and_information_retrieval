import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

posts = pd.read_csv('~/Dropbox/koulu/data_mining_and_information_retrieval/HN_posts_year_to_Sep_26_2016.csv')

posts_sample = posts.sample(n = 100)
posts_comments = posts_sample["num_comments"].value_counts().sort_index()

plt.figure()

plot = posts_comments.plot.bar(title = 'Number of comments the posts received')
plot.set_xlabel('comments')
plot.set_ylabel('amount')

# http://stackoverflow.com/a/25163682
plt.show()

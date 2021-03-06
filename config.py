from os.path import expanduser

DEBUG_MODE = False
home = expanduser("~")  # http://stackoverflow.com/a/4028943

BASE_PATH = home + '/Dropbox/school/data_mining_and_information_retrieval/'
OUTPUT_PATH = BASE_PATH + 'output/'
FIGURE_PATH = BASE_PATH + 'figures/'

BLOGS = {
    'name': 'blog_posts',
    'path': BASE_PATH + 'BlogFeedback/blogData_train.csv',
    'attributes': {50: 'comments', 55: 'trackbacks'}
}

POSTS = {
    'name': 'hacker_news_posts',
    'path': BASE_PATH + 'HN_posts_year_to_Sep_26_2016.csv'
}

CLICKSTREAM = {
        'name': 'clickstream',
        'path': BASE_PATH + 'clickstream/kosarak10k_tab_delimited.txt',
        'path_csv': BASE_PATH + 'clickstream/kosarak10k.csv'
}

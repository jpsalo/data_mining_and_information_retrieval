import utilities
import graph

import config


def analyze_blogs(blogs):
    data_set_name = config.BLOGS['name']
    generate_weekday_frequencies(blogs, data_set_name)

    print('Generated weekday frequencies')
    generate_blog_post_lengths(blogs, data_set_name)
    print('Generated blog post lengths')
    generate_number_of_comments_before_basetime(blogs, data_set_name)
    print('Generated number of comments before basetime')
    calculate_mean_absolute_deviation_blogs(blogs, data_set_name)
    print('Calculated mean absolute deviation')
    generate_standard_deviation_blogs(blogs, data_set_name)
    print('Generated standard deviation')
    generate_box_plot_blogs(blogs, data_set_name)
    generate_box_plot_without_outliers_blogs(blogs, data_set_name)
    print('Generated box plot')


def analyze_posts(posts):
    data_set_name = config.BLOGS['name']

    generate_posts_title_lengths(posts, data_set_name)
    print('Generated posts title lengths')
    generate_number_of_comments_histogram(posts, data_set_name)
    print('Generated number of comments histogram')
    calculate_mean_absolute_deviation_posts(posts, data_set_name)
    print('Calculated mean absolute deviation')
    generate_standard_deviation_posts(posts, data_set_name)
    print('Generated standard deviation')
    generate_box_plot_posts(posts, data_set_name)
    generate_box_plot_without_outliers_posts(posts, data_set_name)
    print('Generated box plot')


# Weekday of the date of publication of the blog post
def generate_weekday_frequencies(data, data_set_name):
    weekday_frequencies = utilities.get_weekday_frequencies(data)
    weekday_labels = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
    frequency_figure = graph.generate_frequency(weekday_frequencies, data_set_name,
                                                'Day of the publication of the blog posts', 'Weekday', weekday_labels)
    utilities.process_plot(frequency_figure, 'frequency', data_set_name,
                           ['weekdays'])


# Lengths of the blog post titles
def generate_posts_title_lengths(data, data_set_name):
    posts_title_lengths = utilities.calculate_lengths(data, 'title')
    frequency_figure = graph.generate_frequency(posts_title_lengths, data_set_name,
                                                'Lengths of the titles',
                                                'Length (characters)')
    utilities.process_plot(frequency_figure, 'frequency', data_set_name,
                           ['title_lengths'])


# Lengths of the blog posts
def generate_blog_post_lengths(data, data_set_name):
    blog_text_lengths = utilities.generate_bins(data[61])
    frequency_figure = graph.generate_frequency(blog_text_lengths, data_set_name,
                                                'Lengths of the blog posts',
                                                'Length (characters)')
    utilities.process_plot(frequency_figure, 'frequency', data_set_name,
                           ['post_lengths'])


def generate_number_of_comments_histogram(data, data_set_name):
    histogram_figure = graph.generate_histogram(data, 'num_comments', data_set_name,
                                                'Number of comments the posts received', 'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['comments'])


def generate_number_of_comments_before_basetime(data, data_set_name):
    histogram_figure = graph.generate_histogram(data, 50, data_set_name,
                                                'Total number of comments before basetime',
                                                'Comments', True)
    utilities.process_plot(histogram_figure, 'frequency', data_set_name,
                           ['comments'])


def calculate_mean_absolute_deviation_posts(data, data_set_name):
    utilities.calculate_mean_absolute_deviation(data, 'num_comments', data_set_name, 'comments')


def calculate_mean_absolute_deviation_blogs(data, data_set_name):
    utilities.calculate_mean_absolute_deviation(data, 50, data_set_name, 'comments')


def generate_standard_deviation_posts(data, data_set_name):
    standard_deviation_figure = graph.generate_standard_deviation(data, 'num_comments',
                                                                  data_set_name,
                                                                  'Standard deviation of the number of comments', True)
    utilities.process_plot(standard_deviation_figure, 'standard_deviation', data_set_name,
                           ['comments'])


def generate_standard_deviation_blogs(data, data_set_name):
    standard_deviation_figure = graph.generate_standard_deviation(data, 50, data_set_name,
                                                                  'Standard deviation of the number of comments', True)
    utilities.process_plot(standard_deviation_figure, 'standard_deviation', data_set_name,
                           ['comments'])


def generate_box_plot_posts(data, data_set_name):
    box_plot_figure = graph.generate_box_plot(data, 'num_points', data_set_name, 'Comments',
                                              log_scale=True)
    utilities.process_plot(box_plot_figure, 'box_plot', data_set_name,
                           ['comments'])


def generate_box_plot_without_outliers_posts(data, data_set_name):
    box_plot_without_outliers_figure = graph.generate_box_plot(data, 'num_points', data_set_name,
                                                               'Comments', True)
    utilities.process_plot(box_plot_without_outliers_figure, 'box_plot', data_set_name,
                           ['comments_without_outliers'])


def generate_box_plot_blogs(data, data_set_name):
    box_plot_figure = graph.generate_box_plot(data, 50,
                                              data_set_name, 'Comments', log_scale=True)
    utilities.process_plot(box_plot_figure, 'box_plot', data_set_name,
                           ['comments'])


def generate_box_plot_without_outliers_blogs(data, data_set_name):
    box_plot_without_outliers_figure = graph.generate_box_plot(data, 50,
                                                               data_set_name, 'Comments',
                                                               True)
    utilities.process_plot(box_plot_without_outliers_figure, 'box_plot', data_set_name,
                           ['comments_without_outliers'])

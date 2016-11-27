import utilities
import graph
import pandas as pd
import config


def analyze_blogs(data):
    data_set_name = config.BLOGS['name']
    scatter_matrix_all(data, data_set_name)
    scatter_matrix_with_parent(data, data_set_name)
    scatter_matrix_without_parent(data, data_set_name)
    scatter_matrix_with_trackbacks(data, data_set_name)
    scatter_matrix_without_trackbacks(data, data_set_name)
    scatter_matrix_with_parent_with_trackbacks(data, data_set_name)
    scatter_matrix_with_parent_without_trackbacks(data, data_set_name)
    scatter_matrix_without_parent_with_trackbacks(data, data_set_name)
    scatter_matrix_without_parent_without_trackbacks(data, data_set_name)
    number_of_comments_with_parents(data, data_set_name)
    number_of_comments_with_trackbacks(data, data_set_name)
    number_of_comments_without_trackbacks(data, data_set_name)
    number_of_comments_without_parent_with_trackbacks(data, data_set_name)
    number_of_comments_without_parent_without_trackbacks(data, data_set_name)
    number_of_comments_with_parent_with_trackbacks(data, data_set_name)
    number_of_comments_with_parent_without_trackbacks(data, data_set_name)
    correlation_posts_length(data, data_set_name)
    correlation_comments_posts_length_without_parent(data, data_set_name)


def analyze_posts(data):
    data_set_name = config.POSTS['name']
    correlation_between_comments_and_points(data, data_set_name)
    comments_by_hour_of_submission(data, data_set_name)


def correlation_between_comments_and_points(data, data_set_name):
    scatter_plot = graph.generate_scatter_plot(data, 'num_comments', 'num_points', data_set_name,
                                               'Correlation between comments and points', 'Comments', 'Points')
    utilities.process_plot(scatter_plot, 'scatter_plot', data_set_name, ['comments_points'])


def comments_by_hour_of_submission(data, data_set_name):
    posts_slice = data[['num_comments', 'created_at']]
    posts_slice['created_at_time'] = posts_slice['created_at'].apply(utilities.parse_time)
    time_series_figure = graph.generate_time_series(posts_slice, 'created_at_time', 'num_comments',
                                                    data_set_name,
                                                    'Comments by hour of submission', 'Hour of submission', 'Comments')
    utilities.process_plot(time_series_figure, 'time_series', data_set_name, ['comments'])


def get_blogs_slice(data):
    blogs_slice = pd.DataFrame(data[[50, 55, 61, 276]])
    blogs_slice.columns = ['comments', 'trackbacks', 'length', 'parent_pages']
    return blogs_slice


def get_blogs_with_parent(data):
    blogs_slice = get_blogs_slice(data)
    return blogs_slice[blogs_slice['parent_pages'] > 0]


def get_blogs_with_trackbacks(data):
    blogs_slice = get_blogs_slice(data)
    return blogs_slice[blogs_slice['trackbacks'] > 0]


def get_blogs_without_trackbacks(data):
    blogs_slice = get_blogs_slice(data)
    blogs_without_trackbacks = blogs_slice[blogs_slice['trackbacks'] == 0]
    blogs_without_trackbacks = blogs_without_trackbacks[['comments', 'length', 'parent_pages']]
    return blogs_without_trackbacks


def get_blogs_without_parent(data):
    blogs_slice = get_blogs_slice(data)
    blogs_without_parent = blogs_slice[blogs_slice['parent_pages'] == 0]
    blogs_without_parent = blogs_without_parent[['comments', 'trackbacks', 'length']]
    return blogs_without_parent


def get_blogs_without_parent_without_trackbacks(data):
    blogs_without_parent = get_blogs_without_parent(data)
    blogs_without_parent_without_trackbacks = blogs_without_parent[blogs_without_parent['trackbacks'] == 0]
    blogs_without_parent_without_trackbacks = blogs_without_parent_without_trackbacks[['comments', 'length']]
    return blogs_without_parent_without_trackbacks


def get_blogs_without_parent_with_trackbacks(data):
    blogs_without_parent = get_blogs_without_parent(data)
    blogs_without_parent_with_trackbacks = blogs_without_parent[blogs_without_parent['trackbacks'] > 0]
    return blogs_without_parent_with_trackbacks


def get_blogs_with_parent_without_trackbacks(data):
    blogs_with_parent = get_blogs_with_parent(data)
    blogs_with_parent_without_trackbacks = blogs_with_parent[blogs_with_parent['trackbacks'] == 0]
    blogs_with_parent_without_trackbacks = blogs_with_parent_without_trackbacks[['comments', 'length', 'parent_pages']]
    return blogs_with_parent_without_trackbacks


def get_blogs_with_parent_with_trackbacks(data):
    blogs_with_parent = get_blogs_with_parent(data)
    blogs_with_parent_with_trackbacks = blogs_with_parent[blogs_with_parent['trackbacks'] > 0]
    return blogs_with_parent_with_trackbacks


def scatter_matrix_all(data, data_set_name):
    blogs_slice = get_blogs_slice(data)
    title = 'All ' + str(len(blogs_slice))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_slice, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name, ['all'])


def scatter_matrix_with_parent(data, data_set_name):
    blogs_with_parent = get_blogs_with_parent(data)
    title = 'With parent ' + str(len(blogs_with_parent))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name, ['with_parent'])


def scatter_matrix_without_parent(data, data_set_name):
    blogs_without_parent = get_blogs_without_parent(data)
    title = 'Without parent ' + str(len(blogs_without_parent))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name, ['without_parent'])


def scatter_matrix_with_trackbacks(data, data_set_name):
    blogs_with_trackbacks = get_blogs_with_trackbacks(data)
    title = 'With trackbacks ' + str(len(blogs_with_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name, ['with_trackbacks'])


def scatter_matrix_without_trackbacks(data, data_set_name):
    blogs_without_trackbacks = get_blogs_without_trackbacks(data)
    title = 'Without trackbacks ' + str(len(blogs_without_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name,
                           ['without_trackbacks'])


def scatter_matrix_with_parent_with_trackbacks(data, data_set_name):
    blogs_with_parent_with_trackbacks = get_blogs_with_parent_with_trackbacks(data)
    title = 'With parent, with trackbacks ' + str(len(blogs_with_parent_with_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent_with_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name,
                           ['with_parent_with_trackbacks'])


def scatter_matrix_with_parent_without_trackbacks(data, data_set_name):
    blogs_with_parent_without_trackbacks = get_blogs_with_parent_without_trackbacks(data)
    title = 'With parent, without trackbacks ' + str(len(blogs_with_parent_without_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent_without_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name,
                           ['with_parent_without_trackbacks'])


def scatter_matrix_without_parent_with_trackbacks(data, data_set_name):
    blogs_without_parent_with_trackbacks = get_blogs_with_parent_with_trackbacks(data)
    title = 'Without parent, with trackbacks ' + str(len(blogs_without_parent_with_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent_with_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name,
                           ['without_parent_with_trackbacks'])


def scatter_matrix_without_parent_without_trackbacks(data, data_set_name):
    blogs_without_parent_without_trackbacks = get_blogs_without_parent_without_trackbacks(data)
    title = 'Without parent, without trackbacks ' + str(len(blogs_without_parent_without_trackbacks))
    scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent_without_trackbacks, title)
    utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', data_set_name,
                           ['without_parent_without_trackbacks'])


def number_of_comments_with_parents(data, data_set_name):
    blogs_with_parent = get_blogs_with_parent(data)
    title = 'Number of comments the posts with parent (' + str(len(blogs_with_parent)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_with_parent, 'comments', data_set_name, title,
                                                'Comments',
                                                True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name, ['with_parent_comments'])


def number_of_comments_with_parent_with_trackbacks(data, data_set_name):
    blogs_with_parent_with_trackbacks = get_blogs_with_parent_with_trackbacks(data)
    title = 'Number of comments the posts with parent, with trackbacks (' + str(
        len(blogs_with_parent_with_trackbacks)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_with_parent_with_trackbacks, 'comments',
                                                data_set_name, title, 'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['with_parent_with_trackbacks_comments'])


def number_of_comments_with_parent_without_trackbacks(data, data_set_name):
    blogs_with_parent_without_trackbacks = get_blogs_with_parent_without_trackbacks(data)
    title = 'Number of comments the posts with parent, without trackbacks (' + str(
        len(blogs_with_parent_without_trackbacks)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_with_parent_without_trackbacks, 'comments',
                                                data_set_name, title, 'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['with_parent_without_trackbacks_comments'])


def number_of_comments_with_trackbacks(data, data_set_name):
    blogs_with_trackbacks = get_blogs_with_trackbacks(data)
    title = 'Number of comments the posts with trackbacks (' + str(len(blogs_with_trackbacks)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_with_trackbacks, 'comments', data_set_name,
                                                title, 'Comments',
                                                True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name, ['with_trackbacks_comments'])


def number_of_comments_without_parent_with_trackbacks(data, data_set_name):
    blogs_without_parent_with_trackbacks = get_blogs_without_parent_with_trackbacks(data)
    title = 'Number of comments the posts without parent, with trackbacks ({0}) received'.format(
        str(len(blogs_without_parent_with_trackbacks)))
    histogram_figure = graph.generate_histogram(blogs_without_parent_with_trackbacks, 'comments',
                                                data_set_name,
                                                title, 'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['without_parent_with_trackbacks_comments'])


def number_of_comments_without_parent_without_trackbacks(data, data_set_name):
    blogs_without_parent_without_trackbacks = get_blogs_without_parent_with_trackbacks(data)
    title = 'Number of comments the posts without parent, without trackbacks (' + \
            str(len(blogs_without_parent_without_trackbacks)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_without_parent_without_trackbacks, 'comments',
                                                data_set_name,
                                                title, 'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['without_parent_without_trackbacks_comments'])


def number_of_comments_without_trackbacks(data, data_set_name):
    blogs_without_trackbacks = get_blogs_without_trackbacks(data)
    title = 'Number of comments the posts without trackbacks (' + str(len(blogs_without_trackbacks)) + ') received'
    histogram_figure = graph.generate_histogram(blogs_without_trackbacks, 'comments', data_set_name,
                                                title,
                                                'Comments', True)
    utilities.process_plot(histogram_figure, 'histogram', data_set_name,
                           ['without_trackbacks_comments'])


def correlation_comments_posts_length_without_parent(data, data_set_name):
    blogs_without_parent = get_blogs_without_parent(data)
    scatter_plot = graph.generate_scatter_plot(blogs_without_parent, 'length', 'comments',
                                               data_set_name,
                                               'Correlation between comments and the post length (without parent)',
                                               'Comments', 'Length')
    utilities.process_plot(scatter_plot, 'scatter_plot', data_set_name,
                           ['comments_length_without_parent'])


def correlation_posts_length(data, data_set_name):
    blogs_with_parent = get_blogs_with_parent(data)
    scatter_plot = graph.generate_scatter_plot(blogs_with_parent, 'length', 'comments',
                                               data_set_name,
                                               'Correlation between comments and the post length', 'Comments', 'Length')
    utilities.process_plot(scatter_plot, 'scatter_plot', data_set_name, ['comments_length'])

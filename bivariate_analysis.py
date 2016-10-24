import utilities
import graph
from main import blogs, posts

scatter_plot = graph.generate_scatter_plot(posts, 'num_comments', 'num_points', utilities.get_data_set_name('posts'),
                                           'Correlation between comments and points', 'Comments', 'Points')
utilities.process_plot(scatter_plot, 'scatter_plot', utilities.get_data_set_name('posts'), 'comments_points')

posts_slice = posts[['num_comments', 'created_at']]
posts_slice['created_at_time'] = posts_slice['created_at'].apply(utilities.parse_time)
time_series_figure = graph.generate_time_series(posts_slice, 'created_at_time', 'num_comments',
                                                utilities.get_data_set_name('posts'),
                                                'Comments by hour of submission', 'Hour of submission', 'Comments')
utilities.process_plot(time_series_figure, 'time_series', utilities.get_data_set_name('posts'), 'comments')

blogs_slice = pd.DataFrame(blogs[[50, 55, 61, 276]])
blogs_slice.columns = ['comments', 'trackbacks', 'length', 'parent_pages']

blogs_with_parent = blogs_slice[blogs_slice['parent_pages'] > 0]

blogs_with_trackbacks = blogs_slice[blogs_slice['trackbacks'] > 0]
blogs_without_trackbacks = blogs_slice[blogs_slice['trackbacks'] == 0]
blogs_without_trackbacks = blogs_without_trackbacks[['comments', 'length', 'parent_pages']]

blogs_without_parent = blogs_slice[blogs_slice['parent_pages'] == 0]
blogs_without_parent = blogs_without_parent[['comments', 'trackbacks', 'length']]

blogs_without_parent_with_trackbacks = blogs_without_parent[blogs_without_parent['trackbacks'] > 0]
blogs_without_parent_with_trackbacks = blogs_without_parent_with_trackbacks[['comments', 'trackbacks', 'length']]

blogs_without_parent_without_trackbacks = blogs_without_parent[blogs_without_parent['trackbacks'] == 0]
blogs_without_parent_without_trackbacks = blogs_without_parent_without_trackbacks[['comments', 'length']]

blogs_with_parent_without_trackbacks = blogs_with_parent[blogs_with_parent['trackbacks'] == 0]
blogs_with_parent_without_trackbacks = blogs_with_parent_without_trackbacks[['comments', 'length', 'parent_pages']]

blogs_with_parent_with_trackbacks = blogs_with_parent[blogs_with_parent['trackbacks'] > 0]

print('In total ' + str(len(blogs_slice)))
print('')

print('With trackbacks, with or without parent ' + str(len(blogs_with_trackbacks)))
print('With parent, with or without trackbacks ' + str(len(blogs_with_parent)))

print('')

print('Without parent, with or without trackbacks ' + str(len(blogs_without_parent)))
print('Without trackbacks, with or without parent ' + str(len(blogs_without_trackbacks)))

print('')

print('Without parent, without trackbacks ' + str(len(blogs_without_parent_without_trackbacks)))
print('Without parent, with trackbacks ' + str(len(blogs_without_parent_with_trackbacks)))

print('')

print('With parent, without trackbacks ' + str(len(blogs_with_parent_without_trackbacks)))
print('With parent, with trackbacks ' + str(len(blogs_with_parent_with_trackbacks)))

title = 'All ' + str(len(blogs_slice))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_slice, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'), 'all')

title = 'With parent ' + str(len(blogs_with_parent))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'), 'with_parent')

title = 'Without parent ' + str(len(blogs_without_parent))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'), 'without_parent')

title = 'With trackbacks ' + str(len(blogs_with_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'), 'with_trackbacks')

title = 'Without trackbacks ' + str(len(blogs_without_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'),
                       'without_trackbacks')

title = 'With parent, with trackbacks ' + str(len(blogs_with_parent_with_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent_with_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'),
                       'with_parent_with_trackbacks')

title = 'With parent, without trackbacks ' + str(len(blogs_with_parent_without_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_with_parent_without_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'),
                       'with_parent_without_trackbacks')

title = 'Without parent, with trackbacks ' + str(len(blogs_without_parent_with_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent_with_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'),
                       'without_parent_with_trackbacks')

title = 'Without parent, without trackbacks ' + str(len(blogs_without_parent_without_trackbacks))
scatter_matrix_figure = graph.generate_scatter_matrix(blogs_without_parent_without_trackbacks, title)
utilities.process_plot(scatter_matrix_figure, 'scatter_matrix', utilities.get_data_set_name('blogs'),
                       'without_parent_without_trackbacks')

title = 'Number of comments the posts with parent (' + str(len(blogs_with_parent)) + ') received'
histogram_figure = graph.generate_histogram(blogs_with_parent, 'comments', utilities.get_data_set_name('blogs'), title,
                                            'Comments',
                                            True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'), 'with_parent_comments')

title = 'Number of comments the posts with parent, with trackbacks (' + str(
    len(blogs_with_parent_with_trackbacks)) + ') received'
histogram_figure = graph.generate_histogram(blogs_with_parent_with_trackbacks, 'comments',
                                            utilities.get_data_set_name('blogs'), title, 'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'),
                       'with_parent_with_trackbacks_comments')

title = 'Number of comments the posts with parent, without trackbacks (' + str(
    len(blogs_with_parent_without_trackbacks)) + ') received'
histogram_figure = graph.generate_histogram(blogs_with_parent_without_trackbacks, 'comments',
                                            utilities.get_data_set_name('blogs'), title, 'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'),
                       'with_parent_without_trackbacks_comments')

title = 'Number of comments the posts with trackbacks (' + str(len(blogs_with_trackbacks)) + ') received'
histogram_figure = graph.generate_histogram(blogs_with_trackbacks, 'comments', utilities.get_data_set_name('blogs'),
                                            title, 'Comments',
                                            True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'), 'with_trackbacks_comments')

title = 'Number of comments the posts without parent, with trackbacks ({0}) received'.format(
    str(len(blogs_without_parent_with_trackbacks)))
histogram_figure = graph.generate_histogram(blogs_without_parent_with_trackbacks, 'comments',
                                            utilities.get_data_set_name('blogs'),
                                            title, 'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'),
                       'without_parent_with_trackbacks_comments')

title = 'Number of comments the posts without parent, without trackbacks (' + \
        str(len(blogs_without_parent_without_trackbacks)) + ') received'
histogram_figure = graph.generate_histogram(blogs_without_parent_without_trackbacks, 'comments',
                                            utilities.get_data_set_name('blogs'),
                                            title, 'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'),
                       'without_parent_without_trackbacks_comments')

title = 'Number of comments the posts without trackbacks (' + str(len(blogs_without_trackbacks)) + ') received'
histogram_figure = graph.generate_histogram(blogs_without_trackbacks, 'comments', utilities.get_data_set_name('blogs'),
                                            title,
                                            'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('blogs'),
                       'without_trackbacks_comments')

# TODO: Plot the above

blogs_slice.columns = ['Comments', 'Number of links (trackbacks)', 'Post length', 'Number of parent pages']

scatter_plot = graph.generate_scatter_plot(blogs_without_parent, 'length', 'comments',
                                           utilities.get_data_set_name('blogs'),
                                           'Correlation between comments and the post length (without parent)',
                                           'Comments', 'Length')
utilities.process_plot(scatter_plot, 'scatter_plot', utilities.get_data_set_name('blogs'),
                       'comments_length_without_parent')

scatter_plot = graph.generate_scatter_plot(blogs_with_parent, 'length', 'comments',
                                           utilities.get_data_set_name('blogs'),
                                           'Correlation between comments and the post length', 'Comments', 'Length')
utilities.process_plot(scatter_plot, 'scatter_plot', utilities.get_data_set_name('blogs'), 'comments_length')

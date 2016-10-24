import utilities
import graph
from main import blogs, posts

# Weekday of the date of publication of the blog post
weekday_frequencies = utilities.get_weekday_frequencies(blogs)
weekday_labels = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
frequency_figure = graph.generate_frequency(weekday_frequencies, utilities.get_data_set_name('blogs'),
                                            'Day of the publication of the blog posts', 'Weekday', weekday_labels)
utilities.process_plot(frequency_figure, 'frequency', utilities.get_data_set_name('blogs'), 'weekdays')

# Lengths of the blog post titles
posts_title_lengths = utilities.calculate_lengths(posts, 'title')
frequency_figure = graph.generate_frequency(posts_title_lengths, utilities.get_data_set_name('posts'),
                                            'Lengths of the titles',
                                            'Length (characters)')
utilities.process_plot(frequency_figure, 'frequency', utilities.get_data_set_name('posts'), 'title_lengths')

# Lengths of the blog posts
blog_text_lengths = utilities.generate_bins(blogs[61])
frequency_figure = graph.generate_frequency(blog_text_lengths, utilities.get_data_set_name('blogs'),
                                            'Lengths of the blog posts',
                                            'Length (characters)')
utilities.process_plot(frequency_figure, 'frequency', utilities.get_data_set_name('blogs'), 'post_lengths')

histogram_figure = graph.generate_histogram(posts, 'num_comments', utilities.get_data_set_name('posts'),
                                            'Number of comments the posts received', 'Comments', True)
utilities.process_plot(histogram_figure, 'histogram', utilities.get_data_set_name('posts'), 'comments')

histogram_figure = graph.generate_histogram(blogs, 50, utilities.get_data_set_name('blogs'),
                                            'Total number of comments before basetime',
                                            'Comments', True)
utilities.process_plot(histogram_figure, 'frequency', utilities.get_data_set_name('blogs'), 'comments')

utilities.calculate_mean_absolute_deviation(posts, 'num_comments', utilities.get_data_set_name('posts'), 'comments')
utilities.calculate_mean_absolute_deviation(blogs, 50, utilities.get_data_set_name('blogs'), 'comments')

standard_deviation_figure = graph.generate_standard_deviation(posts, 'num_comments',
                                                              utilities.get_data_set_name('posts'),
                                                              'Standard deviation of the number of comments', True)
utilities.process_plot(standard_deviation_figure, 'standard_deviation', utilities.get_data_set_name('posts'),
                       'comments')

standard_deviation_figure = graph.generate_standard_deviation(blogs, 50, utilities.get_data_set_name('blogs'),
                                                              'Standard deviation of the number of comments', True)
utilities.process_plot(standard_deviation_figure, 'standard_deviation', utilities.get_data_set_name('blogs'),
                       'comments')

box_plot_figure = graph.generate_box_plot(posts, 'num_points', utilities.get_data_set_name('posts'), 'Comments',
                                          log_scale=True)
utilities.process_plot(box_plot_figure, 'box_plot', utilities.get_data_set_name('posts'), 'comments')

box_plot_without_outliers_figure = graph.generate_box_plot(posts, 'num_points', utilities.get_data_set_name('posts'),
                                                           'Comments', True)
utilities.process_plot(box_plot_without_outliers_figure, 'box_plot', utilities.get_data_set_name('posts'),
                       'comments_without_outliers')

box_plot_figure = graph.generate_box_plot(blogs, 50, utilities.get_data_set_name('blogs'), 'Comments', log_scale=True)
utilities.process_plot(box_plot_figure, 'box_plot', utilities.get_data_set_name('blogs'), 'comments')

box_plot_without_outliers_figure = graph.generate_box_plot(blogs, 50, utilities.get_data_set_name('blogs'), 'Comments',
                                                           True)
utilities.process_plot(box_plot_without_outliers_figure, 'box_plot', utilities.get_data_set_name('blogs'),
                       'comments_without_outliers')

import pygal
from dvisual import util

chart= pygal.Line()
chart.title = 'Linux IO Model Performance'
chart.x_title = 'Number of Descriptors Monitored'
chart.y_title = 'CPU Time (seconds)'
chart.x_labels = (10, 100, 1000, 10000)

chart.add('poll()', [0.61, 2.9, 35, 990])
chart.add('select()', [0.73, 3.0, 35, 930])
chart.add('epoll()', [0.41, 0.42, 0.53, 0.66])

util.render_pygal(chart)

import pygal
from dvisual import util


chart = pygal.StackedLine(fill=True, interpolate='cubic')
chart.title = 'Programming Language Rate'
chart.x_title = 'Years'
chart.y_title = '%'

chart.x_labels = (2013, 2014, 2015)

chart.add('Python', [30.30, 31.24, 26.67])
chart.add('Java', [22.20, 19.57, 22.58])
chart.add('C++', [13.00, 9.79, 9.96])
chart.add('C#', [5.00, 7.37, 9.39])
chart.add('C', [4.10, 6.07, 7.37])
chart.add('JavaScript', [5.20, 6.48, 6.88])
chart.add('Ruby', [10.60, 7.11, 5.88])
chart.add('PHP', [3.30, 7.11, 5.88])

util.render_pygal(chart)

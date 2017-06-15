import pygal
from dvisual import util

chart= pygal.Line()
chart.title = 'Speed of Process Creation'
chart.x_title = 'Total Virtual Memory (MB)'
chart.y_title = 'Time to Create 100,000 processes (seconds)'
chart.x_labels = (1.70, 2.70, 11.70)

chart.add('fork()', [22.27, 26.38, 126.93])
chart.add('vfork()', [3.52, 3.55, 3.53])
chart.add('clone()', [2.97, 2.98, 2.93])
chart.add('fork() + exec()', [135.72, 146.15, 260.34])
chart.add('vfork() + exec()', [107.36, 107.81, 107.97])

util.render_pygal(chart)

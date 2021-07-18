# Import libraries using import keyword
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import one_sine

# Setting Plot and Axis variables as subplots()
# function returns tuple(fig, ax)
Plot, Axis = plt.subplots()

# Adjust the bottom size according to the
# requirement of the user
plt.subplots_adjust(bottom=0.25)

# Set the x and y axis to some dummy data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(2*np.pi * t)

# times = one_sine.get_times()
# a_440 = one_sine.create_sine_wave(times, freq=440, amp=5)
# normalized = one_sine.normalize_data(a_440)
# int_data = one_sine.quantize_wave(normalized)

# plot the x and y using plot function
l = plt.plot(t,s)
# l = plt.plot(times, int_data)

# Choose the Slider color
slider_color = 'White'

# Set the axis and slider position in the plot
axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],
						facecolor = slider_color)
slider_position = Slider(axis_position,
						'Pos', 0.1, 90.0)

# update() function to change the graph when the
# slider is in use
def update(val):
	pos = slider_position.val
	Axis.axis([pos, pos+10, -1, 1])
	Plot.canvas.draw_idle()

# update function called using on_changed() function
slider_position.on_changed(update)

# Display the plot
plt.show()

# sample function from matplotlib site
# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph
#
#     Parameters
#     ----------
#     ax : Axes
#         The axes to draw to
#
#     data1 : array
#        The x data
#
#     data2 : array
#        The y data
#
#     param_dict : dict
#        Dictionary of kwargs to pass to ax.plot
#
#     Returns
#     -------
#     out : list
#         list of artists added
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out

# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(1, 1)
# my_plotter(ax, data1, data2, {'marker': 'x'})
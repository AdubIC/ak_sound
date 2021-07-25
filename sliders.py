# example from matplot.lib.org/stable/gallery/widgets/slider_demo.html
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def plot_wave(sec, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * sec)


sec = np.linspace(0, 1, 1000)

# Initial parameters
init_amplitude = 5
init_frequency = 3


# function returns tuple(fig, ax)
fig, ax = plt.subplots()
line, = plt.plot(sec, plot_wave(sec, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')

axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# Adjust the bottom to make room for sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# horizontal slider for frequency
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
freq_slider = Slider(
    ax=axfreq,
    label='Frquency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

# vertical slider for amplitude
axamp = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolor)
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)

# function to call when slider value changes
def update(val):
    line.set_ydata(plot_wave(sec, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()

# register update function with each slider
freq_slider.on_changed(update)
amp_slider.on_changed(update)

# Create a widget button to reset sliders to initial values
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)

plt.show()
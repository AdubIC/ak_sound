import matplotlib.figure as fg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import one_sine
import wave_math as wav
import numpy as np

fig = fg.Figure(figsize=(25,10), facecolor='white')
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)


# why do I need to worry about x values
a_x, a_y = one_sine.create_sine_wave(duration = 1.0, freq=220, amp =5)
b_x, b_y = one_sine.create_sine_wave(duration = 1.0, freq=440, amp =3)
c_x, c_y = one_sine.create_sine_wave(duration = 1.0, freq=880, amp =2)
m_x, m_y = one_sine.create_sine_wave(duration=1.0,freq = 20, amp =2)

ax1.set_xlim(0,0.1)
ax2.set_xlim(0,0.1)
ax3.set_xlim(0,0.1)
ax4.set_xlim(0,0.1)

abc = np.array([a_y, b_y, c_y])
d = wav.add_waves(abc)
mod_d = wav.mod_waves(d, m_y)

t0a, = ax1.plot(a_x, a_y)
t0b, = ax1.plot(b_x, b_y)
t0c, = ax1.plot(c_x, c_y)
t1, = ax2.plot(a_x, d)
t2, = ax3.plot(m_x, m_y)
t3, = ax4.plot(a_x, mod_d)

fig.legend((t0a, t0b, t0c),('220 Hz sine wave', ' 440 Hz', '880 Hz'))

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()




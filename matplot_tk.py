import matplotlib.figure as fg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import waves
#import one_sine
#import wave_math as wav
import numpy as np


def _destroyWindow():
    root.quit()
    root.destroy()

# TODO add plotting function from this code and matplotlib tutorial
# move global code to main function
if __name__ == '__main__':
    # why do I need to worry about x values
    a_x, a_y = waves.create_sine_wave(duration=1.0, freq=220, amp=5)
    b_x, b_y = waves.create_sine_wave(duration=1.0, freq=440, amp=3)
    c_x, c_y = waves.create_sine_wave(duration=1.0, freq=880, amp=2)
    m_x, m_y = waves.create_sine_wave(duration=1.0, freq=20, amp=2)

    abc = np.array([a_y, b_y, c_y])
    d = waves.add_waves(abc)
    mod_d = waves.mod_waves(d, m_y)

    # TODO create array of all waves and normalize, quantize them
    wave_array = [a_y, b_y, c_y, d, m_y, mod_d]
    normalized = [waves.normalize_data(w) for w in wave_array]
    int_data = [waves.quantize_wave(w) for w in wave_array]

    #wav.write("sine_with_func.wav", SAMPLES_PER_SEC, int_data)
    #plot_wave(DURATION_S, int_data)

    fig = fg.Figure(figsize=(25,20), facecolor='white')
    ax1 = fig.add_subplot(411)
    ax2 = fig.add_subplot(412)
    ax3 = fig.add_subplot(413)
    ax4 = fig.add_subplot(414)

    # TODO loop through axes collection
    ax1.set_xlim(0,0.1)
    ax2.set_xlim(0,0.1)
    ax3.set_xlim(0,0.1)
    ax4.set_xlim(0,0.1)

    ax1.set_title('Individual waves 220, 440, 880 Hz')
    ax2.set_title('Resultant wave from adding sine waves above')
    ax3.set_title('Modulating wave 20 Hz')
    ax4.set_title('Combined sine waves after multipled by modulating wave')


    t0a, = ax1.plot(a_x, int_data[0])
    t0b, = ax1.plot(b_x, int_data[1])
    t0c, = ax1.plot(c_x, int_data[2])
    t1, = ax2.plot(a_x, int_data[3])
    t2, = ax3.plot(m_x, int_data[4])
    t3, = ax4.plot(a_x, int_data[5])

    fig.legend((t0a, t0b, t0c),('220 Hz sine wave', ' 440 Hz', '880 Hz'))


    root = tk.Tk()
    root.withdraw()
    root.protocol('WM_DELETE_WINDOW', _destroyWindow)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.update()
    root.deiconify()
    root.mainloop()




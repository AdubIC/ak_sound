import numpy as np
import one_sine


def add_waves(wave_array):
    result = sum(wave_array)
    return result

def mod_waves(wave1, mod_wave):
    result = wave1 * mod_wave
    return result

if __name__ == '__main__':
    # why do I need to worry about x values
    a_x, a_y = one_sine.create_sine_wave(duration = 1.0, freq=440, amp =5)
    b_x, b_y = one_sine.create_sine_wave(duration = 1.0, freq=880, amp =3)
    c_x, c_y = one_sine.create_sine_wave(duration = 1.0, freq=1760, amp =2)
    m_x, m_y = one_sine.create_sine_wave(duration=1.0,freq = 10, amp =2)

    abc = np.array([a_y, b_y, c_y])
    d = add_waves(abc)
    mod_d = mod_waves(d, m_y)
    print(d)
    print(mod_d)

    #plot_duration = 3/440
    #one_sine.plot_wave(plot_duration,d)
    plot_duration = 3/10
    one_sine.plot_wave(plot_duration,mod_d)
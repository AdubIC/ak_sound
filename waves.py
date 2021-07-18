import numpy as np
import matplotlib.pyplot as plt

SAMPLES_PER_SEC = 44100
DURATION_S = 1
num_samples = SAMPLES_PER_SEC * DURATION_S


def get_times(duration_s=1.0, sample_rate=44100):
    ts = np.linspace(0., duration_s, round(duration_s * sample_rate))
    return ts


# why do I worry about x values an not just assume 0 to duration * samples
def create_sine_wave(duration=1.0, freq=440, amp=1.0):
    ts = get_times(duration)
    samples = amp * np.sin(np.pi * 2 * freq * ts)
    return ts, samples


def normalize_data(data):
    # make sure amplitude is not 0
    max_amp = max(max(data), abs(min(data)))
    normal_data = data / max_amp
    return normal_data


# why not do in one step with normalize
def quantize_wave(data, samp_rate=44100):
    # make amplitude half of the int16 min/max
    if max(data) > 1:
        data = normalize_data(data)
    # check to see if normalized to -1 to 1
    # keep this close to max rather than .5
    desired_amplitude = np.iinfo(np.int16).max * .5
    samples = np.int16(desired_amplitude * data)
    return samples


# need to fix this so data is truncated to duration * sample_rate
def plot_wave(duration, data):
    num_samples = round(duration * SAMPLES_PER_SEC)
    ts = np.linspace(0, duration, num_samples)
    plt.plot(ts, data[:num_samples])
    # plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()


def add_waves(wave_array):
    result = sum(wave_array)
    return result


def mod_waves(wave1, mod_wave):
    result = wave1 * mod_wave
    return result

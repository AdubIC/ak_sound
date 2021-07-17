# make simple sine wave, record, and graph

import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import time
import matplotlib.pyplot as plt

SAMPLES_PER_SEC = 44100
DURATION_S = 1
num_samples = SAMPLES_PER_SEC * DURATION_S


# phase add later
# shift up and down need?

def get_times(duration_s=1.0, sample_rate=44100):
    ts = np.linspace(0., duration_s, round(duration_s * sample_rate))
    return ts


def create_sine_wave(duration=1.0, freq=440, amp=1.0):
    ts = get_times(duration)
    samples = amp * np.sin(np.pi * 2 * freq * ts)
    return ts, samples


def normalize_data(data):
    max_amp = max(max(data), abs(min(data)))
    normal_data = data / max_amp
    return normal_data


def quantize_wave(data, samp_rate=44100):
    # make amplitude half of the int16 min/max
    if max(data) > 1:
        data = normalize_data(data)
    # check to see if normalized to -1 to 1
    desired_amplitude = np.iinfo(np.int16).max * .5
    samples = np.int16(desired_amplitude * data)
    return samples

# need to fix this so data is truncated to duration * sample_rate
def plot_wave(duration, data):
    num_samples = round(duration*SAMPLES_PER_SEC)
    ts = np.linspace(0, duration, num_samples)
    plt.plot(ts, data[:num_samples])
    #plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

if __name__ == '__main__':
    #times = get_times()
    times, a_440 = create_sine_wave(duration=1.0, freq=440, amp=5)
    normalized = normalize_data(a_440)
    int_data = quantize_wave(normalized)
    wav.write("sine_with_func.wav", SAMPLES_PER_SEC, int_data)
    plot_wave(DURATION_S, int_data)


    print(f"times: {min(times)} - {max(times)}, length {len(times)} ({len(times) / SAMPLES_PER_SEC} seconds)")
    print(f"y vals: {min(a_440)} - {max(a_440)}")
    print(f"normalized y vals: {min(normalized)} - {max(normalized)}")
    print(f"quantized y vals: {min(int_data)} - {max(int_data)}")

    # wavefile.read returns sample rate and sample data
    # 1d numpy array for 1-channel (nsamples)
    # or 2d array for 2-channels (nsamples, nchannels)
    samp_rate, wave_from_file = wav.read("sine_with_func.wav")
    dur_s = wave_from_file.shape[0] / samp_rate
    print(f"wave from file duration: {dur_s} seconds")
    print(f"wave from file y vals: {min(wave_from_file)} - {max(wave_from_file)}")

    # play wave from original and from file
    sd.play(int_data, SAMPLES_PER_SEC)
    time.sleep(DURATION_S)
    sd.play(wave_from_file, samp_rate)
    time.sleep(dur_s)
    sd.stop()


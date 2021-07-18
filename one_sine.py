# make simple sine wave, record, and graph

import numpy as np
import scipy.io.wavfile as wav
# import sounddevice as sd
import time
import matplotlib.pyplot as plt

SAMPLES_PER_SEC = 44100
DURATION_S = 1
num_samples = SAMPLES_PER_SEC * DURATION_S


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
#    sd.play(int_data, SAMPLES_PER_SEC)
 #   time.sleep(DURATION_S)
 #   sd.play(wave_from_file, samp_rate)
 #   time.sleep(dur_s)
 #   sd.stop()


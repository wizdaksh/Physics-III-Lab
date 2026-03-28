import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

SAMPLE_RATE = 44100 # Hz; rate at which curve is sampled

# Generate a sine wave of a given frequency and duration, sampled at some rate
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration) # Samples
    frequencies = x * freq # Sampled frequencies
    y = np.sin((2 * np.pi) * frequencies) # A sine wave with amplitude 1
    return x, y # return arrays of sample indices and sampled frequency

# Sine wave lasting 5 s; input sine wave frequency
f = float(input('Sine wave frequency [Hertz]:  '))
DURATION = int(input('Sine wave duration [whole number of seconds]:  '))
x, y = generate_sine_wave(f, SAMPLE_RATE, DURATION)

# Fourier analysis
N = SAMPLE_RATE * DURATION
xft = fftfreq(N, 1 / SAMPLE_RATE) # Middle of frequency bins
yft = fft(y) # Power of each sampled frequency

# 2 plots on same canvas; show only first 1000 elements of frequency spectrum
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

axs[0].plot(x, y, 'k-')
axs[0].set_title('Sine Wave as a Function of Time')
axs[0].set_xlabel('Time [s]')
axs[0].set_ylabel('Amplitude')

# Plot the absolute value (magnitude) of the complex FFT output
axs[1].plot(xft[:1000], np.abs(yft[:1000]), 'k-')
axs[1].set_title('Frequency Spectrum of Sine Wave')
axs[1].set_xlabel('Frequency [Hz]')
axs[1].set_ylabel('Power')

plt.tight_layout() # Prevents overlapping text between subplots
plt.show()

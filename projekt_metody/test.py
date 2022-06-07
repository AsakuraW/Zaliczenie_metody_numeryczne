from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.io import wavfile


dzwiek = wave.open("tone16.wav","r")
print(dzwiek.readframes(-1))

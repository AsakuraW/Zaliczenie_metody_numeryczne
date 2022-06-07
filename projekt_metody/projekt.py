import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import wave
from scipy.io import wavfile
import scipy
#źródła/pomoc: https://sound.eti.pg.gda.pl/,https://geek.justjoin.it/,https://matplotlib.org/


#pierwszy spektrometr
def spect(rate,dzwiek2):
    czestotliwosc, czas, spekt = sig.spectrogram(dzwiek2, fs=rate, nperseg=2048, noverlap=1536,scaling='spectrum', mode='magnitude')
    plt.pcolormesh(czas, czestotliwosc, spekt)
    plt.xlabel('Czas [s]')
    plt.ylabel('Częstotliwość [Hz]')
    plt.title('Spektrogram')
    plt.ylim(0, 10000)
    db=plt.colorbar()
    return plt.show()

#amplituda sygnału cyfrowego
def sygnal(rate,dzwiek2,nazwa):
    sample = len(dzwiek2) #Ilość próbek
    dlugosc = sample / rate #Długość ścieżki audio
    dzwiek = wave.open(nazwa,"r") #Wczytywanie dzwięku za pomocą biblioteki wave
    #wyodrębnienie pliku wav
    plik = dzwiek.readframes(-1)
    plik = np.fromstring(plik, dtype="int16")
    print("Czestotliwość próbkowania:", rate)
    print("Ilość kanałów: ", dzwiek.getnchannels()) #1 kanał - mono , 2 kanały - stereo
    print("Ilość próbek:", sample)
    print("Długość pliku audio:", round(dlugosc, 2), "sekuny")
    print("Data type:", dzwiek2.dtype)
    czzas = np.linspace(0, len(plik) / rate, num=len(plik))
    plt.plot(czzas,plik)
    plt.title("Wizualizacja sygnału")
    plt.xlabel('Czas (s)')
    plt.ylabel('Amplituda')
    return plt.show()

# wykres mocy w decybelach
def spektra(Fs, dzwiek2):
    a, b = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

#Reprezentacje widma
    b[0, 0].set_title("Wielkość widma")
    b[0, 0].magnitude_spectrum(dzwiek2, Fs=Fs,color='C4')
    b[1, 0].set_title("Log. Wielkość (dB)")
    b[1, 0].magnitude_spectrum(dzwiek2, Fs=Fs, scale='dB', color='C4')
    b[1, 1].set_title("Widmo fazowe")
    b[1, 1].phase_spectrum(dzwiek2, Fs=Fs)
    b[2, 0].set_title("Widmo kątowe")
    b[2, 0].angle_spectrum(dzwiek2, Fs=Fs)
    b[0, 1].remove()
    b[2, 1].remove()
    a.tight_layout()
    return plt.show()
#drugi spektrometr
def drugi_spekt(rate,dzwiek2):
    spektr, czestotliwosc, czas, spe = plt.specgram(dzwiek2, Fs=rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    db = plt.colorbar(spe)  # utowrzenie paska pokazującego intensywność dB
    plt.title("Spektogram")
    plt.xlabel("Czas (s)")
    plt.ylabel("Częstotliwość (hz)")
    db.set_label("Intensywność (dB)")
    plt.ylim(0, 10000)
    return plt.show()
#obliczanie FFT
def fourier(rate,dzwiek2):
    fft = scipy.fft.fft(dzwiek2)
    return fft;
if __name__=='__main__':
    nazwa = "am.wav"
    rate, dzwiek2 = wavfile.read(nazwa) #wczytywanie pliku .wav

    spect(rate,dzwiek2)
    drugi_spekt(rate,dzwiek2)
    sygnal(rate,dzwiek2,nazwa)
    spektra(rate, dzwiek2)
    print("")
    print("FFT sygnału: ",fourier(rate,dzwiek2))
    print("")





















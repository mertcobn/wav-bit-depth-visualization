import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

frequency = 1
duration = 1
samplerate = 44100


time = np.linspace(0, duration, int(samplerate * duration))
sine = np.sin(2 * np.pi * frequency * time)


bits = ['PCM_U8', 'PCM_16', 'PCM_24', 'PCM_32']

for bit_depth in bits:
    sf.write(f'{bit_depth}.wav', sine, samplerate, subtype=bit_depth)

data_8bit, samplerate = sf.read('PCM_U8.wav')
data_16bit, samplerate = sf.read('PCM_16.wav')
data_24bit, samplerate = sf.read('PCM_24.wav')
data_32bit, samplerate = sf.read('PCM_32.wav')


plt.figure(figsize=(10, 12))

# 8-bit and 16-bit PCM
plt.subplot(2, 2, 1)
plt.plot(time, data_8bit, color='red')
plt.title('8-bit PCM')
plt.xlabel('time (s)')
plt.ylabel('Genlik')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(time, data_16bit, color='blue')
plt.title('16-bit PCM')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# 24-bit and 32-bit PCM
plt.subplot(2, 2, 3)
plt.plot(time, data_24bit, color='green')
plt.title('24-bit PCM')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(time, data_32bit, color='orange')
plt.title('32-bit PCM')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
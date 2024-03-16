# Visualizing WAV Audio Files

This Python code generates and visualizes audio files in WAV format with different bit depths (8-bit, 16-bit, 24-bit, and 32-bit).

The code utilizes the `numpy`, `matplotlib.pyplot`, and `soundfile` libraries.

## How to Use

1. Run the code to generate audio files in WAV format with different bit depths.
2. Visualize the generated audio files.

## Code Description

- Variables `frequency`, `duration`, and `samplerate` specify the properties of the signal to be generated.
- The `time` variable is used to create the time series.
- The `sine` variable represents the sinusoidal waveform.
- The `bits` list specifies different bit depths.
- Using a loop, separate audio files are created for each bit depth.
- Audio files are read using the `sf.read()` function.
- The `matplotlib.pyplot` library is used to visualize the audio files.

## Visualization

The code visualizes the generated audio files in a 2x2 grid format. Each subplot represents an audio file, with time plotted against amplitude values.

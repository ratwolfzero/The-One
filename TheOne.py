import numpy as np
import matplotlib.pyplot as plt

def generate_wave(frequency=1, samples=100, amplitude=1):
    # Generate a simple sine wave
    x = np.linspace(0, 2 * np.pi, samples)  # Normally represents time
    y = amplitude * np.sin(frequency * x)
    return y

def plot_wave_as_events(wave_data):
    # Plot a waveform using event indices instead of time
    event_indices = range(len(wave_data))  # Use sequential event indices
    amplitude_changes = np.diff(wave_data, prepend=wave_data[0])  # Capture changes

    plt.figure(figsize=(10, 5))

    # Plot original wave with event indices
    plt.subplot(1, 2, 1)
    plt.plot(event_indices, wave_data, label="Amplitude", color="blue")
    plt.title("Waveform as Event Sequence")
    plt.xlabel("Event Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    # Plot only state changes (emergent feature)
    plt.subplot(1, 2, 2)
    plt.stem(event_indices, amplitude_changes, linefmt="orange", markerfmt="o", basefmt="gray")
    plt.title("Amplitude Changes (Emergent Events)")
    plt.xlabel("Event Index")
    plt.ylabel("Change in Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Generate a sine wave
wave = generate_wave(frequency=1, samples=100, amplitude=1)

# Plot it without using time
plot_wave_as_events(wave)


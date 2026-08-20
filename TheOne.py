import numpy as np
import matplotlib.pyplot as plt

def generate_wave(custom_function, samples=100, x_range=(-1, 1)):
    """
    Generate a wave based on a user-defined function.
 
    Args:
        custom_function (callable): A function to generate the wave. Takes an array of x values as input.
        samples (int): Number of points to generate.
        x_range (tuple): Range of x values (start, end).

    Returns:
        np.ndarray: Generated wave values.
    """
    x = np.linspace(x_range[0], x_range[1], samples)  # Generate x values
    y = custom_function(x)  # Apply the custom function
    return y

def plot_wave_as_events(wave_data):
    """
    Plot a waveform four ways: the raw sequence, its local rate of change,
    its frequency spectrum, and a genuinely emergent modulation spectrum.

    These panels get progressively less "local," which can look like a
    march toward emergence. It isn't, and the fourth panel exists to draw
    the real line:

    - LOCAL: the diff panel. y[i] - y[i-1] touches a 2-sample window and is
      exactly invertible via cumsum. No new information, just the same
      signal re-expressed.
    - GLOBAL, but still NOT emergent: the FFT panel. Each bin is a weighted
      SUM over every sample (X[k] = sum_n x[n] * e^{-2pi*i*k*n/N}), so it
      needs the whole signal to compute -- but summation is linear. Every
      term in that sum is independently computable; nothing here requires
      the samples to interact. "Needs the whole to compute" is a weaker
      claim than "the whole exceeds the sum of its parts."
    - ACTUALLY EMERGENT: the modulation panel. The wave is multiplied (not
      added) by a carrier tone. Multiplication in time is convolution in
      frequency, and it creates energy at sum/difference frequencies that
      exist in NEITHER the wave's spectrum nor the carrier's spectrum
      alone. That new content can't be decomposed into independent
      per-sample contributions -- it only exists because the two signals
      interacted. This is the one panel that actually earns "the whole is
      more than the sum of the parts."

    Args:
        wave_data (np.ndarray): The wave values to plot.
    """
    n = np.arange(len(wave_data))
    event_indices = range(len(wave_data))  # Use sequential event indices
    amplitude_changes = np.diff(wave_data, prepend=wave_data[0])  # Local: 2-sample window

    # FFT: global (needs every sample) but still linear -- see docstring
    spectrum = np.fft.rfft(wave_data)
    freqs = np.fft.rfftfreq(len(wave_data), d=1.0)  # cycles per sample
    magnitude = np.abs(spectrum)

    # Modulation: multiply by a carrier at a quarter of the Nyquist rate.
    # Sum/difference sidebands appear here that are in neither input's
    # spectrum -- genuine emergence, not just a big sum.
    carrier_cycles = max(1, len(wave_data) // 4)
    carrier = np.cos(2 * np.pi * carrier_cycles * n / len(wave_data))
    modulated = wave_data * carrier
    modulated_spectrum = np.abs(np.fft.rfft(modulated))

    plt.figure(figsize=(20, 5))

    # Plot original wave with event indices
    plt.subplot(1, 4, 1)
    plt.plot(event_indices, wave_data, label="Amplitude", color="blue")
    plt.title("Waveform as Event Sequence")
    plt.xlabel("Event Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    # Plot only state changes (local -- not emergent, see docstring)
    plt.subplot(1, 4, 2)
    plt.stem(event_indices, amplitude_changes, linefmt="orange", markerfmt="o", basefmt="gray")
    plt.title("Amplitude Changes (Local)")
    plt.xlabel("Event Index")
    plt.ylabel("Change in Amplitude")
    plt.grid(True)

    # Plot the frequency spectrum (global, but linear -- not emergent, see docstring)
    plt.subplot(1, 4, 3)
    plt.stem(freqs, magnitude, linefmt="green", markerfmt="o", basefmt="gray")
    plt.title("Frequency Spectrum (Global)")
    plt.xlabel("Frequency (cycles/sample)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    # Plot the modulated spectrum (genuinely emergent -- see docstring)
    plt.subplot(1, 4, 4)
    plt.stem(freqs, modulated_spectrum, linefmt="red", markerfmt="o", basefmt="gray")
    plt.title("Modulated Spectrum (Emergent)")
    plt.xlabel("Frequency (cycles/sample)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to coordinate wave generation and plotting.
    """
    # Define user-selectable functions
    def sine_wave(x):
        return np.sin(2 * np.pi * x)

    def parabola(x):
        return x**2

    def cubic(x):
        return x**3

    def cosine_wave(x):
        return np.cos(2 * np.pi * x)

    def tangent_wave(x):
        return np.tan(2 * np.pi * x) / 10

    def exponential(x):
        return np.exp(x)

    def logarithmic(x):
        return np.log(x + 1.1)

    def square_wave(x):
        return np.sign(np.sin(2 * np.pi * x))

    def sawtooth_wave(x):
        return 2 * (x - np.floor(x + 0.5))

    def quartic(x):
        return x**4 - x**2

    def noisy_sine_wave(x):
        return np.sin(2 * np.pi * x) + 0.2 * np.random.randn(len(x))

    def hybrid_sin_exp(x):
        return np.sin(2 * np.pi * x) * np.exp(-x)

    def piecewise_function(x):
        return np.where(x < 0, x**2, np.sin(2 * np.pi * x))

    # Map choices to functions
    functions = {
        "1": ("Sine Wave", sine_wave),
        "2": ("Parabola", parabola),
        "3": ("Cubic", cubic),
        "4": ("Cosine Wave", cosine_wave),
        "5": ("Tangent Wave", tangent_wave),
        "6": ("Exponential", exponential),
        "7": ("Logarithmic", logarithmic),
        "8": ("Square Wave", square_wave),
        "9": ("Sawtooth Wave", sawtooth_wave),
        "10": ("Quartic", quartic),
        "11": ("Noisy Sine Wave", noisy_sine_wave),
        "12": ("Hybrid Sin-Exp", hybrid_sin_exp),
        "13": ("Piecewise Function", piecewise_function)
    }

    # Display options to the user
    print("Choose a function to experiment:")
    for key, (name, _) in functions.items():
        print(f"{key}: {name}")

    # Get user input
    choice = input("Enter your choice (1-13): ").strip()
    chosen_function = functions.get(choice, ("Sine Wave", sine_wave))[1]

    # Generate and plot the wave
    wave = generate_wave(custom_function=chosen_function, samples=100, x_range=(-1, 1))
    plot_wave_as_events(wave)

if __name__ == "__main__":
    main()


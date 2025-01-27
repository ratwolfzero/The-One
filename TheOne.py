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
    Plot a waveform using event indices and show amplitude changes.

    Args:
        wave_data (np.ndarray): The wave values to plot.
    """
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

# Example usage with user-defined functions
if __name__ == "__main__":
    # Define a function (e.g., sine wave, parabola, cubic, etc.)
    def sine_wave(x):
        return np.sin(2 * np.pi * x)

    def parabola(x):
        return x**2

    def cubic(x):
        return x**3

    # Choose a function to experiment with
    print("Choose a function to experiment:")
    print("1: Sine Wave")
    print("2: Parabola")
    print("3: Cubic")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        chosen_function = sine_wave
    elif choice == "2":
        chosen_function = parabola
    elif choice == "3":
        chosen_function = cubic
    else:
        print("Invalid choice. Defaulting to sine wave.")
        chosen_function = sine_wave

    # Generate and plot the wave
    wave = generate_wave(custom_function=chosen_function, samples=100, x_range=(-1, 1))
    plot_wave_as_events(wave)
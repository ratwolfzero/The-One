# The One

## The Whole is More Than the Sum of the Parts

## Dor

"Time, he learned, was not to be measured in hours or minutes, or even seconds. Time was measured in moments. The time keeper didn’t just count the seconds, he understood their significance, how each moment could shape a life, a destiny."

"the true beauty of time lies in its impermanence"

Albom, Mitch. The Time Keeper. New York: Hyperion, 2012.

---

A wave generator/visualizer that doubles as a demo of three different senses in which "the whole" can relate to "the parts" — local, global, and genuinely emergent — plotted side by side instead of just asserted.

## Usage

Requires `numpy` and `matplotlib`.

```bash
python3 TheOne.py
```

Pick a function (1–13) at the prompt. A four-panel plot opens.

## The four panels

**1. Waveform as Event Sequence** — the raw signal, indexed by sample.

**2. Amplitude Changes (Local)** — the discrete derivative. Depends on only two neighboring samples and is fully invertible via cumulative sum, so it's a re-expression of the wave, not new information.

$$y[i] - y[i-1]$$

**3. Frequency Spectrum (Global)** — magnitude of the discrete Fourier transform. Every bin needs every sample, but the DFT is linear — each term is independently computable — so "needs the whole signal" still isn't emergence.

$$X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-i 2\pi k n / N}$$

**4. Modulated Spectrum (Emergent)** — the wave multiplied by a fixed carrier tone at half the Nyquist frequency (a quarter of the sampling rate). Multiplication is a genuine interaction between the two signals: it produces sum/difference frequencies that exist in neither input's own spectrum. For a wave at one frequency and a carrier at another:

$$\sin(2\pi f_0 n)\cos(2\pi f_c n) = \frac{1}{2}\sin\big(2\pi (f_0+f_c) n\big) + \frac{1}{2}\sin\big(2\pi (f_0-f_c) n\big)$$

## Takeaway

- **Local** — needs a couple of neighbors.
- **Global** — needs every sample, but only as an additive sum. Still decomposable, still not emergent.
- **Emergent** — needs two things multiplied together. The result contains structure that belongs to neither part alone.

![The One Image](TheOne1.png)
![The One Image](TheOne2.png)
![The One Image](TheOne3.png)

import numpy as np


def compute_fft_spectrum(signal: np.ndarray, sample_rate: float) -> tuple[np.ndarray, np.ndarray]:
    """Computes the 1D Discrete Fourier Transform and corresponding positive frequencies.
    
    Parameters:
        signal: 1D input signal array.
        sample_rate: Sampling frequency in Hz.
        
    Returns:
        tuple containing (positive_frequencies, magnitude_spectrum)
    """
    n = signal.size
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(n, d=1.0 / sample_rate)
    
    # Extract non-negative frequency components
    positive_mask = frequencies >= 0
    pos_freqs = frequencies[positive_mask]
    magnitude = np.abs(fft_result[positive_mask]) / n
    
    return pos_freqs, magnitude


def compute_pairwise_distances(coords_a: np.ndarray, coords_b: np.ndarray) -> np.ndarray:
    """Computes Euclidean distance matrix between two sets of N-dimensional points using broadcasting.
    
    Parameters:
        coords_a: Array of shape (M, D)
        coords_b: Array of shape (N, D)
        
    Returns:
        Distance matrix of shape (M, N)
    """
    # Vectorized computation: ||a - b||^2 = sum((a - b)^2)
    diff = coords_a[:, np.newaxis, :] - coords_b[np.newaxis, :, :]
    return np.sqrt(np.sum(diff**2, axis=-1))


def apply_2d_moving_average(matrix: np.ndarray, window_size: int = 3) -> np.ndarray:
    """Applies a uniform moving average filter to a 2D array via convolution.
    
    Parameters:
        matrix: 2D input array.
        window_size: Odd integer size of the smoothing window.
        
    Returns:
        Smoothed 2D array of the same shape.
    """
    kernel = np.ones((window_size, window_size), dtype=np.float64) / (window_size**2)
    
    # Zero-pad borders to preserve input dimensions
    pad_width = window_size // 2
    padded = np.pad(matrix, pad_width=pad_width, mode='edge')
    
    # 2D correlation/convolution using stride tricks or scipy equivalent pattern
    sub_matrices = np.lib.stride_tricks.sliding_window_view(padded, (window_size, window_size))
    return np.einsum('ij,klij->kl', kernel, sub_matrices)


# Demonstration
if __name__ == "__main__":
    np.random.seed(42)
    
    # 1. FFT Example
    fs = 1000  # 1 kHz sampling rate
    t = np.linspace(0, 1, fs, endpoint=False)
    clean_signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    freqs, mag = compute_fft_spectrum(clean_signal, sample_rate=fs)
    print(f"Top 2 dominant frequencies detected: {freqs[np.argsort(mag)[-2:]]} Hz")
    
    # 2. Distance Matrix Example
    pts_a = np.random.rand(5, 2)
    pts_b = np.random.rand(3, 2)
    dist_matrix = compute_pairwise_distances(pts_a, pts_b)
    print(f"Pairwise Distance Matrix Shape: {dist_matrix.shape}")
    
    # 3. 2D Moving Average Example
    grid = np.random.rand(6, 6)
    smoothed = apply_2d_moving_average(grid, window_size=3)
    print(f"Smoothed Output Shape: {smoothed.shape}")

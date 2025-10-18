import numpy as np
from scipy.signal import detrend, get_window

def psd2d(field, window="hann"):
    f = detrend(field, axis=0, type="linear")
    f = detrend(f, axis=1, type="linear")
    w = get_window(window, f.shape[0])[:, None] * get_window(window, f.shape[1])[None, :]
    F = np.fft.fftshift(np.fft.fft2(f * w))
    psd = (F * F.conj()).real
    psd /= psd.max() + 1e-9
    return psd

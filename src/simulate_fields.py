import numpy as np, yaml
from pathlib import Path

def pink_noise(shape, rng):
    nx, ny = shape
    kx, ky = np.fft.fftfreq(nx), np.fft.fftfreq(ny)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    k = np.hypot(KX, KY); k[0, 0] = 1e-6
    phase = np.exp(1j * 2*np.pi * rng.random((nx, ny)))
    spectrum = phase / k  # ~ 1/f
    field = np.fft.ifft2(spectrum).real
    return (field - field.mean()) / (field.std() + 1e-9)

def gaussian_blobs(shape, rng, count=5, sigma=3.0):
    nx, ny = shape
    x = np.arange(nx)[:, None]; y = np.arange(ny)[None, :]
    out = np.zeros((nx, ny))
    for _ in range(count):
        cx, cy = rng.integers(0, nx), rng.integers(0, ny)
        amp = rng.uniform(0.5, 1.0)
        out += amp * np.exp(-((x-cx)**2 + (y-cy)**2) / (2*sigma**2))
    return (out - out.mean()) / (out.std() + 1e-9)

def line_wave(shape, rng, freq=0.07):
    nx, ny = shape
    x = np.arange(nx)[:, None]; y = np.arange(ny)[None, :]
    theta = rng.uniform(0, np.pi)
    u, v = np.cos(theta), np.sin(theta)
    wave = np.sin(2*np.pi*freq * (u*x + v*y))
    return (wave - wave.mean()) / (wave.std() + 1e-9)

def build_field(cfg):
    rng = np.random.default_rng(cfg.get("seed", 42))
    nx, ny = cfg["grid"]["nx"], cfg["grid"]["ny"]
    field = np.zeros((nx, ny))
    for comp in cfg["fields"]["components"]:
        t, w = comp["type"], comp["weight"]
        if t == "pink_noise":
            field += w * pink_noise((nx, ny), rng)
        elif t == "gaussian_blobs":
            field += w * gaussian_blobs((nx, ny), rng, comp.get("count", 5), comp.get("sigma", 3.0))
        elif t == "line_wave":
            field += w * line_wave((nx, ny), rng, comp.get("freq", 0.07))
    return field

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(open(args.config))
    field = build_field(cfg)

    out = Path(cfg["save"]["out_dir"])
    out.mkdir(parents=True, exist_ok=True)
    np.save(out / "field.npy", field)

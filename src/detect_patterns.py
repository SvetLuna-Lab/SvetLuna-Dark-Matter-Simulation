import numpy as np, yaml
from pathlib import Path
from sklearn.neighbors import LocalOutlierFactor
from .spectral_tools import psd2d

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(open(args.config))
    out = Path(cfg["save"]["out_dir"]); out.mkdir(parents=True, exist_ok=True)

    field = np.load(out / "field.npy")
    psd = psd2d(field, cfg["spectral"]["window"])

    # radial profile of PSD
    nx, ny = psd.shape
    cx, cy = nx // 2, ny // 2
    R = np.hypot(*np.meshgrid(np.arange(nx)-cx, np.arange(ny)-cy, indexing="ij")).astype(int)
    radial = np.array([psd[R == k].mean() for k in range(R.max()+1)])

    X = radial.reshape(-1, 1)
    lof = LocalOutlierFactor(n_neighbors=20, contamination=cfg["detection"]["contamination"])
    scores = -lof.fit_predict(X)  # 2→anom, 1→ok (индикативно)

    np.save(out / "psd.npy", psd)
    np.save(out / "radial.npy", radial)
    np.save(out / "scores.npy", scores)

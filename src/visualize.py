import numpy as np, yaml
from pathlib import Path
import matplotlib.pyplot as plt

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(open(args.config))
    out = Path(cfg["save"]["out_dir"]); (out / "figures").mkdir(parents=True, exist_ok=True)

    field  = np.load(out / "field.npy")
    psd    = np.load(out / "psd.npy")
    radial = np.load(out / "radial.npy")
    scores = np.load(out / "scores.npy")

    plt.figure(); plt.imshow(field, origin="lower"); plt.title("Synthetic Field"); plt.colorbar(); plt.tight_layout()
    plt.savefig(out / "figures" / "field.png", dpi=200)

    plt.figure(); plt.imshow(psd, origin="lower"); plt.title("2D PSD (normalized)"); plt.colorbar(); plt.tight_layout()
    plt.savefig(out / "figures" / "psd.png", dpi=200)

    plt.figure(); plt.plot(radial); plt.title("Radial Spectrum"); plt.tight_layout()
    plt.savefig(out / "figures" / "radial.png", dpi=200)

    plt.figure(); plt.plot(scores); plt.title("Anomaly Scores (LOF)"); plt.tight_layout()
    plt.savefig(out / "figures" / "scores.png", dpi=200)

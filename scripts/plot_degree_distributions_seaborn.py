"""Versão mínima: lê `data/processed/performance_metrics.json`, transforma
`degree_distribution` em arrays x,y e plota sem prints.
"""

import json
import os
import sys
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # use per-figure style for the 'sentence' plot via context
    input_path = os.path.join("data", "processed", "performance_metrics.json")
    outdir = os.path.join("output", "degree_plots_simple")
    os.makedirs(outdir, exist_ok=True)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        sys.exit(1)

    plotted = 0
    for name, metrics in data.items():
        dist = metrics.get("degree_distribution")
        if not dist:
            continue

        items = sorted(((int(k), int(v)) for k, v in dist.items()), key=lambda x: x[0])
        degrees = [d for d, _ in items]

        # preencher graus ausentes entre 0 e max(degrees)
        max_deg = max(degrees) if degrees else 0
        full_degrees = list(range(0, max_deg + 1))
        counts_map = {d: c for d, c in items}
        counts_filled = [int(counts_map.get(d, 0)) for d in full_degrees]

        x = np.arange(len(full_degrees))
        y = np.array(counts_filled, dtype=float)

        with plt.style.context("dark_background"):
            fig, ax = plt.subplots(figsize=(10, 4))

        ax.plot(x, y, color="C2", linestyle="-")
        ax.set_title(name)
        # forçar eixos a começar em 0
        ax.set_xlim(left=0)
        ax.set_ylim(bottom=0)

        # x ticks: mostrar apenas a cada 5 graus
        x_tick_pos = [i for i, d in enumerate(full_degrees) if d % 5 == 0]
        if not x_tick_pos:
            x_tick_pos = [0]
        ax.set_xticks(x_tick_pos)
        ax.set_xticklabels(
            [str(full_degrees[i]) for i in x_tick_pos], rotation=45, ha="right"
        )

        # y ticks de 5 em 5
        max_y = int(y.max() if y.size else 0)
        y_ticks = (
            list(range(0, max_y + 5, 5))
            if max_y >= 5
            else [0, max_y] if max_y > 0 else [0]
        )
        ax.set_yticks(y_ticks)

        ax.set_xlabel("degree")
        ax.set_ylabel("count")
        plt.tight_layout()
        out_file = os.path.join(outdir, f"{name}_degree_distribution.png")
        fig.savefig(out_file)
        plt.close(fig)
        plotted += 1

    if plotted == 0:
        sys.exit(0)


if __name__ == "__main__":
    main()

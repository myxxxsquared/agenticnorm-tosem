from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

cur_path = Path(__file__).parent

mpl.rcParams["font.family"] = "Linux Libertine"

rounds = list(range(10))

data = {
    "Round 1": [
        0.608,
        0.608,
        0.608,
        0.784,
        0.784,
        0.758,
        0.856,
        0.856,
        0.856,
        0.856,
    ],
    "Round 2": [
        0.526,
        0.608,
        0.608,
        0.608,
        0.830,
        0.856,
        0.856,
        0.856,
        0.856,
        0.856,
    ],
    "Round 3": [
        0.608,
        0.737,
        0.722,
        0.809,
        0.830,
        0.856,
        0.856,
        0.856,
        0.856,
        0.856,
    ],
}

styles = [
    {"color": "C0", "linestyle": "-", "marker": "."},
    {"color": "C1", "linestyle": "-", "marker": "."},
    {"color": "C2", "linestyle": "-", "marker": "."},
    {"color": "C1", "linestyle": "--", "marker": "+"},
    {"color": "C2", "linestyle": "-.", "marker": "x"},
    {"color": "C3", "linestyle": ":", "marker": "*"},
]

fig = plt.figure(figsize=(3, 2.5))
ax = fig.add_subplot(111)

for (model, recalls), s in zip(data.items(), styles):
    ax.plot(rounds, recalls, label=model, **s)

ax.set_xlabel("Rounds")
ax.set_ylabel("Recall")
ax.grid()

ax.legend(fontsize=6)

plt.tight_layout()
plt.savefig(cur_path / "rounds.pdf", bbox_inches="tight")
plt.close(fig)

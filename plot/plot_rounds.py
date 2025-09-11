from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

cur_path = Path(__file__).parent

mpl.rcParams["font.family"] = "Linux Libertine"

rounds = list(range(10))

data = {
    "DeepSeek v3": [
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
    "Gemma 3 4B": [
        0.608,
        0.799,
        0.856,
        0.799,
        0.856,
        0.856,
        0.856,
        0.856,
        0.856,
        0.856,
    ],
    "GPT-OSS 20B": [
        0.526,
        0.608,
        0.722,
        0.809,
        0.809,
        0.835,
        0.835,
        0.835,
        0.835,
        0.835,
    ],
    "GPT-OSS 120B": [
        0.598,
        0.737,
        0.809,
        0.809,
        0.809,
        0.830,
        0.830,
        0.830,
        0.830,
        0.830,
    ],
}

styles = [
    {"color": "C0", "linestyle": "-", "marker": "."},
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

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

cur_path = Path(__file__).parent

mpl.rcParams["font.family"] = "Linux Libertine"

rounds = list(range(10))

data = {
    "TrainTicket": [370, 1057, 1060, 2228, 2316, 2382, 2534, 2987, 2987, 3121],
    "NiceFish": [370, 647, 1320, 1925, 1345, 1598, 2141, 1504, 1322, 1626],
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
ax.set_ylabel("Number of Prompt Tokens")
ax.grid()

ax.legend(fontsize=6)

plt.tight_layout()
plt.savefig(cur_path / "number_of_tokens.pdf", bbox_inches="tight")
plt.close(fig)

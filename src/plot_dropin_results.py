import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/dropin_results.csv")

plt.figure(figsize=(8, 5))

plt.plot(
    df["dropin_probability"],
    df["average_log10_lr"],
    marker="o"
)

plt.xlabel("Drop-in probability")
plt.ylabel("Average log10(LR)")
plt.title("Effect of allele drop-in on DNA evidence strength")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "reports/dropin_experiment.png",
    dpi=300
)

print("Plot saved.")
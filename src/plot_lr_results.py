import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/lr_results.csv")

plt.figure(figsize=(8, 5))

plt.plot(
    df["dropout_probability"],
    df["average_log10_lr"],
    marker="o"
)

plt.xlabel("Dropout probability")
plt.ylabel("Average log10(LR)")
plt.title("Effect of allele dropout on likelihood ratio")
plt.grid(True)

plt.tight_layout()
plt.savefig("reports/lr_experiment.png", dpi=300)
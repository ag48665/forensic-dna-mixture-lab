import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/contributors_results.csv")

plt.figure(figsize=(8,5))

plt.plot(
    df["contributors"],
    df["false_exclusion_rate"],
    marker="o"
)

plt.xlabel("Number of contributors")
plt.ylabel("False exclusion rate")
plt.title("Effect of contributor number on false exclusion")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "reports/contributors_experiment.png",
    dpi=300
)

print("Plot saved.")
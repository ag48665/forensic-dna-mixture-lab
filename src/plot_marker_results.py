import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/marker_results.csv")

plt.figure(figsize=(8, 5))
plt.plot(
    df["number_of_markers"],
    df["false_exclusion_rate"],
    marker="o"
)

plt.xlabel("Number of STR markers")
plt.ylabel("False exclusion rate")
plt.title("Effect of marker count on false exclusions")
plt.grid(True)

plt.savefig("reports/marker_experiment.png")
plt.show()
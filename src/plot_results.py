import matplotlib.pyplot as plt

dropout = [0.00, 0.05, 0.10, 0.20, 0.30]
false_exclusion = [0.000, 0.342, 0.523, 0.773, 0.910]

plt.figure(figsize=(8,5))
plt.plot(dropout, false_exclusion, marker="o")

plt.xlabel("Dropout probability")
plt.ylabel("False exclusion rate")
plt.title("Impact of allele dropout on false exclusions")

plt.grid(True)

plt.savefig("reports/dropout_experiment.png")
plt.show()
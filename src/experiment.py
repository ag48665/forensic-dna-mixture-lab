import pandas as pd

from simulator import (
    generate_profile,
    create_mixture,
    apply_dropout,
    load_allele_frequencies
)
from likelihood import can_be_excluded


frequencies = load_allele_frequencies()
results = []

for p in [0.0, 0.05, 0.10, 0.20, 0.30]:

    false_exclusions = 0

    for _ in range(1000):
        person1 = generate_profile(frequencies)
        person2 = generate_profile(frequencies)

        mixture = create_mixture(person1, person2)
        mixture_dropout = apply_dropout(mixture, probability=p)

        if can_be_excluded(person1, mixture_dropout):
            false_exclusions += 1

    rate = false_exclusions / 1000

    results.append({
        "dropout_probability": p,
        "false_exclusion_rate": rate
    })

    print(f"Dropout={p:.2f}  False exclusion={rate:.3f}")

df = pd.DataFrame(results)
df.to_csv("reports/dropout_results.csv", index=False)
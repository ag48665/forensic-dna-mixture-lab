import math
import pandas as pd

from simulator import (
    generate_profile,
    create_mixture,
    apply_dropout,
    apply_dropin,
    load_allele_frequencies
)

from likelihood import frequency_based_lr


frequencies = load_allele_frequencies()
results = []

for p in [0.0, 0.05, 0.10, 0.20, 0.30]:

    log_lr_values = []

    for _ in range(1000):

        person1 = generate_profile(frequencies)
        person2 = generate_profile(frequencies)

        mixture = create_mixture(person1, person2)

        mixture_dropout = apply_dropout(
            mixture,
            probability=0.10
        )

        mixture_dropin = apply_dropin(
            mixture_dropout,
            frequencies,
            probability=p
        )

        lr = frequency_based_lr(
            person1,
            mixture_dropin,
            frequencies
        )

        log_lr_values.append(math.log10(lr))

    average_log_lr = sum(log_lr_values) / len(log_lr_values)

    results.append({
        "dropin_probability": p,
        "average_log10_lr": average_log_lr
    })

    print(
        f"Drop-in={p:.2f}  Average log10(LR)={average_log_lr:.3f}"
    )

df = pd.DataFrame(results)
df.to_csv("reports/dropin_results.csv", index=False)
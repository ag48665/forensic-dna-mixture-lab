from simulator import (
    load_allele_frequencies,
    generate_profile,
    apply_dropout
)

from likelihood import can_be_excluded


def create_multi_mixture(profiles):

    mixture = {}

    for marker in profiles[0]:

        alleles = set()

        for profile in profiles:
            alleles.update(profile[marker])

        mixture[marker] = sorted(alleles)

    return mixture


frequencies = load_allele_frequencies()

for contributors in [2, 3, 4]:

    false_exclusions = 0
    N = 1000

    for _ in range(N):

        profiles = [
            generate_profile(frequencies)
            for _ in range(contributors)
        ]

        mixture = create_multi_mixture(profiles)

        mixture_dropout = apply_dropout(
            mixture,
            probability=0.2
        )

        suspect = profiles[0]

        if can_be_excluded(
            suspect,
            mixture_dropout
        ):
            false_exclusions += 1

    rate = false_exclusions / N

import pandas as pd

results = []

for contributors in [2, 3, 4]:

    false_exclusions = 0
    N = 1000

    for _ in range(N):

        profiles = [
            generate_profile(frequencies)
            for _ in range(contributors)
        ]

        mixture = create_multi_mixture(profiles)

        mixture_dropout = apply_dropout(
            mixture,
            probability=0.2
        )

        suspect = profiles[0]

        if can_be_excluded(
            suspect,
            mixture_dropout
        ):
            false_exclusions += 1

    rate = false_exclusions / N

    results.append({
        "contributors": contributors,
        "false_exclusion_rate": rate
    })

    print(
        f"Contributors={contributors} "
        f"False exclusion={rate:.3f}"
    )

pd.DataFrame(results).to_csv(
    "reports/contributors_results.csv",
    index=False
)


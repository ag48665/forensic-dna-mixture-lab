from simulator import (
    generate_profile,
    create_mixture,
    apply_dropout,
    load_allele_frequencies
)
from likelihood import can_be_excluded

frequencies = load_allele_frequencies()

for markers_to_use in [1, 2, 3, 4]:

    false_exclusions = 0

    selected_markers = list(frequencies.keys())[:markers_to_use]

    reduced_freqs = {
        marker: frequencies[marker]
        for marker in selected_markers
    }

    for _ in range(1000):

        person1 = generate_profile(reduced_freqs)
        person2 = generate_profile(reduced_freqs)

        mixture = create_mixture(person1, person2)

        mixture_dropout = apply_dropout(
            mixture,
            probability=0.10
        )

        if can_be_excluded(person1, mixture_dropout):
            false_exclusions += 1

    rate = false_exclusions / 1000

    print(
        f"Markers={markers_to_use}  False exclusion={rate:.3f}"
    )
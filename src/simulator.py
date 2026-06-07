import random
from collections import defaultdict

import pandas as pd

from likelihood import can_be_excluded, simple_lr, frequency_based_lr


STR_MARKERS = {
    "D3S1358": [12, 13, 14, 15, 16, 17, 18],
    "vWA": [14, 15, 16, 17, 18, 19, 20, 21],
    "FGA": [18, 19, 20, 21, 22, 23, 24, 25, 26],
    "TH01": [6, 7, 8, 9, 10],
    "D8S1179": [10, 11, 12, 13, 14, 15],
    "D21S11": [27, 28, 29, 30, 31, 32],
}


def load_allele_frequencies(path="data/allele_frequencies.csv"):
    df = pd.read_csv(path)

    frequencies = {}

    for marker in df["marker"].unique():

        subset = df[df["marker"] == marker]

        frequencies[marker] = {
            int(row["allele"]): float(row["frequency"])
            for _, row in subset.iterrows()
        }

    return frequencies


def generate_profile(frequencies=None):

    profile = {}

    if frequencies is None:

        for marker, alleles in STR_MARKERS.items():

            profile[marker] = sorted([
                random.choice(alleles),
                random.choice(alleles)
            ])

    else:

        for marker, allele_freqs in frequencies.items():

            alleles = list(allele_freqs.keys())
            weights = list(allele_freqs.values())

            profile[marker] = sorted(
                random.choices(
                    alleles,
                    weights=weights,
                    k=2
                )
            )

    return profile


def create_mixture(profile1, profile2):

    mixture = defaultdict(list)

    for marker in profile1:

        mixture[marker].extend(profile1[marker])
        mixture[marker].extend(profile2[marker])

        mixture[marker] = sorted(
            set(mixture[marker])
        )

    return dict(mixture)


def apply_dropout(profile, probability=0.2):

    dropped = {}

    for marker, alleles in profile.items():

        remaining = []

        for allele in alleles:

            if random.random() > probability:
                remaining.append(allele)

        if len(remaining) == 0:
            remaining.append(
                random.choice(alleles)
            )

        dropped[marker] = sorted(remaining)

    return dropped


if __name__ == "__main__":

    frequencies = load_allele_frequencies()

    person1 = generate_profile(frequencies)
    person2 = generate_profile(frequencies)

    mixture = create_mixture(
        person1,
        person2
    )

    mixture_dropout = apply_dropout(
        mixture,
        probability=0.2
    )

    print("\nPERSON 1")
    print(person1)

    print("\nPERSON 2")
    print(person2)

    print("\nDNA MIXTURE")
    print(mixture)

    print("\nDNA MIXTURE WITH DROPOUT")
    print(mixture_dropout)

    excluded = can_be_excluded(
        person1,
        mixture_dropout
    )

    print("\nEXCLUSION TEST")

    if excluded:
        print("Suspect excluded")
    else:
        print("Suspect cannot be excluded")

    lr = simple_lr(
        person1,
        mixture_dropout
    )

    print("\nLIKELIHOOD RATIO")
    print(f"LR = {lr:.3f}")

def genotype_probability(alleles, allele_frequencies):
    a1, a2 = alleles

    p1 = allele_frequencies.get(a1, 0.001)
    p2 = allele_frequencies.get(a2, 0.001)

    if a1 == a2:
        return p1 * p1

    return 2 * p1 * p2


def frequency_based_lr(suspect, mixture, frequencies):
    lr = 1.0

    for marker in suspect:
        suspect_alleles = suspect[marker]
        mixture_alleles = set(mixture[marker])

        if not set(suspect_alleles).issubset(mixture_alleles):
            continue

        genotype_prob = genotype_probability(
            suspect_alleles,
            frequencies[marker]
        )

        lr *= 1 / genotype_prob

    return lr

frequency_lr = frequency_based_lr(
    person1,
    mixture_dropout,
    frequencies
)

print("\nFREQUENCY-BASED LR")
print(f"LR = {frequency_lr:.3f}")



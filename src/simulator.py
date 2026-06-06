import random
from collections import defaultdict

STR_MARKERS = {
    "D3S1358": [12,13,14,15,16,17,18],
    "vWA": [14,15,16,17,18,19,20,21],
    "FGA": [18,19,20,21,22,23,24,25,26],
    "TH01": [6,7,8,9,10],
    "D8S1179": [10,11,12,13,14,15],
    "D21S11": [27,28,29,30,31,32]
}


import random
from collections import defaultdict
from likelihood import can_be_excluded


def generate_profile():
    profile = {}

    for marker, alleles in STR_MARKERS.items():
        profile[marker] = sorted([
            random.choice(alleles),
            random.choice(alleles)
        ])

    return profile


def create_mixture(profile1, profile2):

    mixture = defaultdict(list)

    for marker in STR_MARKERS:

        mixture[marker].extend(profile1[marker])
        mixture[marker].extend(profile2[marker])

        mixture[marker] = sorted(set(mixture[marker]))

    return dict(mixture)


if __name__ == "__main__":

    person1 = generate_profile()
    person2 = generate_profile()

    mixture = create_mixture(person1, person2)

    print("\nPERSON 1")
    print(person1)

    print("\nPERSON 2")
    print(person2)

    print("\nDNA MIXTURE")
    print(mixture)

excluded = can_be_excluded(person1, mixture)

print("\nEXCLUSION TEST")

if excluded:
    print("Suspect excluded")
else:
    print("Suspect cannot be excluded")
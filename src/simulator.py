import random

STR_MARKERS = {
    "D3S1358": [14, 15, 16, 17],
    "vWA": [16, 17, 18, 19],
    "FGA": [21, 22, 23, 24]
}


def generate_profile():
    profile = {}

    for marker, alleles in STR_MARKERS.items():
        a1 = random.choice(alleles)
        a2 = random.choice(alleles)

        profile[marker] = sorted([a1, a2])

    return profile


if __name__ == "__main__":
    profile = generate_profile()

    print("Generated STR profile:")
    for marker, alleles in profile.items():
        print(f"{marker}: {alleles}")
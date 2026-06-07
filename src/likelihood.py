def can_be_excluded(suspect, mixture):
    for marker in suspect:
        suspect_alleles = set(suspect[marker])
        mixture_alleles = set(mixture[marker])

        if not suspect_alleles.issubset(mixture_alleles):
            return True

    return False


def simple_lr(suspect, mixture):
    matches = 0
    total = 0

    for marker in suspect:
        total += 1

        suspect_alleles = set(suspect[marker])
        mixture_alleles = set(mixture[marker])

        if suspect_alleles.issubset(mixture_alleles):
            matches += 1

    return (matches + 1) / (total - matches + 1)

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


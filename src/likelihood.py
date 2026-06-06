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
def can_be_excluded(suspect, mixture):

    for marker in suspect:

        suspect_alleles = set(suspect[marker])
        mixture_alleles = set(mixture[marker])

        if not suspect_alleles.issubset(mixture_alleles):
            return True

    return False
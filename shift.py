def shift_ch(c, k, ab):
    try:
        i = ab.index(c)
    except ValueError:
        return c
    else:
        return ab[(i + k) % len(ab)]

def shift_str(pt, k, ab):
    return "".join([shift_ch(c, k, ab) for c in pt])

def shift_lf(lf, k):
    import frequency
    sfreqs = dict()
    for c in lf.alphabet:
        sfreqs[shift_ch(c, k, lf.alphabet)] = lf[c]
    return frequency.Language(sfreqs)

def attack_str(ct, lf):
    import frequency
    clf = frequency.measure(ct)
    maxs = 0
    candk = 0
    for k in range(len(lf.alphabet)):
        s = frequency.Language.sum(clf, shift_lf(lf, k))
        if s > maxs:
            maxs = s
            candk = k
    return candk
        

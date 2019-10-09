def _shift_ch(c, k, ab, invert=False):
    try:
        i = ab.index(k)
    except ValueError:
        return c
    else:
        import shift
        return shift._shift_ch(c, -i if invert else i, ab)
        
def _shift_str(pt, k, ab, invert=False):
    return "".join([_shift_ch(c, k[i % len(k)], ab, invert) for i, c in enumerate(pt)])

def _ioc_lf(lf):
    return sum(f ** 2 for f in lf.values())

def _ioc_str(ct, ab):
    import frequency
    f, n = frequency.count(ct, ab)
    s = 0
    for c in ab:
        o = f.get(c, 0)
        s += o * (o - 1)
    return s / (n * (n - 1)) if n > 1 else None
    
def _segment_str(ct, kn, o=0):
    return (c for i, c in enumerate(ct) if (i - o) % kn == 0)

def _ioc_str_kn(ct, ab, kn, maxo=None):
    iocs = 0
    cn = 0
    if maxo is None or maxo > kn:
        maxo = kn
    for o in range(maxo + 1):
        sstr = _segment_str(ct, kn, o)
        ioc = _ioc_str(sstr, ab)
        if ioc is not None:
            iocs += ioc
            cn += 1
    return iocs / cn if cn > 0 else None

def _attack_kn_str(ct, lf, maxkn=None, multh=0.01, minioc=0.01, mulstep=False, maxo=5):
    import frequency
    lab = frequency.alphabet(lf)
    if maxkn is None or maxkn > len(ct):
        maxkn = len(ct)
    candkn = 1
    maxioc = 0
    for kn in range(2, maxkn + 1):
        cioc = _ioc_str_kn(ct, lab, kn, maxo)
        if cioc > maxioc and cioc >= minioc:
            if kn % candkn != 0 or cioc - maxioc > multh:
                maxioc = cioc
                candkn = kn
            elif mulstep:
                maxioc = cioc
    return candkn

def _attack_shift_str(ct, kn, lf):
    import shift
    dt = [None] * len(ct)
    for ki in range(kn):
        sstr = "".join(_segment_str(ct, kn, ki))
        dsstr = shift.attackDecode(sstr, lf)
        for i, c in enumerate(dsstr):
            dt[i * kn + ki] = c
    return "".join(dt)
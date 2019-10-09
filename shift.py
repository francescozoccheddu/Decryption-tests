def _shift_ch(c, k, ab):
    try:
        i = ab.index(c)
    except ValueError:
        return c
    else:
        return ab[(i + k) % len(ab)]

def _shift_str(pt, k, ab):
    return "".join([_shift_ch(c, k, ab) for c in pt])

def _sum_lf(mf, lf, ab, k):
    s = 0
    for c in ab:
        s += mf.get(_shift_ch(c, k, ab), 0) * lf.get(c, 0)
    return s

def _attack_str(ct, lf):
    import frequency
    mf = frequency.measure(ct)
    lab = frequency.alphabet(lf)
    maxs = 0
    candk = 0
    for k in range(len(lf)):
        s = _sum_lf(mf, lf, lab, k)
        if s > maxs:
            maxs = s
            candk = k
    return candk

def encode(pt, k, ab):
    return _shift_str(pt, k, ab)

def decode(pt, k, ab):
    return _shift_str(pt, -k, ab)

def attackDecode(ct, lf):
    import frequency
    return decode(ct, _attack_str(ct, lf), frequency.alphabet(lf))
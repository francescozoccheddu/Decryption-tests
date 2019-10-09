def _shift_ch(c, k, ab):
    try:
        i = ab.index(c)
    except ValueError:
        return c
    else:
        return ab[(i + k) % len(ab)]

def _shift_str(pt, k, ab):
    return "".join([_shift_ch(c, k, ab) for c in pt])

def _sum_f(tf, lf, ab, k):
    s = 0
    for c in ab:
        s += tf.get(_shift_ch(c, k, ab), 0) * lf.get(c, 0)
    return s

def _attack_str(ct, lf):
    import frequency
    lab = frequency.alphabet(lf)
    tf = frequency.probability(ct)
    maxs = 0
    candk = 0
    for k in range(len(lf)):
        s = _sum_f(tf, lf, lab, k)
        if s > maxs:
            maxs = s
            candk = k
    return candk

# ----------------
# Public interface

def encode(pt, k, ab):
    import frequency
    return _shift_str(pt, k, frequency.alphabet(ab))

def decode(pt, k, ab):
    import frequency
    return _shift_str(pt, -k, frequency.alphabet(ab))

def attackDecode(ct, lf):
    return decode(ct, _attack_str(ct, lf), lf)
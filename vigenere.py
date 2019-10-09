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

def _ioc(lf):
    
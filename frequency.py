def load(language):
    import json
    import os
    rootpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(rootpath, "data", "frequency", f"{language}.json")
    with open(filepath, "r") as file:
        return json.load(file)

def count(t, ab=None):
    f = dict()
    n = 0
    for c in t:
        if ab is None or c in ab:
            f[c] = f.get(c, 0) + 1
            n += 1
    if ab is None:
        return f
    else:
        return f, n

def probability(t, ab=None):
    if ab is None:
        f, n = count(t), len(t)
    else:
        f, n = count(t, ab)
    return {k: f[k] / n for k in f}

def alphabet(x):
    if isinstance(x, dict):
        return list(x.keys())
    else:
        return x
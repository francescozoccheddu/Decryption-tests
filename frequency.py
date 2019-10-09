def load(language):
    import json
    import os
    rootpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(rootpath, "data", "frequency", f"{language}.json")
    with open(filepath, "r") as file:
        return json.load(file)

def measure(text):
    freqs = dict()
    for c in text:
        freqs[c] = freqs.get(c, 0) + 1
    return freqs

def alphabet(x):
    if isinstance(x, dict):
        return list(x.keys())
    else:
        return x
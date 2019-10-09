class Language:

    def __init__(self, frequencies):
        self._frequencies = frequencies
        self._alphabet = list(frequencies.keys())
        self._sqr = sum(map(lambda x : x**2, frequencies.values()))

    def __getitem__(self, key):
        return self._frequencies.get(key, 0)

    @property
    def sqr(self):
        return self._sqr

    @property
    def alphabet(self):
        return self._alphabet

    @staticmethod
    def sum(a, b):
        if len(a.alphabet) > len(b.alphabet):
            a, b = b, a
        s = 0
        for c in a.alphabet:
            s += a[c] * b[c]
        return s

def load(language):
    import json
    import os
    rootpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(rootpath, "data", "frequency", f"{language}.json")
    with open(filepath, "r") as file:
        return Language(json.load(file))

def measure(text):
    freqs = dict()
    for c in text:
        freqs[c] = freqs.get(c, 0) + 1
    return Language(freqs)
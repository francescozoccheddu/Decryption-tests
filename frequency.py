class Language:

    def __init__(self, frequencies):
        self._frequencies = frequencies
        self._sqr = sum(map(lambda x : x**2, frequencies.values()))

    def __getitem__(self, key):
        return self._frequencies.get(key) or 0
    
    def sqr(self):
        return self._sqr

def get(language):
    import json
    import os
    rootpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(rootpath, "data", "frequency", f"{language}.json")
    with open(filepath, "r") as file:
        return Language(json.load(file))


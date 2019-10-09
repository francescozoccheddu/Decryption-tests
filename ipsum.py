def load(language):
    import os
    rootpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(rootpath, "data", "ipsum", f"{language}.txt")
    with open(filepath, "r") as file:
        return file.read()
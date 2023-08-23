def loading_files(file):
    date = []
    with open(file, "r") as f:
        for idx in f:
            date.append(idx)
    return date



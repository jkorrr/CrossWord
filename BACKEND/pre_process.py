import pandas as pd

def process_data():
    df = pd.read_csv("DATASET/clues.csv")
    data = {}
    words = list(df.get("answer"))
    clues = list(df.get("question"))
    arr = list(df.get("difficulty"))

    l = len(words)
    i = 0

    while i < l:
        data[words[i]] = clues[i]
        i += 1
    return data, arr
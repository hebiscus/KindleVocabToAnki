import pandas as pd

from home.services.get_word_definition import get_word_definition


def generate_csv(data, file_path="result.csv"):
    df = pd.DataFrame(data, columns=["Word", "Context"])
    df["Definitions"] = df.apply(lambda row: get_word_definition(row["Word"]), axis=1)
    df.to_csv(file_path, index=False)

import os

import gdown
import pandas as pd


def load_data():
    os.makedirs("data", exist_ok=True)

    url = "https://drive.google.com/uc?id=1Xk2KMJSVp_JmmAD-3fYD2w8qVVBaelJJ"
    output = "data/finance_ecommerce_dirty_dataset.csv"

    gdown.download(url, output, quiet=False)

    data = pd.read_csv(output)

    print(data.head(10))


if __name__ == "__main__":
    load_data()
import os

import gdown
import pandas as pd


def load_data():
    os.makedirs("data", exist_ok=True)

    url = "https://drive.google.com/uc?id=1Xk2KMJSVp_JmmAD-3fYD2w8qVVBaelJJ"
    output = "data/finance_ecommerce_dirty_dataset.csv"

    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

    data = pd.read_csv(output)

    print(data.head(10))
    return data


def convert_types(data):
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce", format="mixed")
    data["CustomerSince"] = pd.to_datetime(data["CustomerSince"], errors="coerce", format="mixed")
    data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
    data["Balance"] = pd.to_numeric(data["Balance"], errors="coerce")
    data["MerchantPhone"] = data["MerchantPhone"].astype("string")
    data["PostalCode"] = data["PostalCode"].astype("string")
    data["Phone"] = data["Phone"].astype("string")

    return data
    

if __name__ == "__main__":
    load_data()
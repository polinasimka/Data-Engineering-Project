import pandas as pd


def convert_types(data):
    data = data.copy()

    data["Date"] = pd.to_datetime(
        data["Date"], errors="coerce", format="%m/%d/%Y"
    )
    data["CustomerSince"] = pd.to_datetime(
        data["CustomerSince"], errors="coerce", format="mixed"
    )
    data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
    data["Balance"] = pd.to_numeric(data["Balance"], errors="coerce")
    data["MerchantPhone"] = data["MerchantPhone"].astype("string")
    data["PostalCode"] = data["PostalCode"].astype("string")
    data["Phone"] = data["Phone"].astype("string")

    for col in ["Date", "CustomerSince", "Amount", "Balance"]:
        print(f"{col}: {data[col].isna().sum()} пропусков после преобразования")

    print(data.dtypes)
    data.to_parquet("data/finance_ecommerce_typed.parquet", index=False)

    return data

import os

import gdown
import pandas as pd


DATASET_URL = "https://drive.google.com/uc?id=1Xk2KMJSVp_JmmAD-3fYD2w8qVVBaelJJ"
DATA_PATH = "data/finance_ecommerce_dirty_dataset.csv"


def load_data(preview=10):
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_PATH):
        try:
            result = gdown.download(DATASET_URL, DATA_PATH, quiet=False)
            if result is None:
                raise RuntimeError("Скачивание не завершилось.")
        except Exception as error:
            raise RuntimeError(
                "Не удалось скачать датасет. "
                "Проверьте интернет и доступ к файлу на Google Drive."
            ) from error

    data = pd.read_csv(DATA_PATH)

    print(data.head(preview))
    return data
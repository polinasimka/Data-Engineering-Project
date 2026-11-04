import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_url = os.getenv("DB_URL")
db_port = os.getenv("DB_PORT")
db_root_base = os.getenv("DB_ROOT_BASE")

assert db_url

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}"
)

data = pd.read_parquet("data/finance_ecommerce_typed.parquet")
data = data.head(100)

data.to_sql(
    name="simaninapa",
    con=engine,
    if_exists="replace",
    index=False,
)

new_data = pd.read_sql_table(
    "simaninapa",
    con=engine,
)

print("Rows written:", len(new_data))

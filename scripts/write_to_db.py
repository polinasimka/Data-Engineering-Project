import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text


DATA_PATH = "data/finance_ecommerce_typed.parquet"
ROWS_TO_LOAD = 100


load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_url = os.getenv("DB_URL")
db_port = os.getenv("DB_PORT")
db_root_base = os.getenv("DB_ROOT_BASE")

required = {
    "DB_USER": db_user,
    "DB_PASSWORD": db_password,
    "DB_URL": db_url,
    "DB_PORT": db_port,
    "DB_ROOT_BASE": db_root_base,
}

missing = [name for name, value in required.items() if not value]

if missing:
    raise ValueError(
        f"Не заданы переменные окружения: {', '.join(missing)}"
    )

try:
    db_port = int(db_port)
except ValueError as error:
    raise ValueError("DB_PORT должен быть числом") from error

connection_url = URL.create(
    "postgresql+psycopg2",
    username=db_user,
    password=db_password,
    host=db_url,
    port=db_port,
    database=db_root_base,
)

engine = create_engine(connection_url)

data = pd.read_parquet(DATA_PATH)
data = data.head(ROWS_TO_LOAD)

data.to_sql(
    name="simaninapa",
    con=engine,
    if_exists="replace",  # при повторном запуске в таблице остаётся ровно 100 строк
    index=False,
)

with engine.connect() as connection:
    rows_written = connection.execute(
        text("SELECT COUNT(*) FROM simaninapa")
    ).scalar_one()

print("Rows written:", rows_written)

import argparse

from .extract import load_data
from .transform import convert_types
from .load import load_data_to_db


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preview",
        type=int,
        default=10,
        help="Количество строк для просмотра",
    )
    args = parser.parse_args()

    data = load_data(args.preview)
    data = convert_types(data)
    load_data_to_db(data)


if __name__ == "__main__":
    main()
      
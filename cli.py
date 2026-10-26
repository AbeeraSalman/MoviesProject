
import argparse
import os

MIN_YEAR = 1894
MAX_YEAR = 2022


def year_type(value: str) -> int:
    try:
        year = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"{value} is not a valid integer."
        )

    if year < MIN_YEAR or year > MAX_YEAR:
        raise argparse.ArgumentTypeError(
            f"Invalid year: {year}. "
            f"Year must be between {MIN_YEAR} and {MAX_YEAR}."
        )

    return year


def genre_type(value: str) -> str:
    genre = value.strip()

    if not genre or not genre.replace("-", "").isalpha():
        raise argparse.ArgumentTypeError(
            f"'{value}' is not a valid genre."
        )

    return genre


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Movie Report Generator"
    )

    parser.add_argument(
        "-r",
        type=year_type,
        metavar="YEAR",
        help="highest/lowest rating and average runtime for a year"
    )

    parser.add_argument(
        "-g",
        type=genre_type,
        metavar="GENRE",
        help="movie count and mean rating for a genre"
    )

    parser.add_argument(
        "-y",
        type=year_type,
        metavar="YEAR",
        help="top ten movies by votes for a year"
    )

    args = parser.parse_args()
    if args.r is None and args.g is None and args.y is None:
        parser.error("provide at least one of -r, -g, -y")
    return args


def get_file_path() -> str:
    path = os.getenv("MOVIES_FILE_PATH")
    if not path:
        raise SystemExit("Set the MOVIES_FILE_PATH environment variable.")
    if not os.path.isfile(path):
        raise SystemExit(f"File not found: {path}")
    return path


if __name__ == "__main__":
    print(get_args())
    print(get_file_path())
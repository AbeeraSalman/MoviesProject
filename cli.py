import argparse
import os

MIN_YEAR = 1892
MAX_YEAR = 1912


def validate_year(value: str) -> tuple[int | None, str | None]:
    try:
        year = int(value)
    except ValueError:
        return None, f"'{value}' is not a valid integer."

    if year < MIN_YEAR or year > MAX_YEAR:
        return None, (
            f"Invalid year: {year}. "
            f"Year must be between {MIN_YEAR} and {MAX_YEAR}."
        )

    return year, None


def validate_genre(value: str) -> tuple[str | None, str | None]:
    genre = value.strip()

    if not genre or not genre.replace("-", "").isalpha():
        return None, f"'{value}' is not a valid genre."

    return genre, None


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Movie Report Generator")
    parser.add_argument(
        "-r",
        metavar="YEAR",
        help="highest/lowest rating and average runtime for a year",
    )
    parser.add_argument(
        "-g",
        metavar="GENRE",
        help="movie count and mean rating for a genre",
    )
    parser.add_argument(
        "-y",
        metavar="YEAR",
        help="top ten movies by votes for a year",
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

import sys

from analyzer import MovieAnalyzer
from cli import get_args, get_file_path, validate_year, validate_genre
from csv_parser import MovieParser
from report_printer import ReportPrinter


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    args = get_args()
    path = get_file_path()
    movies = MovieParser(path).parse()
    analyzer = MovieAnalyzer(movies)
    printer = ReportPrinter()

    had_error = False

    if args.r is not None:
        year, error = validate_year(args.r)
        if error:
            print(f"error in -r: {error}")
            had_error = True
        else:
            printer.print_year_report(
                year, analyzer.year_rating_report(year)
            )

    if args.g is not None:
        genre, error = validate_genre(args.g)
        if error:
            print(f"error in -g: {error}")
            had_error = True
        else:
            printer.print_genre_report(
                genre, analyzer.genre_report(genre)
            )

    if args.y is not None:
        year, error = validate_year(args.y)
        if error:
            print(f"error in -y: {error}")
            had_error = True
        else:
            printer.print_top_votes_report(
                year, analyzer.top_votes_report(year)
            )

    sys.exit(1 if had_error else 0)


if __name__ == "__main__":
    main()

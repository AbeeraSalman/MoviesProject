import csv
import math
import sys
import statistics
from dataclasses import dataclass
from typing import Optional
sys.stdout.reconfigure(encoding="utf-8")

@dataclass
class Movie:
    movie_id: str
    title_type: str
    original_title: str
    start_year: int
    runtime: Optional[int]
    genres: list[str]
    rating: float
    num_votes: int


def to_int(value: str) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def to_float(value: str) -> Optional[float]:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def to_genres(genre_str: str) -> list[str]:
    if genre_str == "\\N":
        return []
    return genre_str.split(",")


class MovieParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> list[Movie]:
        movies = []
        with open(self.file_path, encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                year = to_int(row["startYear"])
                rating = to_float(row["rating"])
                votes = to_int(row["numVotes"])
                if year is None or rating is None or votes is None:
                    continue
                movie = Movie(
                    movie_id=row["id"],
                    title_type=row["titleType"],
                    original_title=row["originalTitle"],
                    start_year=year,
                    runtime=to_int(row["runtimeMinutes"]),
                    genres=to_genres(row["genres"]),
                    rating=rating,
                    num_votes=votes,
                )
                movies.append(movie)
        return movies


@dataclass
class YearRatingResult:
    highest: Movie
    lowest: Movie
    average_runtime: Optional[float]


@dataclass
class GenreResult:
    movie_count: int
    mean_rating: float


@dataclass
class TopVotesResult:
    top_movies: list[Movie]
    votes_per_circle: int


class MovieAnalyzer:
    def __init__(self, movies: list[Movie]):
        self.movies = movies

    def year_rating_report(self, year: int) -> Optional[YearRatingResult]:
        filtered_movies = [
            movie for movie in self.movies if movie.start_year == year
        ]
        if not filtered_movies:
            return None

        highest = max(filtered_movies, key=lambda m: m.rating)
        lowest = min(filtered_movies, key=lambda m: m.rating)
        runtimes = [
            m.runtime for m in filtered_movies if m.runtime is not None
        ]
        average_runtime = statistics.mean(runtimes) if runtimes else None

        return YearRatingResult(highest, lowest, average_runtime)

    def genre_report(self, genre: str) -> Optional[GenreResult]:
        filtered_movies = [
            movie for movie in self.movies if genre in movie.genres
        ]
        if not filtered_movies:
            return None
        count = len(filtered_movies)
        ratings = [movie.rating for movie in filtered_movies]
        mean_rating = statistics.mean(ratings)
        return GenreResult(count, mean_rating)

    def top_votes_report(self, year: int) -> Optional[TopVotesResult]:
        filtered_movies = [
            movie for movie in self.movies if movie.start_year == year
        ]
        if not filtered_movies:
            return None
        sorted_movies = sorted(
            filtered_movies, key=lambda m: m.num_votes, reverse=True
        )
        top_movies = sorted_movies[:10]
        votes_per_circle = math.ceil(top_movies[0].num_votes / 80)
        return TopVotesResult(top_movies, votes_per_circle)


class ReportPrinter:
    def print_year_report(
        self, year: int, result: Optional[YearRatingResult]
    ) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return
        runtime = (
            f"{result.average_runtime:.1f}"
            if result.average_runtime is not None
            else "N/A"
        )
        print("1st Report----")
        print(f"Highest rating: {result.highest.rating} - "
              f"{result.highest.original_title}")
        print(f"Lowest rating: {result.lowest.rating} - "
              f"{result.lowest.original_title}")
        print(f"Average mean minutes: {runtime}")

    def print_genre_report(
        self, genre: str, result: Optional[GenreResult]
    ) -> None:
        if result is None:
            print(f"No movies found for genre {genre}.")
            return
        print("2nd report-----")
        print(f"Movies found: {result.movie_count}")
        print(f"Average mean rating: {result.mean_rating:.1f}")

    def print_top_votes_report(
        self, year: int, result: Optional[TopVotesResult]
    ) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return
        print("3rd report-----")
        for movie in result.top_movies:
            circles = round(movie.num_votes / result.votes_per_circle)
            print(f"{movie.original_title}  {'● ' * circles}"
                  f"{movie.num_votes}")


# Temporary test lines (delete when main is ready)
movies = MovieParser("movies.csv").parse()
analyzer = MovieAnalyzer(movies)
printer = ReportPrinter()
printer.print_year_report(1903, analyzer.year_rating_report(1903))
printer.print_genre_report("Comedy", analyzer.genre_report("Comedy"))
printer.print_top_votes_report(1892, analyzer.top_votes_report(1892))
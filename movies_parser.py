
import csv
import math
import statistics
from dataclasses import dataclass
from typing import Optional


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
       
        average_runtime = statistics.mean(runtimes) if runtimes else None
      
        return YearRatingResult(highest, lowest, average_runtime)
    
    
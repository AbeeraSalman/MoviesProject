# Environment variable: MOVIES_FILE_PATH

# Movie: holds the information of one movie (8 attributes).
# MovieParser: reads the CSV file and returns a list of Movie objects.
# MovieAnalyzer: takes the movies and calculates the results.
# ReportPrinter: prints the results of each report.
# Argument helper: reads and validates the flags -r, -g, -y.
# Environment helper: reads and validates the file path.
# main: connects all the pieces and runs the program.

# Results dataclasses:
# Report 1 (-r, takes a year):
#   highest movie, lowest movie, average runtime
# Report 2 (-g, takes a genre):
#   movie count, mean rating
# Report 3 (-y, takes a year):
#   list of up to ten movies, votes each circle stands for

# id,titleType,originalTitle,startYear,runtimeMinutes,genres,rating,numVotes
import csv
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


def to_genres(genre_str:str)->list[str]:
    if genre_str == "\\N":
        return []
    return genre_str.split(",")


def print_movie():
    movie = Movie("tt0000001", "short", "The Movie", 2020, 120,
                  ["Action", "Short"], 7.5, 1000)
    print(movie)


print(to_int("45"), to_int("\\N"), to_int("abc"))
print(to_float("5.9"), to_float("\\N"))
print(to_genres("Comedy,Short"), to_genres("\\N"))
print_movie()
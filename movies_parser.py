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
    
class MovieParser:
       def __init__(self,file_path:str):
           self.file_path=file_path
               
       def parse(self)->list[Movie]:
            with open(self.file_path, 'r', encoding='utf-8',newLine="") as file:
                reader=csv.DictReader(file)
                movies=[]
                for row in reader:
                    movie=Movie(
                        movie_id=row['id'],
                        title_type=row['titleType'],
                        original_title=row['originalTitle'],
                        start_year=to_int(row['startYear']),
                        runtime=to_int(row['runtimeMinutes']),
                        genres=to_genres(row['genres']),
                        rating=to_float(row['rating']),
                        num_votes=to_int(row['numVotes'])
                    )
                    movies.append(movie)
                    
                    return movies


print(to_int("45"), to_int("\\N"), to_int("abc"))
print(to_float("5.9"), to_float("\\N"))
print(to_genres("Comedy,Short"), to_genres("\\N"))
print_movie()


movie_parse=MovieParser("movies.csv")
print
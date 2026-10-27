
import csv
import math
from models import Movie


def to_int(value):
    try:
        number = int(value)
    except (ValueError, TypeError):
        return None
    return number if number >= 0 else None
    
    
def to_float(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        return None
    return number if math.isfinite(number) else None


def to_genres(genre_str):
    if genre_str == "\\N":
        return []
    return genre_str.split(",")



class MovieParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    
    def parse(self) -> list[Movie]:
        movies=[]
        with open(self.file_path, encoding="utf-8", newline="") as file:
            reader=csv.DictReader(file)
            for  row in reader:
                year=to_int(row["startYear"])
                rating=to_float(row["rating"])
                votes=to_int(row["numVotes"])
                if (
                    year is None
                    or rating is None
                    or votes is None
                    or not 0 <= rating <= 10
                    or row["id"] is None
                    or row["titleType"] is None
                    or row["originalTitle"] is None
                ):
                    continue
                movie=Movie(
                    movie_id=row["id"],
                    title_type=row["titleType"],
                    original_title=row["originalTitle"],
                    start_year=year,
                    runtime_min=to_int(row["runtimeMinutes"]),
                    genres=to_genres(row["genres"]),
                    rating=rating,
                    num_of_votes=votes,
                )
                movies.append(movie)
            return movies
            
        
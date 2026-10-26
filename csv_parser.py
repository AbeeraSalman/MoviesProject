from models import Movie
import csv

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
    
    
def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


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
                if year is None or rating is None or votes is None:
                    continue
                movie=Movie(
                    movie_id=row["id"],
                    title_type=row["title_type"],
                    original_title=row["original_title"],
                    start_year=year,
                    runtime_min=to_int(row["runtimeMinutes"]),
                    genres=to_genres(row["genres"]),
                    rating=rating,
                    num_of_votes=votes,
                )
                movies.append(movie)
            
        
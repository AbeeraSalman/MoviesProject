from typing import Optional
from sympy import Lambda
import math
from models import Movie, YearRatingResult, GenreResult, TopVoteResult
import statistics
class MovieAnalyzer:
    def __init__(self,movies:list[Movie]):
        self.movies=movies
        
    def year_rating_report(self,year:int) -> Optional[YearRatingResult]: 
        filtered_movies = [
            movie for movie in self.movies if movie.start_year == year
        ]
        if not filtered_movies:
            return None
        highest = max(filtered_movies,key=lambda m:m.rating)
        lowest = min(filtered_movies,key=lambda m:m.rating)
        runtimes = [
            m.runtime for m in filtered_movies if m.runtime is not None
        ]
        average_runtime = statistics.mean(runtimes) if runtimes else None
        return YearRatingResult(highest,lowest,average_runtime)
    
    
    def genre_report(self,genre:str) -> Optional[GenreResult]:
        filtered_movies = [
            movie for movie in self.movies if genre in movie.genres
        ]
        if not filtered_movies:
            return None
        count = len(filtered_movies)
        ratings = [movie.rating for movie in filtered_movies]
        mean_rating = statistics.mean(ratings)
        return GenreResult(count,mean_rating)
    
    def top_votes_report(self,year:int) -> Optional[TopVoteResult]:
        filtered_movies = [
            movie for movie in self.movies if movie.start_year == year
        ]
        if not filtered_movies:
            return None
        sorted_movies=sorted(
            filtered_movies,key=lambda m:m.num_of_votes,reverse=True
        )
        top_movies=sorted_movies[:10]
        votes_per_circle = math.ceil(top_movies[0].num_of_votes / 80)
        return TopVoteResult(top_movies,votes_per_circle)
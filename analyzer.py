import math
import statistics
from typing import Optional

from models import GenreResult, Movie, TopVoteResult, YearRatingResult


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
            m.runtime_min for m in filtered_movies
            if m.runtime_min is not None
        ]
        average_runtime = statistics.mean(runtimes) if runtimes else None
        return YearRatingResult(highest, lowest, average_runtime)

    def genre_report(self, genre: str) -> Optional[GenreResult]:
        genre = genre.lower()
        filtered_movies = [
            movie for movie in self.movies
            if genre in [g.lower() for g in movie.genres]
        ]
        if not filtered_movies:
            return None
        count = len(filtered_movies)
        ratings = [movie.rating for movie in filtered_movies]
        mean_rating = statistics.mean(ratings)
        return GenreResult(count, mean_rating)

    def top_votes_report(self, year: int) -> Optional[TopVoteResult]:
        filtered_movies = [
            movie for movie in self.movies if movie.start_year == year
        ]
        if not filtered_movies:
            return None
        sorted_movies = sorted(
            filtered_movies, key=lambda m: m.num_of_votes, reverse=True
        )
        top_movies = sorted_movies[:10]
        votes_per_circle = [
            max(1, math.ceil(movie.num_of_votes / 80))
            for movie in top_movies
        ]
        return TopVoteResult(top_movies, votes_per_circle)
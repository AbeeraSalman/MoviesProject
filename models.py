
from dataclasses import dataclass
from typing import Optional


@dataclass
class Movie:
    movie_id: str
    title_type: str
    original_title: str
    start_year: int
    runtime_min: Optional[int]
    genres: list[str]
    rating: float
    num_of_votes: int


@dataclass
class YearRatingResult:
    highest_rated_movie: Movie
    lowest_rated_movie: Movie
    average_runtime: Optional[float]


@dataclass
class GenreResult:
    movie_count: int
    mean_rating: float


@dataclass
class TopVoteResult:
    top_movies: list[Movie]
    votes_per_circle: int

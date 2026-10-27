
from typing import Optional

from models import YearRatingResult, GenreResult, TopVoteResult


class ReportPrinter:
    def print_year_report(
        self, year: int, result: Optional[YearRatingResult]
    ) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return

       
        print(
            f"Highest Rated Movie: "
            f"{result.highest_rated_movie.original_title} - "
            f"{result.highest_rated_movie.rating}"
        )
        print(
            f"Lowest Rated Movie: "
            f"{result.lowest_rated_movie.original_title} - "
            f"{result.lowest_rated_movie.rating}"
        )

        if result.average_runtime is not None:
            print(f"Average Runtime: {result.average_runtime:.1f} minutes")
        else:
            print("Average Runtime: N/A")

    def print_genre_report(
        self, genre: str, result: Optional[GenreResult]
    ) -> None:
        if result is None:
            print(f"No movies found for genre {genre}.")
            return

        print(f"{genre} Genre Report:")
        print(f"Total Movies: {result.movie_count}")
        print(f"Average Rating: {result.mean_rating:.1f}")
        
    
    def print_top_votes_report(self, year: int, result: Optional[TopVoteResult]) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return

        print(f"{year} Top Votes Report:")
        for movie in result.top_movies:
            circles = round(movie.num_of_votes / result.votes_per_circle)
            print(f"{movie.original_title}  {'● ' * circles}" f"{movie.num_of_votes}")
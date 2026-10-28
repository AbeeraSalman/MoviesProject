from typing import Optional

from models import GenreResult, TopVoteResult, YearRatingResult


class ReportPrinter:
    def print_year_report(
        self, year: int, result: Optional[YearRatingResult]
    ) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return
        high = result.highest_rated_movie
        low = result.lowest_rated_movie
        runtime = (
            f"{result.average_runtime:.1f}"
            if result.average_runtime is not None
            else "N/A"
        )
        print(f"Highest rating: {high.rating} - {high.original_title}")
        print(f"Lowest rating: {low.rating} - {low.original_title}")
        print(f"Average mean minutes: {runtime}")

    def print_genre_report(
        self, genre: str, result: Optional[GenreResult]
    ) -> None:
        if result is None:
            print(f"No movies found for genre {genre}.")
            return
        print(f"Movies found: {result.movie_count}")
        print(f"Average mean rating: {result.mean_rating:.1f}")

    def print_top_votes_report(
        self, year: int, result: Optional[TopVoteResult]
    ) -> None:
        if result is None:
            print(f"No movies found for year {year}.")
            return
        for movie, per_circle in zip(
            result.top_movies, result.votes_per_circle
        ):
            circles = round(movie.num_of_votes / per_circle)
            print(f"{movie.original_title}  {'● ' * circles}"
                  f"{movie.num_of_votes}")
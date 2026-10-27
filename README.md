# Movie Report Generator

A command-line tool that reads a CSV of movies and prints simple reports:
rating extremes and average runtime for a year, movie count and mean rating
for a genre, and a text bar chart of the top ten movies by votes for a year.

## Requirements

- Python 3.10+ (uses `int | None` type syntax)
- No third-party packages

## Project structure

| File | Purpose |
|------|---------|
| `movies_parser.py` | Entry point (`main()`); wires everything together |
| `cli.py` | Argument parsing, year/genre validation, file-path lookup |
| `csv_parser.py` | `MovieParser`: reads the CSV and skips invalid rows |
| `models.py` | `Movie` and report-result dataclasses |
| `analyzer.py` | `MovieAnalyzer`: year, genre and top-votes calculations |
| `report_printer.py` | `ReportPrinter`: formats results for the terminal |
| `movies.csv` | Sample data set |

## Data format

CSV with this header:

```
id,titleType,originalTitle,startYear,runtimeMinutes,genres,rating,numVotes
```

- `genres` is comma-separated; `\N` means no genres.
- Rows with a missing/invalid year, rating (outside 0–10) or vote count are skipped.
- `runtimeMinutes` is optional; missing values are ignored in the average.

## Usage

Set the `MOVIES_FILE_PATH` environment variable to the CSV, then run with at
least one option:

```powershell
$env:MOVIES_FILE_PATH = "movies.csv"
python movies_parser.py -r 1900 -g Drama -y 1900
```

| Option | Description |
|--------|-------------|
| `-r YEAR` | Highest/lowest rated movie and average runtime for the year |
| `-g GENRE` | Number of movies and mean rating for the genre (case-insensitive) |
| `-y YEAR` | Top ten movies by votes for the year, with a `●` bar per vote chunk |

Options can be combined. Years must be between 1894 and 1912.

## Example output

```
Highest Rated Movie: <title> - 8.1
Lowest Rated Movie: <title> - 3.2
Average Runtime: 12.3 minutes

Drama Genre Report:
Total Movies: 42
Average Rating: 6.4
```

## Known limitations

- Year range is hard-coded in `cli.py` (`MIN_YEAR`/`MAX_YEAR`).
- No automated tests yet.

# Movie Report Generator

A command-line tool that reads a CSV file of movies and prints reports:

1. **Year rating report (`-r`)**: highest-rated movie, lowest-rated movie, and average runtime for a year.
2. **Genre report (`-g`)**: number of movies and mean rating for a genre.
3. **Top votes report (`-y`)**: the ten most-voted movies of a year, with a `●` bar for each.

Several reports can be requested in one command.

## Requirements

- Python 3.10+ (uses `int | None` type syntax)
- No third-party packages

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point: `main()` connects all the pieces |
| `cli.py` | Command-line arguments, year/genre validation, file-path lookup |
| `csv_parser.py` | Converters and `MovieParser` (reads the CSV into `Movie` objects) |
| `models.py` | `Movie` and the result dataclasses |
| `analyzer.py` | `MovieAnalyzer`: calculates the results of each report |
| `report_printer.py` | `ReportPrinter`: prints the results |

Each file has one job: parse, calculate, and print are kept separate.

## Data format

The CSV must have this header:

```
id,titleType,originalTitle,startYear,runtimeMinutes,genres,rating,numVotes
```

- `\N` means a missing value.
- `genres` holds several genres separated by commas, for example `Comedy,Short`.
- Rows with a missing or invalid year, rating, or vote count are skipped.
- A missing `runtimeMinutes` is allowed and is ignored in the average.
- The file is read as UTF-8.

## Setup

The CSV path is read from the `MOVIES_FILE_PATH` environment variable.
The variable lasts only for the current terminal window.

Windows (PowerShell):

```powershell
$env:MOVIES_FILE_PATH = "movies.csv"
```

Mac / Linux:

```bash
export MOVIES_FILE_PATH=movies.csv
```

## Usage

```
python main.py -r 1903
python main.py -g Comedy
python main.py -y 1892
python main.py -r 1903 -g Comedy -y 1892
```

| Option | Value | Report |
|--------|-------|--------|
| `-r` | year | highest rating, lowest rating, average runtime |
| `-g` | genre (not case-sensitive) | movie count and mean rating |
| `-y` | year | top ten movies by votes, with circles |

At least one option is required.

## Top votes chart

`votes_per_circle` is the top movie's votes divided by 80, rounded up, so a
bar never has more than 80 circles. Every movie gets
`round(votes / votes_per_circle)` circles, followed by its vote count.

## Example output

```
Highest rating: 6.9 - Le fiancé ensorcelé
Lowest rating: 4.3 - Compagnons de voyage encombrants
Average mean minutes: 2.4
Movies found: 386
Average mean rating: 5.6
Pauvre Pierrot  ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● 1363
```

The numbers depend on the CSV file you use.

## Error handling

- No option given, or an unknown option: the program stops and shows the usage message.
- An invalid value for one option (a non-integer year, a year outside 1894-1912, an invalid genre): an error is printed for that option only. The other valid reports still run.
- If any option had an error, the program ends with exit code 1.
- Missing `MOVIES_FILE_PATH`, a missing file, or an unreadable file: the program stops with a short message.
- A year or genre with no movies prints "No movies found".

## Known limitations

- The year range (`MIN_YEAR` and `MAX_YEAR`) is hard-coded in `cli.py`.
- No automated tests yet.
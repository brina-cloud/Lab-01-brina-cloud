# Grade Generator and Organizer

Brief README for the two utility scripts in this repo:
- `grade-generator.py` — generate student grades and reports from input data.
- `organizer.sh` — organize files in a directory (by extension or date).

## Requirements
- `grade-generator.py`: Python 3.8+
- `organizer.sh`: Bash (Linux, macOS, WSL on Windows)
- Optional: `pip` packages listed in a `requirements.txt` (none required by default)

## Files
- grade-generator.py — Python script to compute grades, averages and export reports.
- organizer.sh — Bash script to move files into folders by extension or by date.

---

## grade-generator.py

Purpose:
- Read student scores (CSV or JSON), compute totals, averages, and optionally convert numeric scores to letter grades.
- Export results to CSV, JSON, or print to stdout.

Typical usage:
- Basic (read CSV, write CSV):
    ```
    python grade-generator.py -i students.csv -o results.csv
    ```
- With weights and letter grades:
    ```
    python grade-generator.py -i students.csv -o results.csv --weights weights.json --letters
    ```

Common options (example):
- `-i, --input` : input file (CSV or JSON)
- `-o, --output` : output file (CSV or JSON). If omitted, prints to stdout.
- `--weights` : JSON file defining assignment weights
- `--letters` : convert numeric scores to letter grades (A, B, C...)
- `--scale` : grading scale file or preset (optional)
- `--help` : show usage

Input CSV example (columns):
```
name,assignment1,assignment2,exam
Alice,85,90,78
Bob,70,75,80
```

Output example (CSV):
```
name,total,average,letter
Alice,253,84.33,B
Bob,225,75.00,C
```

Notes:
- Validate input columns and handle missing values according to script options.
- Add `--dry-run` to preview changes if supported.

---

## organizer.sh

Purpose:
- Move files from a target directory into subfolders (by extension, by year/month, or custom rules).
- Useful to tidy downloads/working folders.

Typical usage:
- Organize by extension:
    ```
    ./organizer.sh /path/to/dir --by extension
    ```
- Organize by modification date (year/month):
    ```
    ./organizer.sh /path/to/dir --by date
    ```
- Dry run:
    ```
    ./organizer.sh /path/to/dir --by extension --dry-run
    ```

Common options (example):
- First positional arg: target directory (defaults to current directory if omitted)
- `--by` : `extension` | `date` (or other modes implemented)
- `--dry-run` : show actions without moving files
- `--pattern` : only process matching filenames (optional)
- `--help` : show usage

Behavior:
- Creates subdirectories as needed (e.g., `pdf/`, `jpg/` or `2025-11/`).
- Skips directories and hidden files by default (configurable).
- Handles name conflicts by appending a suffix or skipping (implementation-defined).

Installation / Permissions:
```
chmod +x organizer.sh
```

---

## Examples

1) Generate grades and export CSV:
```
python grade-generator.py -i grades/input.csv -o grades/output.csv --letters
```

2) Organize Downloads folder by extension (dry run first):
```
./organizer.sh "$HOME/Downloads" --by extension --dry-run
./organizer.sh "$HOME/Downloads" --by extension
```

---

## Contributing
- Open an issue or PR for bugs, new features or improvements.
- Add tests for edge cases (missing fields, zero weights, filename collisions).

## License
MIT

## Author
Repository scripts by project contributor.

Replace example flags/options with the actual flags implemented in each script if they differ.

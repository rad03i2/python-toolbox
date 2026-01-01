# Calendar reference data

`2026.csv` contains one row per calendar date from January 1 through September 13, 2026.
Use it as a small input dataset for date parsing, chronological sorting, and grouping examples.

| Column | Meaning |
| --- | --- |
| `date` | Calendar date in YYYY-MM-DD format. |
| `weekday` | English weekday name. |
| `day_of_year` | Ordinal day, starting at 1 on January 1. |
| `iso_week` | ISO week number; weeks start on Monday. |

Dates are calendar values without a time or time zone. The file uses UTF-8, a header row,
and comma-separated fields. All values are derived from the Gregorian calendar.

Read the data with Python's standard library:

```python
import csv
from pathlib import Path

path = Path("examples/calendar/2026.csv")
with path.open(encoding="utf-8", newline="") as source:
    rows = list(csv.DictReader(source))
print(len(rows))
print(rows[0]["date"])
```

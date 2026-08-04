#!/usr/bin/env python3
import re
import sys
from pathlib import Path

template = Path(__file__).parent / "template.html"

print("\n--- Flyer Generator ---\n")
date     = input("Date (e.g. Saturday, July 12):  ")
time     = input("Time (e.g. 10:00 AM):           ")
location = input("Location (e.g. 5th Ave & Main): ")
duration = input("Estimated duration (e.g. 2 hrs): ")

html = template.read_text()
html = html.replace("{{ DATE }}", date)
html = html.replace("{{ TIME }}", time)
html = html.replace("{{ LOCATION }}", location)
html = html.replace("{{ DURATION }}", duration)

# sanitize filename from date
slug = re.sub(r"[^a-z0-9]+", "_", date.lower()).strip("_")
out = Path(__file__).parent / f"flyer_{slug}.html"
out.write_text(html)

print(f"\nSaved: {out}")

#!/usr/bin/env python3
"""MapReduce (mapper) Module"""
import sys
import csv


reader = csv.reader(sys.stdin)


for row in reader:
    try:
        _id = row[0].strip()
        company = row[1].strip()
        compensation = row[3].strip()
        print(f"{_id}\t{company},{compensation}")
    except IndexError:
        print(f"Skipping invalid row: {row}", file=sys.stderr)

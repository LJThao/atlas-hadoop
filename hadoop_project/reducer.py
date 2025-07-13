#!/usr/bin/env python3
"""MapReduce (reducer) Module"""
import sys


records = []


for line in sys.stdin:
    try:
        emp_id, rest = line.strip().split('\t')
        company, salary = rest.split(',')
        salary = float(salary)
        records.append((salary, emp_id, company.strip()))
    except:
        continue

# sort by salary in descending order and take the top 10
for salary, emp_id, company in sorted(records, reverse=True)[:10]:
    print(f"{emp_id}\t{salary}\t{company}")

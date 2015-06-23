#!/usr/bin/env python
import csv


def average(grades):
    return sum(grades) / len(grades)


def main():
    with open('grades.csv') as f:
        grade_reader = csv.DictReader(f)
        grades = {column: [] for column in grade_reader.fieldnames[1:]}
        for row in grade_reader:
            for course in grades.keys():
                grades[course].append(float(row[course]))

    averages = {key: average(val) for key, val in grades.iteritems()}

    with open('results.csv', 'w') as f:
        grade_writer = csv.DictWriter(f, fieldnames=averages.keys())
        grade_writer.writeheader()
        grade_writer.writerow(averages)


if __name__ == '__main__':
    main()

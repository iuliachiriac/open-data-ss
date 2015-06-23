#!/usr/bin/env python
import datetime

DATE_FORMAT = '%d-%m-%Y %H:%M'
XMAS_DATE = '25-12-2015 00:00'


def main():
    now = datetime.datetime.now()
    print('Current time: ' + now.strftime(DATE_FORMAT))

    xmas = datetime.datetime.strptime(XMAS_DATE, DATE_FORMAT)
    time_left = xmas - now
    print('Seconds until Christmas: ' + str(time_left.total_seconds()))


if __name__ == '__main__':
    main()

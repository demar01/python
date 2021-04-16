import urllib.request as request
import csv
r = request.urlopen('https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv').read().decode('utf8').split("\n")
reader = csv.reader(r)
print(reader)
for line in reader:
    print(line)


"""I can also read this file with pandas."""
import pandas as pd
import io
import requests

url="https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(c)
print(type(c)) #<class 'pandas.core.frame.DataFrame'>

"""I can also read this file with with Python’s built-in open() function."""
import csv

with open('Chapter_1_IDE-Test/employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
from asyncore import read
import csv

year_start = int(input('Please enter year from:'))
year_end = int(input('Please enter year to:'))

with open("books.csv", 'r') as f:
    reader = csv.reader(f)
    print(line for line in reader)

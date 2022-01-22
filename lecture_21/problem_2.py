from asyncore import read
import csv
from hashlib import new

new_book=["Moby Dick", "Herman Melville", "1851"]

with open('books.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(new_book)

with open("books.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)


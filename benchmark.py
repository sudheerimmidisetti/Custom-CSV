import timeit
import csv
from custom_csv_reader import CustomCsvReader
from custom_csv_writer import CustomCsvWriter

FILE = "test_data.csv"

def custom_read():
    for _ in CustomCsvReader(FILE):
        pass

def standard_read():
    with open(FILE, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass

def custom_write():
    reader = CustomCsvReader(FILE)
    writer = CustomCsvWriter("custom_out.csv")
    writer.writerows(reader)
    writer.close()

def standard_write():
    with open(FILE, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        with open("standard_out.csv", "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerows(reader)

print("Custom Read:", timeit.timeit(custom_read, number=3))
print("CSV Read:", timeit.timeit(standard_read, number=3))
print("Custom Write:", timeit.timeit(custom_write, number=3))
print("CSV Write:", timeit.timeit(standard_write, number=3))

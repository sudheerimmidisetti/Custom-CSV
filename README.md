# 📄 Custom CSV Reader and Writer in Python

## 📌 Project Overview

This project implements a **custom CSV (Comma-Separated Values) reader and writer from scratch in Python**, without using Python’s built-in `csv` module for parsing or writing logic.  
The goal is to understand the internal mechanics of CSV parsing, including handling complex real-world cases such as quoted fields, escaped characters, and embedded newlines.

The project demonstrates strong fundamentals in **file I/O**, **string parsing**, **state-machine-based logic**, and **performance benchmarking**, which are essential skills for data engineering and backend development.

---

## 🎯 Features

### Custom CSV Reader
- Implemented as a **Python iterator**
- Reads files in a **streaming manner** (no full file load)
- Correctly handles:
  - Comma-delimited fields
  - Quoted fields (`"text"`)
  - Escaped quotes (`""`)
  - Embedded newlines inside quoted fields
- Produces output consistent with Python’s standard `csv.reader`

### Custom CSV Writer
- Writes a list of lists to a CSV file
- Automatically:
  - Encloses fields in quotes when required
  - Escapes internal quotes correctly
- Produces standards-compliant CSV output

### Benchmarking
- Compares performance with Python’s built-in `csv` module
- Uses a synthetic dataset with **10,000+ rows**
- Benchmarks both **read** and **write** operations

---

## 🛠 Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/sudheerimmidisetti/Custom-CSV.git
cd Custom-CSV
```

## Verify Python Installation

Ensure that Python 3 is installed on your system.
```bash
python --version
```

## Install Dependencies

Install the required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

## Generate Synthetic CSV Data

Generate a CSV file with test data for benchmarking and validation.
```bash
python generate_data.py
```

## Run the Benchmark

Execute the benchmark script to compare the custom CSV implementation with Python’s built-in csv module.
```bash
python benchmark.py
```

## Run Custom CSV Reader or Writer (Optional)

You can directly test the reader and writer using your own scripts or the usage examples provided in this documentation.
After completing these steps, the project will be fully set up and ready to use.

## 📂 Project Structure
Below is the directory structure of the project along with a brief description of each file:
```
Custom-CSV/
│
├── custom_csv_reader.py     # Custom CSV reader implementation
├── custom_csv_writer.py     # Custom CSV writer implementation
├── generate_data.py         # Script to generate synthetic CSV data
├── benchmark.py             # Script to benchmark performance
├── README.md                # Project documentation
├── requirements.txt         # Dependency list (no external dependencies)
└── .gitignore               # Git ignore rules
```

## 🚀 Usage Examples

### Reading a CSV File using `CustomCsvReader`
```python
from custom_csv_reader import CustomCsvReader

reader = CustomCsvReader("test_data.csv")

for row in reader:
    print(row)
```

## 📊 Benchmarking and Performance Analysis

To evaluate the performance of the custom CSV reader and writer, a benchmark was conducted comparing the custom implementation with Python’s built-in `csv` module.

### Benchmark Setup
- A synthetic CSV file with **10,000+ rows and 5 columns** was generated programmatically.
- The dataset includes edge cases such as quoted fields, escaped quotes, and embedded newlines.
- Both **read** and **write** operations were benchmarked.
- Python’s built-in `timeit` module was used to obtain reliable timing results.

### Sample Benchmark Results

| Operation        | Custom Implementation | Python csv Module |
|------------------|----------------------|------------------|
| Read (10k rows)  | ~0.28 seconds        | ~0.03 seconds   |
| Write (10k rows) | ~0.42 seconds        | ~0.07 seconds   |

### Performance Analysis

The benchmark results show that Python’s standard `csv` module significantly outperforms the custom implementation. This is expected because the standard library is implemented in **highly optimized C code**, whereas the custom CSV reader and writer are implemented in **pure Python**.

The custom implementation processes input **character-by-character** using a **state-machine-based approach** to ensure correctness and robustness. While this design is slower, it successfully handles complex edge cases such as quoted fields, escaped quotes, and embedded newlines, which highlights the complexity hidden behind standard CSV libraries.

Overall, the benchmark demonstrates the trade-off between **performance and flexibility**, and validates the correctness of the custom implementation when compared with Python’s built-in CSV handling.

"""benchmark.py

Benchmark custom CSV reader/writer vs standard library csv.
"""
import argparse
import time
import statistics
import csv

from generate_synthetic import generate
from custom_csv_reader import CustomCsvReader
from custom_csv_writer import CustomCsvWriter


def time_function(func, repeat=3):
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        func()
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.mean(times), times


def benchmark(rows: int, cols: int):
    # Generate synthetic CSV
    path = "synthetic.csv"
    print(f"Generating synthetic dataset ({rows} rows, {cols} cols)...")
    generate(path, rows=rows, cols=cols)

    results = {}

    # Baseline read
    def baseline_read():
        with open(path, "r", encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            for _ in r:
                pass

    mean_baseline_read, _ = time_function(baseline_read)
    results["baseline_read_mean"] = mean_baseline_read

    # Custom read
    def custom_read():
        with CustomCsvReader(path) as r:
            for _ in r:
                pass

    mean_custom_read, _ = time_function(custom_read)
    results["custom_read_mean"] = mean_custom_read

    # Load into memory for writing tests
    mem = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        for row in r:
            mem.append(row)

    # Baseline write
    baseline_out = "baseline_out.csv"

    def baseline_write():
        with open(baseline_out, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            for row in mem:
                w.writerow(row)

    mean_baseline_write, _ = time_function(baseline_write)
    results["baseline_write_mean"] = mean_baseline_write

    # Custom write
    custom_out = "custom_out.csv"

    def custom_write():
        with CustomCsvWriter(custom_out) as w:
            w.write_rows(mem)

    mean_custom_write, _ = time_function(custom_write)
    results["custom_write_mean"] = mean_custom_write

    print("Benchmark complete!")
    print(results)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=10000)
    parser.add_argument("--cols", type=int, default=5)
    args = parser.parse_args()
    benchmark(args.rows, args.cols)
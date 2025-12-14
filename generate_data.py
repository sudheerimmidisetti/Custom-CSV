import random
import string

def generate_csv(file_path, rows=10000, cols=5):
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(rows):
            row = []
            for _ in range(cols):
                text = ''.join(random.choices(string.ascii_letters, k=10))
                if random.random() < 0.2:
                    text += ', "quoted"\n'
                row.append(text)
            f.write(",".join(f'"{r}"' for r in row) + "\n")

generate_csv("test_data.csv")

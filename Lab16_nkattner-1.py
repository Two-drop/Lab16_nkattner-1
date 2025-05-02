"""
Data Plotter
author: Noah Kattner
date: 5/02/2025
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('UNRATE.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, col_title in enumerate(header_row):
#     print(f'{index} {col_title}, ', end=' ')
# print()

dates = []
unemployment_rates = []

for row in reader:
    unrate = float(row[1])
    unemployment_rates.append(unrate)

plt.style.use('grayscale')
figure, graph = plt.subplots()
graph.plot(unemployment_rates, color='blue')

plt.show()
"""
Data Plotter
author: Noah Kattner
date: 5/02/2025
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, col_title in enumerate(header_row):
#     print(f'{index} {col_title}, ', end=' ')
# print()

dates = []
unemployment_rates = []

for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    unrate = float(row[1])

    dates.append(current_date)
    unemployment_rates.append(unrate)

plt.style.use('grayscale')
figure, graph = plt.subplots()
graph.plot(dates, unemployment_rates, color='blue')

graph.set_title('Unemployment Rates in Ohio since 1976', fontsize=14)
graph.set_xlabel("Year", fontsize=14)
graph.set_ylabel('Unemp Rate', fontsize=14)
plt.show()
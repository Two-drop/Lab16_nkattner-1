"""
Data Plotter
author: Noah Kattner
date: 5/02/2025
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

class Main:
    """Main class to handle the program
    """
    def __init__(self):
        """Initializes the needed variables to graph the data
        """
        self.path = Path('OHUR.csv')
        self.lines = self.path.read_text(encoding='utf-8').splitlines()

        self.reader = csv.reader(self.lines)
        self.header_row = next(self.reader)

        self.dates = []
        self.unemployment_rates = []

        self.graph_data()

    def graph_data(self):
        """Function to graph data and stylize it
        """
        self.get_data()
        plt.style.use('grayscale')
        figure, graph = plt.subplots()
        graph.plot(self.dates, self.unemployment_rates, color='blue')

        graph.set_title('Unemployment Rates in Ohio since 1976', fontsize=14)
        graph.set_xlabel("Year", fontsize=14)
        graph.set_ylabel('Unemp Rate', fontsize=14)
        plt.show()

    def get_data(self):
        """Function to get the data from the CSV file and append to lists
        """
        for row in self.reader:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            unrate = float(row[1])

            self.dates.append(current_date)
            self.unemployment_rates.append(unrate)

if __name__ == '__main__':
    Main()
# 🚀 Mini Projects: Python for ML

## 1. CSV Data Analyzer
**Description:** Build a pure-Python script (no Pandas allowed) that reads a CSV file, calculates the mean, median, and mode for a specified numerical column, and prints the summary.
**Skills:** File I/O, Lists/Dictionaries, Math operations, CLI arguments.
**Starter Instructions:** Use the built-in `csv` module. Write functions to calculate the statistics. Accept the filename and column name via `sys.argv`.

## 2. Web Scraper for ML Datasets
**Description:** Create a script that scrapes tabular data from a given Wikipedia page and saves it as a structured JSON file.
**Skills:** `requests`, `BeautifulSoup`, JSON parsing, String manipulation.
**Starter Instructions:** Identify a Wikipedia table (e.g., list of countries by population). Extract the headers and rows into a list of dictionaries, then dump to a file using `json.dump`.

## 3. Automated Report Generator
**Description:** Write an OOP-based application that processes raw log files, aggregates errors and warnings, and generates a formatted Markdown report.
**Skills:** OOP (Classes/Objects), File handling, String formatting, Regex (optional).
**Starter Instructions:** Create a `LogParser` class that reads the file, and a `ReportGenerator` class that takes the parsed data and writes out the Markdown file.

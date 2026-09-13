# Matplotlib

This section covers Matplotlib, the main Python library we'll use for data visualization in the Machine Learning journey.

## Topics

- Matplotlib basics
- Line plots
- Bar charts
- Histograms
- Scatter plots
- Pie charts
- Figure customization
- Multiple plots
- Plotting Pandas data
- Saving visualizations

## Structure

- `notes/` — Learning notes and examples
- `exercises/` — Practice problems
- `mini_projects/` — Practical visualization projects

## Goal

Learn how to visualize datasets and understand patterns, trends, distributions, and relationships before applying Machine Learning models.

## Day 1 — Matplotlib Basics

### Topics Covered

- Importing Matplotlib
- `pyplot`
- `plt.plot()`
- `plt.show()`
- `plt.title()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.legend()`
- `plt.grid()`
- `plt.figure()`
- `figsize`
- Plotting multiple lines
- Plotting Pandas DataFrame columns
- Saving graphs with `plt.savefig()`
- Understanding X-axis and Y-axis

### Files

- `notes/01_matplotlib_basics.py`
- `exercises/exercise_01.py`
- `mini_projects/matplotlib_basic_analysis.py`

### What I Learned

- How to create basic line graphs
- How to identify X-axis and Y-axis data
- How to customize graph titles and axis labels
- How to add legends and grids
- How to control figure size
- How to plot data stored in Pandas DataFrames
- How to save visualizations as image files
- How to visualize a value changing across an ordered variable such as months

### Mini Project

Built a Monthly Sales visualization using Pandas and Matplotlib.

The project:

- Creates a small sales dataset
- Uses months as the X-axis
- Uses sales as the Y-axis
- Creates a line plot
- Adds a title and axis labels
- Adds a legend and grid
- Saves the visualization as a PNG file
---
## Day 2 — Bar Charts

### Topics Covered

- Bar charts
- `plt.bar()`
- `plt.barh()`
- Category and numerical values
- Bar width
- X-axis and Y-axis
- Y-axis grid
- Horizontal bar charts
- Plotting Pandas DataFrames with bar charts
- Comparing categories

### Files

- `notes/02_bar_charts.py`
- `exercises/exercise_02.py`
- `mini_projects/matplotlib_bar_analysis.py`

### What I Learned

- How to create vertical bar charts
- How to create horizontal bar charts
- How categories are matched with numerical values
- How to control bar width
- How to add appropriate grid lines
- How to visualize Pandas DataFrame columns
- How to use bar charts for category comparisons

### Mini Project

Built a Product Sales Analysis visualization using Pandas and Matplotlib.

The project:

- Creates a product sales dataset
- Uses products as categories
- Uses units sold as numerical values
- Creates a bar chart
- Adds a title and axis labels
- Adds a Y-axis grid
- Saves the visualization as a PNG file

### Key Concept

Bar charts are useful for comparing values across separate categories.
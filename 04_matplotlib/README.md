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
---
### Current Progress

Matplotlib — Day 4 completed — Covered multiple plots, subplots, `plt.subplot()`, `plt.subplots()`, subplot rows and columns, and basic visualization dashboards.

Next Step: Continue with Matplotlib Day 5 and learn the next visualization techniques.
---
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

## Day 3 — Scatter Plots

### Topics Covered

- Scatter plots
- `plt.scatter()`
- X and Y numerical variables
- Individual data points
- Positive relationships
- Negative relationships
- No obvious relationship
- Point size with `s=`
- Transparency with `alpha=`
- Scatter plots with Pandas
- Basic ML-style data analysis
- Exploratory Data Analysis (EDA)

### Files

- `notes/03_scatter_plots.py`
- `exercises/exercise_03.py`
- `mini_projects/matplotlib_scatter_analysis.py`

### What I Learned

- How to create scatter plots
- How to plot two numerical variables
- How to identify positive and negative relationships
- How to recognize when there is no obvious relationship
- How to control point size and transparency
- How to create scatter plots from Pandas DataFrames
- How scatter plots can help explore relationships before machine learning

### Mini Project

Built a House Size vs House Price scatter plot using Pandas and Matplotlib.

The project:

- Creates a house dataset
- Uses house size as the X-axis
- Uses house price as the Y-axis
- Creates a scatter plot
- Controls point size and transparency
- Adds a title and axis labels
- Adds a grid
- Saves the visualization as a PNG file

### Key Concept

Scatter plots help visualize the relationship between two numerical variables and are useful during Exploratory Data Analysis (EDA).


## Day 4 — Multiple Plots & Subplots

### Topics Covered

- Multiple plots
- Subplots
- `plt.subplot()`
- `plt.subplots()`
- Rows and columns
- Subplot positions
- `fig` and `ax` basics
- Plotting line charts in subplots
- Plotting bar charts in subplots
- Plotting scatter plots in subplots
- `tight_layout()`
- Visualization dashboards

### Files

- `notes/04_subplots.py`
- `exercises/exercise_04.py`
- `mini_projects/matplotlib_dashboard.py`

### What I Learned

- How to place multiple graphs in one figure
- How `plt.subplot()` divides a figure into positions
- How `plt.subplots()` creates multiple plotting areas
- How to access different subplot positions
- How to combine different chart types in one figure
- How to use `tight_layout()` to improve subplot spacing
- How multiple visualizations can be combined into a simple dashboard

### Mini Project

Built a Business Visualization Dashboard using Pandas and Matplotlib.

The dashboard:

- Creates a monthly business dataset
- Visualizes monthly sales
- Visualizes monthly customers
- Visualizes monthly profit
- Shows the relationship between customers and profit
- Combines four visualizations into one figure
- Saves the dashboard as a PNG file

### Key Concept

Subplots allow multiple visualizations to be combined into a single figure, making it easier to compare different aspects of a dataset.
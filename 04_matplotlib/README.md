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

Matplotlib — Day 9 completed — Covered annotations, `plt.annotate()`, `plt.text()`, `xy`, `xytext`, `arrowprops`, offset-based annotation positioning, and highlighting important observations in charts.

Next Step: Continue with Matplotlib Day 10 and learn the next visualization techniques.
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
---

## Day 5 — Histograms

### Topics Covered

- Histograms
- `plt.hist()`
- Histogram vs bar chart
- Numerical data distributions
- Bins
- `bins=`
- Frequency and count
- `edgecolor=`
- Histograms with Pandas
- Reading distributions
- Data concentration
- Data spread
- Peaks and unusual values
- Comparing distributions
- `alpha=`
- `label=`
- `plt.legend()`
- `density=True`
- Probability density

### Files

- `notes/05_histograms.py`
- `exercises/exercise_05.py`
- `mini_projects/matplotlib_histogram_analysis.py`

### What I Learned

- How to create histograms from numerical data
- How histograms group values into bins
- How the Y-axis represents frequency
- How to control the number of bins
- How to make histogram bars easier to distinguish
- How to create histograms from Pandas DataFrames
- How to identify concentration and spread in a distribution
- How to compare distributions
- How `density=True` changes a histogram to probability density

### Mini Project

Built a Student Score Distribution visualization using Pandas and Matplotlib.

The project:

- Creates a student score dataset
- Uses scores as numerical data
- Groups scores into bins
- Creates a histogram
- Adds a title and axis labels
- Adds a Y-axis grid
- Saves the visualization as a PNG file

### Key Concept

Histograms show the distribution of a numerical variable by grouping values into ranges and counting how many observations fall into each range.
---

## Day 6 — Pie Charts

### Topics Covered

- Pie charts
- `plt.pie()`
- `labels=`
- `autopct=`
- `startangle=`
- `explode=`
- `shadow=`
- `plt.axis("equal")`
- Categories and proportions
- Parts of a whole
- Pie charts with Pandas
- Pie charts vs bar charts

### Files

- `notes/06_pie_charts.py`
- `exercises/exercise_06.py`
- `mini_projects/matplotlib_pie_analysis.py`

### What I Learned

- How to create pie charts
- How to represent parts of a whole
- How to label pie-chart slices
- How to display percentages
- How to rotate a pie chart
- How to separate slices using `explode`
- How to add a shadow
- How to keep a pie chart circular
- How to create pie charts from Pandas DataFrames
- When pie charts are useful for showing proportions

### Mini Project

Built a Monthly Expense Distribution visualization using Pandas and Matplotlib.

The project:

- Creates a monthly expense dataset
- Uses categories as pie-chart labels
- Uses expenses to determine slice sizes
- Displays percentages
- Highlights the Rent category
- Adds a title
- Saves the visualization as a PNG file

### Key Concept

Pie charts are useful for showing how different categories make up a meaningful whole.
---
## Day 7 — Box Plots

### Topics Covered

- Box plots
- `plt.boxplot()`
- Median
- Quartiles
- Q1
- Q3
- Interquartile Range (IQR)
- Whiskers
- Potential outliers
- `1.5 × IQR` outlier rule
- Comparing multiple datasets
- `plt.xticks()`
- Box plots with Pandas
- Distribution comparison
- Basic ML/EDA use of box plots

### Files

- `notes/07_box_plots.py`
- `exercises/exercise_07.py`
- `mini_projects/matplotlib_box_analysis.py`

### What I Learned

- How to create box plots
- How to interpret the median
- How to understand Q1 and Q3
- How to calculate the IQR
- How whiskers work
- How potential outliers are identified
- How to compare multiple distributions
- How to create box plots from Pandas data
- How box plots can help during Exploratory Data Analysis

### Mini Project

Built a Department Salary Distribution Analysis using Pandas and Matplotlib.

The project:

- Creates a department salary dataset
- Separates salary data by department
- Creates box plots for multiple departments
- Compares salary distributions
- Shows median and spread
- Helps identify potential outliers
- Saves the visualization as a PNG file

### Key Concept

Box plots summarize numerical distributions and make it easy to compare the center, spread, and potential outliers of different datasets.
---
## Day 8 — Plot Customization

### Topics Covered

- Plot customization
- `color=`
- `marker=`
- `linestyle=`
- `linewidth=`
- `markersize=`
- Scatter plot customization
- `s=`
- `alpha=`
- Bar chart customization
- Combining customization options
- Improving visualization readability

### Files

- `notes/08_customization.py`
- `exercises/exercise_08.py`
- `mini_projects/matplotlib_custom_analysis.py`

### What I Learned

- How to change plot colors
- How to add and customize markers
- How to change line styles
- How to control line thickness
- How to control marker size
- How to customize scatter plots
- How to customize bar charts
- How to combine multiple customization options
- How to make visualizations easier to read

### Mini Project

Built a Custom Monthly Sales Analysis using Pandas and Matplotlib.

The project:

- Creates a monthly sales dataset
- Plots monthly sales
- Customizes the line color
- Adds circular markers
- Uses a dashed line
- Controls line and marker sizes
- Adds labels, title, legend, and grid
- Saves the visualization as a PNG file

### Key Concept

Matplotlib customization changes how data is displayed without changing the underlying data.
---
## Day 9 — Annotations

### Topics Covered

- Plot annotations
- `plt.annotate()`
- `plt.text()`
- `xy=`
- `xytext=`
- `arrowprops=`
- `textcoords="offset points"`
- Highlighting important data points
- Annotating line plots
- Annotating scatter plots
- Annotating bar charts
- Positioning annotation text
- Practical EDA use of annotations

### Files

- `notes/09_annotations.py`
- `exercises/exercise_09.py`
- `mini_projects/matplotlib_annotations_analysis.py`

### What I Learned

- How to add annotations to plots
- How to identify the target point with `xy`
- How to position annotation text with `xytext`
- How to connect annotations to data points with arrows
- How to use offset points for better annotation positioning
- How to add text directly to a graph
- How to highlight important observations
- How annotations can improve EDA visualizations

### Mini Project

Built a Monthly Sales Analysis with annotations using Pandas and Matplotlib.

The project:

- Creates a monthly sales dataset
- Creates a sales line plot
- Highlights the highest sales
- Highlights a sales drop
- Uses arrows to connect annotations to data points
- Uses offset positioning for readable annotations
- Saves the visualization as a PNG file

### Key Concept

Annotations allow important observations in a visualization to be highlighted and explained directly on the graph.
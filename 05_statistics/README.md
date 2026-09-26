### Current Progress

Statistics & Probability — Day 6 completed — Covered conditional probability, the conditional probability formula, contingency tables, independent and dependent events, and applications in Machine Learning.

Next Step: Continue with Statistics Day 7 and learn Bayes' theorem.

---
## Day 1 — Descriptive Statistics

### Topics Covered

- Descriptive statistics
- Population vs sample
- Mean
- Median
- Mode
- Minimum
- Maximum
- Range
- Mean vs median
- Effect of extreme values
- Descriptive statistics in ML

### Files

- `notes/01_descriptive_statistics.py`
- `exercises/exercise_01.py`
- `mini_projects/statistics_basic_analysis.py`

### What I Learned

- What descriptive statistics are
- The difference between a population and a sample
- How mean represents the average
- How median represents the middle of ordered data
- How mode represents the most frequent value
- How to identify minimum and maximum values
- How to calculate and interpret range
- Why mean can be affected by extreme values
- Why median can be useful when data contains outliers
- Why descriptive statistics are useful during ML data analysis

### Mini Project

Built a Student Score Statistical Analysis.

The project:

- Creates a student score dataset
- Calculates the mean
- Calculates the median
- Finds the mode
- Finds the minimum and maximum
- Calculates the range
- Produces a basic statistical summary of the dataset

### Key Concept

Descriptive statistics summarize the important characteristics of a dataset and provide an initial understanding of the data before further analysis or machine learning.
---
## Day 2 — Variance & Standard Deviation

### Topics Covered

- Data spread
- Variance
- Distance from the mean
- Squared deviations
- Population variance
- Sample variance
- Standard deviation
- Population standard deviation
- Sample standard deviation
- `ddof=1`
- Interpreting standard deviation
- Effect of outliers on variance and standard deviation
- Variance vs standard deviation
- Range vs standard deviation
- Statistical spread in ML

### Files

- `notes/02_variance_standard_deviation.py`
- `exercises/exercise_02.py`
- `mini_projects/statistics_spread_analysis.py`

### What I Learned

- Why mean alone is not enough to describe a dataset
- How variance measures average squared distance from the mean
- How standard deviation represents spread in the original units
- The difference between population and sample calculations
- How `ddof=1` is used for sample standard deviation
- How to interpret small and large standard deviations
- Why standard deviation is affected by outliers
- Why range and standard deviation measure spread differently
- Why variation is important when analyzing ML features

### Mini Project

Built a Student Score Spread Analysis.

The project:

- Creates a student score dataset
- Calculates the mean
- Calculates variance
- Calculates standard deviation
- Calculates minimum and maximum
- Calculates range
- Compares different measures of spread

### Key Concept

Standard deviation describes how much data typically varies around its mean. A small standard deviation indicates relatively consistent values, while a large standard deviation indicates greater spread.
---
## Day 3 — Percentiles & Quartiles

### Topics Covered

- Percentiles
- Percentile rank
- 25th, 50th, 75th, and 90th percentiles
- Quartiles
- Q1
- Q2
- Q3
- Q2 as the median
- Middle 50% of data
- Interquartile Range (IQR)
- Percentiles vs quartiles
- IQR-based outlier detection
- Box plot concepts
- Percentiles in ML and EDA

### Files

- `notes/03_percentiles_quartiles.py`
- `exercises/exercise_03.py`
- `mini_projects/statistics_percentile_analysis.py`

### What I Learned

- What a percentile represents
- How percentiles describe the relative position of a value in a dataset
- The difference between percentage and percentile
- How quartiles divide ordered data
- Why Q1 represents the 25th percentile
- Why Q2 represents the 50th percentile and median
- Why Q3 represents the 75th percentile
- How the IQR describes the spread of the middle 50% of data
- How IQR is less affected by extreme values than range
- How the 1.5 × IQR rule can identify potential outliers
- How quartiles and IQR connect to box plots
- Why percentiles are useful for ML data analysis and EDA

### Mini Project

Built a Student Score Percentile Analysis.

The project:

- Creates a student score dataset
- Calculates Q1, Q2, and Q3
- Calculates the IQR
- Calculates lower and upper outlier boundaries
- Identifies potential outliers

### Key Concept

Percentiles describe the relative position of values within a dataset, while quartiles divide the data into four parts. The IQR measures the spread of the middle 50% and can be used to identify potential outliers.
---
## Day 4 — Distributions

### Topics Covered

- Distributions
- Frequency distributions
- Probability distributions
- Distribution shape
- Symmetric distributions
- Normal distribution
- Uniform distribution
- Right-skewed distributions
- Left-skewed distributions
- Mean and median in different distributions
- Standard deviation and distribution spread
- Histograms
- Distributions in EDA
- Distributions in Machine Learning

### Files

- `notes/04_distributions.py`
- `exercises/exercise_04.py`
- `mini_projects/statistics_distribution_analysis.py`

### What I Learned

- What a distribution represents
- How frequency describes how often values occur
- How probability distributions describe the likelihood of possible outcomes
- How to recognize different distribution shapes
- The characteristics of a normal distribution
- How standard deviation affects the spread of a normal distribution
- What a uniform distribution represents
- How to identify right-skewed and left-skewed distributions
- How skewness can affect the relationship between mean and median
- Why mean is sensitive to extreme values
- How histograms help visualize distributions
- Why distribution analysis is important during EDA
- Why understanding feature distributions is useful in Machine Learning

### Mini Project

Built a Student Score Distribution Analysis.

The project:

- Creates a student score dataset
- Calculates the mean
- Calculates the median
- Calculates standard deviation
- Calculates Q1 and Q3
- Visualizes the distribution using a histogram
- Demonstrates right-skewed data
- Demonstrates left-skewed data
- Compares mean and median for different distributions

### Key Concept

A distribution describes how values are spread across a dataset. Understanding its shape helps identify concentration, spread, skewness, and unusual patterns that may not be obvious from a single statistical measure.
---
## Day 5 — Probability Fundamentals

### Topics Covered

- Probability
- Experiments
- Outcomes
- Sample spaces
- Events
- Favorable outcomes
- Basic probability formula
- Probability range
- Impossible events
- Certain events
- Complements
- Addition rule
- Mutually exclusive events
- Independent events
- Dependent events
- Multiplication rule for independent events
- Experimental probability
- Probability in Machine Learning

### Files

- `notes/05_probability_fundamentals.py`
- `exercises/exercise_05.py`
- `mini_projects/statistics_probability_analysis.py`

### What I Learned

- What probability represents
- How experiments, outcomes, and sample spaces are related
- How to define events
- How to calculate basic probability
- Why probability always falls between 0 and 1
- How to calculate the complement of an event
- How the addition rule works
- The difference between mutually exclusive and independent events
- How independent events use the multiplication rule
- How dependent events differ from independent events
- How experimental probability can be estimated from repeated trials
- Why probability is important for Machine Learning

### Mini Project

Built a Coin Flip Probability Analysis.

The project:

- Simulates 1,000 coin flips
- Counts Heads and Tails
- Calculates experimental probabilities
- Verifies that the probabilities add up to approximately 1
- Demonstrates the difference between theoretical and experimental probability

### Key Concept

Probability provides a mathematical way to represent uncertainty and measure how likely events are to occur. It forms an important foundation for understanding later concepts such as conditional probability, Bayes' theorem, probability distributions, and Machine Learning classification.
---
## Day 6 — Conditional Probability

### Topics Covered

- Conditional probability
- \(P(A \mid B)\) notation
- Conditional probability formula
- Given information
- Conditional probability using tables
- Real-life applications
- Independent and dependent events
- Relationship between conditional probability and independence
- Conditional probability in Machine Learning

### Files

- `notes/06_conditional_probability.py`
- `exercises/exercise_06.py`
- `mini_projects/statistics_conditional_probability.py`

### What I Learned

- What conditional probability represents
- How additional information changes probability
- How to interpret \(P(A \mid B)\)
- How to calculate conditional probability using the formula
- How to calculate conditional probability from a contingency table
- Why \(P(A \mid B)\) and \(P(B \mid A)\) can have different values
- How conditional probability relates to independent and dependent events
- How conditional probability is used in Machine Learning

### Mini Project

Built a Student Course Probability Analysis.

The project:

- Creates a student course enrollment dataset
- Calculates the probability of studying Python
- Calculates the probability of studying JavaScript
- Calculates the probability of studying both courses
- Calculates conditional probabilities
- Checks whether the two events are independent

### Key Concept

Conditional probability measures the probability of an event occurring when another event is already known to have occurred. It allows us to update probabilities based on available information and is an important foundation for Bayes' theorem and Machine Learning.

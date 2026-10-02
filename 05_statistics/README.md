### Current Progress

Statistics & Probability — Day 12 completed — Covered hypothesis testing, null and alternative hypotheses, test directions, significance levels, Z-statistics, critical values, p-values, Type I and Type II errors, statistical power, and ML applications.

Next Step: Continue with Statistics Day 13.
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
---
## Day 7 — Bayes' Theorem

### Topics Covered

- Bayes' theorem
- Prior probability
- Likelihood
- Evidence
- Posterior probability
- Bayes' theorem formula
- Updating probabilities with new information
- Conditional probability vs. Bayes' theorem
- Medical testing examples
- Applications in Machine Learning
- Naive Bayes introduction

### Files

- `notes/07_bayes_theorem.py`
- `exercises/exercise_07.py`
- `mini_projects/statistics_bayes_theorem.py`

### What I Learned

- What Bayes' theorem is and why it is useful
- How prior probability represents initial beliefs
- How likelihood measures the probability of evidence under a condition
- How evidence represents the overall probability of an observation
- How posterior probability updates the prior using new evidence
- How to apply Bayes' theorem to medical testing
- Why \(P(A \mid B)\) and \(P(B \mid A)\) are different
- How Bayes' theorem connects to conditional probability
- How Bayes' theorem is used in Machine Learning
- The basic idea behind Naive Bayes

### Mini Project

Built a Medical Test Bayes' Theorem Analysis.

The project:

- Creates a medical testing dataset
- Calculates the prior probability of disease
- Calculates the likelihood of a positive test
- Calculates the evidence
- Applies Bayes' theorem
- Calculates the posterior probability of disease given a positive test

### Key Concept

Bayes' theorem updates the probability of an event using new evidence. It combines prior probability, likelihood, and evidence to calculate posterior probability. It is an important foundation for probabilistic Machine Learning and Naive Bayes.
---
## Day 8 — Random Variables & Expected Value

### Topics Covered

- Random variables
- Discrete random variables
- Continuous random variables
- Probability distributions
- Expected value
- Expected value formula
- Expected value using probability tables
- Long-run average
- Real-life applications of expected value
- Expected value in Machine Learning

### Files

- `notes/08_random_variables_expected_value.py`
- `exercises/exercise_08.py`
- `mini_projects/statistics_expected_value.py`

### What I Learned

- What a random variable represents
- The difference between discrete and continuous random variables
- How probability distributions describe possible outcomes
- What expected value means
- How to calculate expected value using probabilities
- Why expected value represents a long-run average rather than a guaranteed outcome
- How expected value can be applied to real-life problems
- How expected value is useful in Machine Learning

### Mini Project

Built a Daily Sales Expected Value Analysis.

The project:

- Creates a daily sales probability distribution
- Calculates weighted sales for each possible outcome
- Checks that the probabilities sum to 1
- Calculates expected daily sales

### Key Concept

Expected value is the probability-weighted average of a random variable. It represents the long-run average outcome over repeated trials and is useful for reasoning about uncertainty in statistics and Machine Learning.
---
## Day 9 — Covariance & Correlation

### Topics Covered

- Covariance
- Positive covariance
- Negative covariance
- Zero covariance
- Population covariance
- Sample covariance
- Pearson correlation coefficient
- Correlation range (-1 to +1)
- Strength and direction of linear relationships
- Covariance vs. correlation
- Correlation vs. causation
- Nonlinear relationships
- Correlation in EDA and Machine Learning

### Files

- `notes/09_covariance_correlation.py`
- `exercises/exercise_09.py`
- `mini_projects/statistics_correlation_analysis.py`

### What I Learned

- How covariance describes the direction in which two variables vary together
- The difference between positive, negative, and near-zero covariance
- The difference between population and sample covariance
- Why covariance magnitude depends on units and scale
- How Pearson correlation standardizes covariance
- How to interpret correlation values between -1 and +1
- Why correlation measures linear association
- Why zero correlation does not rule out a nonlinear relationship
- Why correlation does not prove causation
- How covariance and correlation help analyze ML features

### Mini Project

Built a Student Performance Correlation Analysis.

The project:

- Creates a dataset containing study hours, exam scores, and sleep hours
- Calculates a covariance matrix
- Calculates a correlation matrix
- Examines the relationship between study hours and exam scores
- Visualizes the relationship using a scatter plot

### Key Concept

Covariance describes how two variables vary together, while correlation standardizes the direction and strength of their linear relationship. Correlation is easier to interpret and compare, but it does not establish causation.
---
## Day 10 — Sampling & Sampling Distributions

### Topics Covered

- Population and sample
- Population parameters and sample statistics
- Sampling and statistical inference
- Simple random sampling
- Systematic sampling
- Stratified sampling
- Cluster sampling
- Sampling bias
- Sampling variability
- Sampling distributions
- Standard error
- Central Limit Theorem (CLT)
- Sampling in Machine Learning

### Files

- `notes/10_sampling.py`
- `exercises/exercise_10.py`
- `mini_projects/statistics_sampling_analysis.py`

### What I Learned

- The difference between a population and a sample
- How sample statistics are used to estimate population parameters
- How simple random, systematic, stratified, and cluster sampling work
- Why sampling bias can produce misleading results
- How different samples produce different statistics
- What a sampling distribution represents
- The difference between standard deviation and standard error
- How sample size affects standard error
- How the Central Limit Theorem explains the behavior of sample means
- Why sampling is important in Machine Learning

### Mini Project

Built a Sampling Analysis of Student Performance.

The project:

- Simulates a population of student scores
- Draws repeated random samples of different sizes
- Calculates sample means and standard errors
- Compares observed and theoretical standard errors
- Visualizes sampling distributions for different sample sizes
- Examines how sample size affects sampling variability

### Key Concept

Sampling allows us to estimate population characteristics using a subset of observations. Sampling distributions and standard errors help us understand the uncertainty in those estimates. Larger samples generally reduce sampling variability, while biased sampling can still lead to misleading conclusions.
---
## Day 11 — Confidence Intervals

### Topics Covered

- Point estimates and interval estimates
- Confidence intervals
- Confidence levels (90%, 95%, and 99%)
- Margin of error
- Confidence intervals for population means
- Z-confidence intervals
- t-confidence intervals
- Critical values and degrees of freedom
- Standard error in confidence intervals
- Factors affecting interval width
- Confidence intervals in Machine Learning

### Files

- `notes/11_confidence_intervals.py`
- `exercises/exercise_11.py`
- `mini_projects/statistics_confidence_interval_analysis.py`

### What I Learned

- The difference between point estimates and interval estimates
- How confidence intervals estimate unknown population parameters
- How to interpret confidence levels using repeated sampling
- How margin of error determines interval width
- When to use Z-intervals and t-intervals
- How degrees of freedom affect t critical values
- How sample size, confidence level, and variability affect interval width
- How confidence intervals help express uncertainty in ML evaluation

### Mini Project

Built a Student Performance Confidence Interval Analysis.

The project:

- Simulates a population of student exam scores
- Draws samples of different sizes
- Calculates confidence intervals at 90%, 95%, and 99% confidence levels
- Compares interval widths across sample sizes and confidence levels
- Checks whether intervals contain the simulated population mean
- Visualizes confidence interval width and interval bounds

### Key Concept

A confidence interval provides a range of plausible values for an unknown population parameter. The confidence level describes the long-run coverage of the interval method. Larger samples generally produce narrower intervals, while higher confidence levels generally produce wider intervals.
---
## Day 12 — Hypothesis Testing Fundamentals

### Topics Covered

- Hypothesis testing
- Null hypothesis (H₀)
- Alternative hypothesis (H₁)
- Two-tailed tests
- Left-tailed and right-tailed tests
- Significance level (α)
- Test statistics
- Critical values
- P-values
- Type I and Type II errors
- Statistical power
- Hypothesis testing in Machine Learning

### Files

- `notes/12_hypothesis_testing.py`
- `exercises/exercise_12.py`
- `mini_projects/hypothesis_testing_analysis.py`

### What I Learned

- How hypothesis testing evaluates claims about a population using sample data
- The difference between null and alternative hypotheses
- How to identify two-tailed, left-tailed, and right-tailed tests
- How significance levels determine rejection thresholds
- How to calculate a Z-test statistic
- How to calculate and interpret p-values using SciPy
- How to make decisions using critical values and p-values
- The difference between Type I and Type II errors
- How statistical power relates to Type II errors
- How hypothesis testing can help evaluate differences in ML model performance

### Mini Project

Built a Student Exam Score Hypothesis Testing Analysis.

The project:

- Simulates a population of student exam scores
- Draws a random sample from the population
- Calculates the sample mean and standard deviation
- Performs a two-tailed Z-test
- Calculates the standard error, Z-statistic, and p-value
- Compares the p-value with the significance level
- Makes a statistical decision
- Visualizes the sample distribution and hypothesis test

### Key Concept

Hypothesis testing uses sample data to evaluate a claim about a population. The p-value measures how unusual the observed result would be if the null hypothesis were true. A small p-value provides evidence against the null hypothesis, but does not prove the alternative hypothesis.



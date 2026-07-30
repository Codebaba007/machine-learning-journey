# 🎤 Machine Learning Interview Preparation Notes

This document contains a curated list of questions and templates to prepare for Machine Learning / Data Science interviews.

---

## 🐍 1. Python & Programming

### 1.1. What is the difference between a list and a tuple in Python?
- **Key Points:**
  - Lists are mutable, tuples are immutable.
  - Lists have a variable size, tuples have a fixed size.
  - Tuples are slightly faster and more memory efficient.
- **My Answer:** [To be filled]

### 1.2. Explain generators and the `yield` keyword.
- **Key Points:**
  - Generators return an iterator that computes one value at a time.
  - `yield` pauses the function saving all its states, and later continues from there.
  - Memory efficient for large datasets.
- **My Answer:** [To be filled]

### 1.3. What are decorators in Python?
- **Key Points:**
  - Functions that modify the functionality of another function.
  - Wraps a function without permanently modifying it.
- **My Answer:** [To be filled]

*(7 more Python questions...)*

---

## 📊 2. Statistics & Probability

### 2.1. Explain the Central Limit Theorem.
- **Key Points:**
  - The sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the population distribution.
  - Usually applies when n >= 30.
- **My Answer:** [To be filled]

### 2.2. What is a p-value?
- **Key Points:**
  - The probability of obtaining test results at least as extreme as the results actually observed, assuming the null hypothesis is correct.
- **My Answer:** [To be filled]

### 2.3. Explain Bayes' Theorem.
- **Key Points:**
  - P(A|B) = [P(B|A) * P(A)] / P(B)
  - Updates the probability of a hypothesis as more evidence or information becomes available.
- **My Answer:** [To be filled]

*(7 more Statistics questions...)*

---

## 🤖 3. Machine Learning Theory

### 3.1. Explain the Bias-Variance Tradeoff.
- **Key Points:**
  - High bias causes underfitting. High variance causes overfitting.
  - Total Error = Bias² + Variance + Irreducible Error.
- **My Answer:** [To be filled]

### 3.2. How does Regularization work (L1 vs L2)?
- **Key Points:**
  - Adds a penalty to the loss function.
  - L1 (Lasso) uses absolute weights, causes sparsity (feature selection).
  - L2 (Ridge) uses squared weights, shrinks weights evenly.
- **My Answer:** [To be filled]

### 3.3. What is Cross-Validation?
- **Key Points:**
  - A technique to evaluate a model's performance by training it on subsets of input data and evaluating on a complementary subset (e.g., k-fold).
- **My Answer:** [To be filled]

*(12 more ML Theory questions...)*

---

## 🧠 4. Deep Learning

### 4.1. What is the Vanishing Gradient Problem?
- **Key Points:**
  - Gradients become extremely small during backpropagation, stopping earlier layers from learning.
  - Often caused by Sigmoid/Tanh activations; mitigated by ReLU and ResNets.
- **My Answer:** [To be filled]

### 4.2. Explain Batch Normalization.
- **Key Points:**
  - Normalizes the inputs of each layer to have a mean of 0 and variance of 1.
  - Stabilizes and speeds up training.
- **My Answer:** [To be filled]

### 4.3. What is the purpose of Dropout?
- **Key Points:**
  - Randomly zeroes out a fraction of neurons during training to prevent overfitting.
- **My Answer:** [To be filled]

*(7 more Deep Learning questions...)*

---

## 🏗️ 5. System Design for ML

### Scenario 1: Design a Recommendation System for Netflix.
- **Key Points:**
  - Collaborative Filtering vs Content-Based.
  - Matrix Factorization.
  - Cold start problem handling.
- **My Answer:** [To be filled]

### Scenario 2: Design a Fraud Detection System.
- **Key Points:**
  - Imbalanced data handling (SMOTE, precision-recall optimization).
  - Real-time latency constraints.
- **My Answer:** [To be filled]

*(3 more Scenarios...)*

---

## 🤝 6. Behavioral Questions

### Template 1: Tell me about a time you worked with a difficult dataset.
- **Situation:**
- **Task:**
- **Action:**
- **Result:**

### Template 2: Tell me about a time your model failed in production.
- **Situation:**
- **Task:**
- **Action:**
- **Result:**

*(3 more Behavioral Templates...)*

---

## 💻 7. Coding Challenges

Focus on these patterns on LeetCode/HackerRank:
- Array and String manipulation (Two Pointers, Sliding Window)
- Hash Maps / Dictionaries
- SQL Queries (Joins, Window Functions, Group By)
- Basic Matrix operations

---

## 💡 8. Tips & Strategies

- **Clarify the Problem:** Always ask clarifying questions before jumping to a solution.
- **Think Out Loud:** Interviewers care more about your thought process than the final answer.
- **Start Simple:** Suggest a simple baseline model (e.g., Logistic Regression) before jumping to Deep Learning.
- **Know Your Resume:** Be prepared to explain any project or model listed on your resume in deep mathematical detail.

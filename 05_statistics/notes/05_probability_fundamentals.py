import numpy as np

die_rolls = np.arange(1, 7)

even = die_rolls[die_rolls % 2 == 0]

probability_even = len(even) / len(die_rolls)

print("Probability of even:", probability_even)

probability_not_even = 1 - probability_even

print("Probability of not even:", probability_not_even)

probability_three = 1 / 6
probability_five = 1 / 6

probability_three_or_five = probability_three + probability_five

print("Probability of 3 or 5:", probability_three_or_five)

probability_six_twice = (1 / 6) * (1 / 6)

print("Probability of two sixes:", probability_six_twice)
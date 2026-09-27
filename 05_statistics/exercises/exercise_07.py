prior_spam = 0.20
probability_word_given_spam = 0.80
probability_word_given_not_spam = 0.10

prior_not_spam = 1 - prior_spam

probability_word = (
    probability_word_given_spam * prior_spam
    + probability_word_given_not_spam * prior_not_spam
)

posterior_spam = (
    probability_word_given_spam * prior_spam
    / probability_word
)

print("Prior Probability of Spam:", prior_spam)
print("Probability of Word:", probability_word)
print("Posterior Probability of Spam:", posterior_spam)
import numpy as np
import pandas as pd

np.random.seed(42)

flips = np.random.choice(["Heads", "Tails"], size=1000)

data = pd.DataFrame({
    "Flip": flips
})

heads = (data["Flip"] == "Heads").sum()
tails = (data["Flip"] == "Tails").sum()

total = len(data)

probability_heads = heads / total
probability_tails = tails / total

print("Coin Flip Probability Analysis")
print("Total Flips:", total)
print("Heads:", heads)
print("Tails:", tails)
print("Estimated Probability of Heads:", probability_heads)
print("Estimated Probability of Tails:", probability_tails)
print("Probability Sum:", probability_heads + probability_tails)
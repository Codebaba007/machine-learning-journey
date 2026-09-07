import pandas as pd

trades = pd.DataFrame({
    "Time": [
        "2025-02-01 09:02:00",
        "2025-02-01 09:05:00",
        "2025-02-01 09:09:00",
        "2025-02-01 09:12:00"
    ],
    "Price": [101, 105, 103, 108]
})

prices = pd.DataFrame({
    "Time": [
        "2025-02-01 09:00:00",
        "2025-02-01 09:04:00",
        "2025-02-01 09:08:00",
        "2025-02-01 09:11:00"
    ],
    "Market_Price": [100, 104, 102, 107]
})

trades["Time"] = pd.to_datetime(trades["Time"])
prices["Time"] = pd.to_datetime(prices["Time"])

trades = trades.sort_values("Time")
prices = prices.sort_values("Time")

backward = pd.merge_asof(
    trades,
    prices,
    on="Time",
    direction="backward"
)

forward = pd.merge_asof(
    trades,
    prices,
    on="Time",
    direction="forward"
)

nearest = pd.merge_asof(
    trades,
    prices,
    on="Time",
    direction="nearest"
)

limited = pd.merge_asof(
    trades,
    prices,
    on="Time",
    direction="nearest",
    tolerance=pd.Timedelta("2min")
)

print("Backward Merge")
print(backward)

print("\nForward Merge")
print(forward)

print("\nNearest Merge")
print(nearest)

print("\nNearest Merge With 2 Minute Tolerance")
print(limited)
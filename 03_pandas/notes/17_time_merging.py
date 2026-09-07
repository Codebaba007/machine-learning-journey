import pandas as pd


# Trade data
trades = pd.DataFrame({
    "Time": [
        "2025-01-01 10:01:00",
        "2025-01-01 10:03:00",
        "2025-01-01 10:07:00",
        "2025-01-01 10:10:00"
    ],
    "Price": [100, 102, 105, 103]
})


# Market data
market = pd.DataFrame({
    "Time": [
        "2025-01-01 10:00:00",
        "2025-01-01 10:02:00",
        "2025-01-01 10:05:00",
        "2025-01-01 10:08:00"
    ],
    "Volume": [500, 700, 600, 900]
})


print("Trade Data")
print(trades)

print("\nMarket Data")
print(market)


# Convert time columns
trades["Time"] = pd.to_datetime(trades["Time"], format="mixed")
market["Time"] = pd.to_datetime(market["Time"], format="mixed")


# Sort by time
trades = trades.sort_values("Time")
market = market.sort_values("Time")


# Previous matching time
print("\nBackward Merge")

backward = pd.merge_asof(
    trades,
    market,
    on="Time",
    direction="backward"
)

print(backward)


# Next matching time
print("\nForward Merge")

forward = pd.merge_asof(
    trades,
    market,
    on="Time",
    direction="forward"
)

print(forward)


# Closest matching time
print("\nNearest Merge")

nearest = pd.merge_asof(
    trades,
    market,
    on="Time",
    direction="nearest"
)

print(nearest)


# Limit allowed time difference
print("\nMerge With Tolerance")

tolerance_merge = pd.merge_asof(
    trades,
    market,
    on="Time",
    direction="backward",
    tolerance=pd.Timedelta("2min")
)

print(tolerance_merge)


# Trade data with departments
trades = pd.DataFrame({
    "Time": [
        "2025-01-01 10:01:00",
        "2025-01-01 10:04:00",
        "2025-01-01 10:07:00",
        "2025-01-01 10:10:00"
    ],
    "Department": [
        "CSE",
        "CSE",
        "EEE",
        "EEE"
    ],
    "Score": [80, 85, 75, 90]
})


# Event data
events = pd.DataFrame({
    "Time": [
        "2025-01-01 10:00:00",
        "2025-01-01 10:03:00",
        "2025-01-01 10:06:00",
        "2025-01-01 10:09:00"
    ],
    "Department": [
        "CSE",
        "CSE",
        "EEE",
        "EEE"
    ],
    "Status": [
        "Open",
        "Active",
        "Open",
        "Active"
    ]
})


# Convert and sort time
trades["Time"] = pd.to_datetime(trades["Time"], format="mixed")
events["Time"] = pd.to_datetime(events["Time"], format="mixed")

trades = trades.sort_values("Time")
events = events.sort_values("Time")


# Match within the same department
print("\nMerge Using by")

department_merge = pd.merge_asof(
    trades,
    events,
    on="Time",
    by="Department",
    direction="backward"
)

print(department_merge)


# Nearest event within 3 minutes
print("\nFinal Time-Based Analysis")

final_analysis = pd.merge_asof(
    trades,
    events,
    on="Time",
    by="Department",
    direction="nearest",
    tolerance=pd.Timedelta("3min")
)

print(final_analysis)
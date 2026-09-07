import pandas as pd

sales = pd.DataFrame({
    "Time": [
        "2025-03-01 10:01:00",
        "2025-03-01 10:04:00",
        "2025-03-01 10:07:00",
        "2025-03-01 10:11:00",
        "2025-03-01 10:14:00",
        "2025-03-01 10:18:00"
    ],
    "Department": [
        "CSE",
        "CSE",
        "EEE",
        "EEE",
        "CSE",
        "EEE"
    ],
    "Sales": [500, 650, 450, 700, 800, 550]
})

events = pd.DataFrame({
    "Time": [
        "2025-03-01 10:00:00",
        "2025-03-01 10:03:00",
        "2025-03-01 10:06:00",
        "2025-03-01 10:10:00",
        "2025-03-01 10:13:00",
        "2025-03-01 10:17:00"
    ],
    "Department": [
        "CSE",
        "CSE",
        "EEE",
        "EEE",
        "CSE",
        "EEE"
    ],
    "Event": [
        "Normal",
        "Promotion",
        "Normal",
        "Promotion",
        "Discount",
        "Promotion"
    ]
})

sales["Time"] = pd.to_datetime(sales["Time"])
events["Time"] = pd.to_datetime(events["Time"])

sales = sales.sort_values("Time")
events = events.sort_values("Time")

analysis = pd.merge_asof(
    sales,
    events,
    on="Time",
    by="Department",
    direction="nearest",
    tolerance=pd.Timedelta("2min")
)

analysis["Event"] = analysis["Event"].fillna("No Event")

event_summary = (
    analysis.groupby("Event")["Sales"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

analysis.to_csv("time_based_sales_analysis.csv", index=False)
event_summary.to_csv("event_sales_summary.csv", index=False)

print("Time-Based Sales Analysis")
print(analysis)

print("\nEvent Sales Summary")
print(event_summary)

print("\nFiles Saved")
print("time_based_sales_analysis.csv")
print("event_sales_summary.csv")
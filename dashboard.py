import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("weather.csv")

df["last_updated"] = pd.to_datetime(df["last_updated"])

df["Year"] = df["last_updated"].dt.year
df["Month"] = df["last_updated"].dt.month

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["Season"] = df["Month"].apply(get_season)

monthly_temp = df.groupby("Month")["temperature_celsius"].mean()

monthly_humidity = df.groupby("Month")["humidity"].mean()

monthly_rainfall = df.groupby("Month")["precip_mm"].mean()

season_data = df.groupby("Season").agg({
    "temperature_celsius":"mean",
    "humidity":"mean",
    "precip_mm":"mean"
})

season_data = season_data.reindex([
    "Winter",
    "Spring",
    "Summer",
    "Autumn"
])

correlation = df[
[
"temperature_celsius",
"humidity",
"precip_mm",
"pressure_mb",
"cloud",
"wind_kph"
]
].corr()

top_hot = df.groupby("location_name")["temperature_celsius"].mean().sort_values(ascending=False).head(10)

top_humid = df.groupby("location_name")["humidity"].mean().sort_values(ascending=False).head(10)

top_rain = df.groupby("location_name")["precip_mm"].mean().sort_values(ascending=False).head(10)









fig, ax = plt.subplots(2, 2, figsize=(9, 8))

# Monthly Temperature
monthly_temp.plot(
    ax=ax[0,0],
    marker="o",
    color="red"
)
ax[0,0].set_title("Monthly Average Temperature")
ax[0,0].set_xlabel("Month")
ax[0,0].set_ylabel("Temperature (°C)")
ax[0,0].grid(True)

# Monthly Humidity
monthly_humidity.plot(
    ax=ax[0,1],
    marker="o",
    color="green"
)
ax[0,1].set_title("Monthly Average Humidity")
ax[0,1].set_xlabel("Month")
ax[0,1].set_ylabel("Humidity (%)")
ax[0,1].grid(True)

# Monthly Rainfall
monthly_rainfall.plot(
    ax=ax[1,0],
    marker="o",
    color="blue"
)
ax[1,0].set_title("Monthly Average Rainfall")
ax[1,0].set_xlabel("Month")
ax[1,0].set_ylabel("Rainfall (mm)")
ax[1,0].grid(True)

# Seasonal Analysis
season_data.plot(
    kind="bar",
    ax=ax[1,1]
)
ax[1,1].set_title("Seasonal Weather Analysis")
ax[1,1].set_xlabel("Season")
ax[1,1].set_ylabel("Average Value")
ax[1,1].grid(axis="y")

plt.suptitle(
    "Weather Pattern Analysis Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.show()








fig, ax = plt.subplots(2, 2, figsize=(9,8))

# Top 10 Hottest Locations
top_hot.plot(
    kind="bar",
    ax=ax[0,0],
    color="red"
)

ax[0,0].set_title("Top 10 Hottest Locations")
ax[0,0].set_xlabel("Location")
ax[0,0].set_ylabel("Temperature (°C)")
ax[0,0].tick_params(axis='x', rotation=45)

# Top 10 Most Humid Locations
top_humid.plot(
    kind="bar",
    ax=ax[0,1],
    color="green"
)

ax[0,1].set_title("Top 10 Most Humid Locations")
ax[0,1].set_xlabel("Location")
ax[0,1].set_ylabel("Humidity (%)")
ax[0,1].tick_params(axis='x', rotation=45)

# Top 10 Rainiest Locations
top_rain.plot(
    kind="bar",
    ax=ax[1,0],
    color="blue"
)

ax[1,0].set_title("Top 10 Rainiest Locations")
ax[1,0].set_xlabel("Location")
ax[1,0].set_ylabel("Rainfall (mm)")
ax[1,0].tick_params(axis='x', rotation=45)

# Correlation Heatmap
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    ax=ax[1,1]
)

ax[1,1].set_title("Correlation Heatmap")

plt.suptitle(
    "Weather Pattern Analysis Dashboard - Insights",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.show()
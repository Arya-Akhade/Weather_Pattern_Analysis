import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("weather.csv")# read .csv dataset

print(df.columns) #show cloums name in dataset
print(df.head()) #show first 5 values
# print(df.info()) #Data types
# print(df.isnull().sum())  #check if null value
# df = df.drop_duplicates() #remove duplicate value
# df = df.dropna() #remove missing value

print(df.shape) # Shows the rows
print(df["last_updated"].nunique())
print(df['last_updated'].head())
print(df['last_updated'].dtype)

df['last_updated'] = pd.to_datetime(df['last_updated']) #converts text dates into real datetime values.

print(df['last_updated'].dtype)

df['Year'] = df['last_updated'].dt.year
df['Month'] = df['last_updated'].dt.month

print(df[['last_updated', 'Year', 'Month']].head())


print("Earliest Date:", df['last_updated'].min())
print("Latest Date:", df['last_updated'].max())

print(df['Year'].value_counts().sort_index())

# # Temp Analysis

# print("Average Temperature:",df['temperature_celsius'].mean())

# #humidity analysis
# print( "Average Humidity:",df['humidity'].mean())

# # Rainfall nalysis
# print( "Maximum Rainfall:",df['precip_mm'].max())



monthly_temp = df.groupby('Month')['temperature_celsius'].mean()

print(monthly_temp)




import matplotlib.pyplot as plt

monthly_temp.plot(
    kind='line',
    figsize=(10,5),
    marker='o'
)

plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()


monthly_humidity = df.groupby('Month')['humidity'].mean()

print(monthly_humidity)





import matplotlib.pyplot as plt

monthly_humidity.plot(
    kind='line',
    figsize=(10,5),
    marker='o',
    color='green'
)

plt.title("Average Monthly Humidity")
plt.xlabel("Month")
plt.ylabel("Humidity (%)")
plt.grid(True)

plt.show()


monthly_rainfall = df.groupby('Month')['precip_mm'].mean()

print(monthly_rainfall)

monthly_rainfall.plot(
    kind='line',
    figsize=(10,5),
    marker='o',
    color='blue'
)

plt.title("Average Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)

plt.show()

#Seasonal Analysis

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df['Season'] = df['Month'].apply(get_season)
import matplotlib.pyplot as plt
import numpy as np

# Average values for each season
season_data = df.groupby("Season").agg({
    "temperature_celsius": "mean",
    "humidity": "mean",
    "precip_mm": "mean"
})

# Arrange seasons in order
season_data = season_data.reindex(["Winter", "Spring", "Summer", "Autumn"])

# X-axis positions
x = np.arange(len(season_data.index))
width = 0.25

plt.figure(figsize=(10,6))

# Temperature Bars
plt.bar(
    x - width,
    season_data["temperature_celsius"],
    width,
    label="Temperature (°C)",
    color="red"
)

# Humidity Bars
plt.bar(
    x,
    season_data["humidity"],
    width,
    label="Humidity (%)",
    color="green"
)

# Rainfall Bars
plt.bar(
    x + width,
    season_data["precip_mm"],
    width,
    label="Rainfall (mm)",
    color="blue"
)

# Labels and Title
plt.xticks(x, season_data.index)
plt.xlabel("Season")
plt.ylabel("Average Value")
plt.title("Seasonal Analysis of Temperature, Humidity & Rainfall")

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()





correlation = df[[
    'temperature_celsius',
    'humidity',
    'precip_mm',
    'pressure_mb',
    'cloud',
    'wind_kph'
]].corr()

print(correlation)


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Weather Parameters")

plt.show()




top_hot = df.groupby("location_name")["temperature_celsius"].mean().sort_values(ascending=False).head(10)

print(top_hot)

plt.figure(figsize=(10,5))

top_hot.plot(
    kind="bar",
    color="red"
)

plt.title("Top 10 Hottest Locations")
plt.xlabel("Location")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()





top_humid = df.groupby("location_name")["humidity"] \
              .mean() \
              .sort_values(ascending=False) \
              .head(10)

print(top_humid)

plt.figure(figsize=(10,5))

top_humid.plot(
    kind="bar",
    color="green"
)

plt.title("Top 10 Most Humid Locations")
plt.xlabel("Location")
plt.ylabel("Average Humidity (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()





top_rain = df.groupby("location_name")["precip_mm"] \
             .mean() \
             .sort_values(ascending=False) \
             .head(10)

print(top_rain)

plt.figure(figsize=(10,5))

top_rain.plot(
    kind="bar",
    color="blue"
)

plt.title("Top 10 Rainiest Locations")
plt.xlabel("Location")
plt.ylabel("Average Rainfall (mm)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

df.to_csv("cleaned_weather_data.csv", index=False)

print("Cleaned weather dataset saved successfully!")
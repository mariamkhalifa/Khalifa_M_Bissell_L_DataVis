import matplotlib.polyplot as plt

# bar chart 1
# total medals bar chart
countries = ["USA", "Canada", "Norway", "Finland", "Austria", "Sweden", "Germany", "Switzerland"]
total_medals = [653, 625, 457, 434, 280, 433, 360, 285]

plt.bar(countries, total_medals, label="Total Medals")

plt.xlabel("Total Medals")
plt.ylabel("Country")
plt.title("Olympics Winter Medals 1896 - 2014")
plt.legend()
plt.show()

# bar chart 2
# bronze, silver and medal Canada and USA
total_canada = [107, 203, 315]
medal_canada = ["Bronze", "Silver", "Gold"]

total_usa = [167, 319, 169]
medal_usa = ["Bronze", "Silver", "Gold"]

plt.bar(total_canada, medal_canada, label="Medal Color Total for Canada", color="red")
plt.bar(total_usa, medal_usa, label="Medal Color Total for USA", color="blue")

plt.xlabel("Medal Color")
plt.ylabel("Total Medals")
plt.title("Total Number of Each Medal Color Won By USA and Canada")
plt.legend()
plt.show()


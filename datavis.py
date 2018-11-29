import matplotlib.pyplot as plt

# bar chart 1
# total medals bar chart
countries = ["USA", "Canada"]
total_medals = [653, 625]

plt.bar(countries, total_medals, label="Total Medals")

plt.xlabel("Total Medals")
plt.ylabel("Country")
plt.title("Olympics Winter Medals Canada Vs USA")
plt.legend()
plt.show()

# bar chart 2
# bronze, silver and medal Canada and USA
medal_canada = ["Bronze Ca", "Silver Ca", "Gold Ca"]
total_canada = [107, 203, 315]

medal_usa = ["Bronze USA", "Silver USA", "Gold USA"]
total_usa = [167, 319, 169]

plt.bar(medal_canada, total_canada, label="Medal Color Total for Canada", color="red")
plt.bar(medal_usa, total_usa, label="Medal Color Total for USA", color="blue")

plt.xlabel("Medal Color")
plt.ylabel("Total Medals")
plt.title("Total Number of Each Medal Color Won By USA and Canada")
plt.legend()
plt.show()

# 3 scatter plot 
# bronze, silver and gold medal totals for Canada and USA
medal_color = ["Bronze Ca", "Bronze USA", "Silver Ca", "Silver USA", "Gold Ca", "Gold USA"]
total = [107, 167, 203, 319, 315, 169]

plt.scatter(medal_color, total, label="Total for each Medal Color")

plt.xlabel("Medal Color")
plt.ylabel("Total Medals")
plt.title("Total Number of Each Medal Color Won By USA and Canada")
plt.legend()
plt.show()

# 4 pie chart 
# percentage of medals won by men and women Canada
slices = [62, 38]
labels = ["men", "women"]
colors = ["magenta", "yellow"]

plt.pie(slices, labels=labels, colors=colors, autopct="%1.1f%%")

plt.title ("Percentage of Medals won by Canadian Men and Women")
plt.show()

# 5 pie chart
# percentage of medals won by men and women USA
slices = [63, 37]
labels = ["men", "women"]
colors = ["skyblue", "pink"]

plt.pie(slices, labels=labels, colors=colors, autopct="%1.1f%%")

plt.title ("Percentage of Medals won American by Men and Women")
plt.show()

# 6 simple plot
# medals of Canada by years
years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1964, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
total_m_c= [9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 48, 75, 68, 91, 90]

plt.plot(years, total_m_c)

plt.xlabel("Year")
plt.ylabel("Total Medals")
plt.title("Canada Medals Won by Year")
plt.show()

# 7 simple plot
# medals of Canada by years
total_m_us = [13, 14, 45, 16, 16, 30, 26, 27, 8, 7, 25, 10, 30, 9, 7, 14, 21, 33, 83, 53, 98, 65]

plt.plot(years, total_m_us)

plt.xlabel("Year")
plt.ylabel("Total Medals")
plt.title("USA Medals Won by Year")
plt.show()

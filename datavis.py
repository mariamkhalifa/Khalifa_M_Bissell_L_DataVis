import matplotlib.pyplot as plt
import csv

canada = []
usa = []
categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count +=1 

		elif row[4] == "USA":
			usa.append(row[7])

		elif row[4] == "CAN":
			canada.append(row[7])
	line_count += 1

print('total medals for Canada: ', len(canada))
print('total medals for USA: ', len(usa))

print('processed', line_count, 'row of data')

country = ["Canada", "USA"]
total_medals = [len(canada), len(usa)]

plt.bar(country, total_medals)
plt.ylabel("Total Medals")
plt.xlabel("Canada & USA")
plt.show()

ca_bronze = []
ca_silver = []
ca_gold = []
usa_bronze = []
usa_silver = []
usa_gold = []

for row in canada:
	if row == "Bronze":
		ca_bronze.append(row)
	elif row == "Silver":
		ca_silver.append(row)
	elif row == "Gold":
		ca_gold.append(row)

for row in usa:
	if row == "Bronze":
		usa_bronze.append(row)
	elif row == "Silver":
		usa_silver.append(row)
	elif row == "Gold":
		usa_gold.append(row)

print("total bronze medals for canada: ", len(ca_bronze))
print("total silver medals for canada: ", len(ca_silver))
print("total gold medals for canada: ", len(ca_gold))
print("total bronze medals for usa: ", len(usa_bronze))
print("total silver medals for usa: ", len(usa_silver))
print("total gold medals for usa: ", len(usa_gold))

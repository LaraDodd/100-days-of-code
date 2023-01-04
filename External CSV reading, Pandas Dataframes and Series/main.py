"""this program reads in csv data"""

#can do it using the normal readlines() of a file method
with open("weather_data.csv", "r") as weather_data:
    data = weather_data.readlines()

for line in data:
    print(line)

# can do it using the csv library import
import csv

with open("weather_data.csv", "r") as weather_data:
    data_csv = csv.reader(weather_data)

    temp = []
    for row in data_csv:
        if row[1] != "temp":
            temp.append(int(row[1]))

    print(f"Temperature: {temp}")

# can do it using pandas!
import pandas

#read in csv and create pd DataFrame
pd_data = pandas.read_csv("weather_data.csv")
print(pd_data)

#convert the temp series values into integers
pd_data["temp"] = pd_data["temp"].astype(int)

#use the mean method from series API
mean_temp = pd_data["temp"].mean()
print(round(mean_temp, 2))

#use the mean method from series API
max_temp = pd_data["temp"].max()
print(round(max_temp))

#two ways to call series data
print(pd_data.condition)
print(pd_data["condition"])

# get row data
print(f'rows with rain: {pd_data[pd_data.condition == "Rain"]}')

#print row of max temp
print(pd_data[pd_data.temp == pd_data["temp"].max()])

#get condition of hottest day
hottest_day = pd_data[pd_data.temp == pd_data["temp"].max()]
hottest_day_conditions = hottest_day.condition
print(f"hottest day conditions: {hottest_day_conditions}")

# convert temperature to Farreheit
monday_temp = pd_data[pd_data.day == "Monday"].temp
print(monday_temp)
mon_temp_F = int(monday_temp) * 1.8 + 32
print(mon_temp_F)







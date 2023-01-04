import pandas

# read in csv file
squirrel_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# initialise fur colours list, squirrel count list
fur_colours = ["Gray", "Cinnamon", "Black"]
squirrel_count = []

# cycle through fur colours, create filtered dataframe which only has rows of that fur colour, count the number of rows
for colour in fur_colours:
    filtered_rows = squirrel_df[squirrel_df["Primary Fur Color"] == colour]
    squirrel_count.append(filtered_rows.shape[0])  # shape[0] returns no rows, shape[1] returns no. columns

# put into dict
squirrel_count_dict = {
    "Fur Colour": fur_colours,
    "Number of Squirrels": squirrel_count
}

# convert dict to df
squirrel_count_df = pandas.DataFrame(squirrel_count_dict)
print(squirrel_count_df)

# write to csv
squirrel_count_df.to_csv("squirrel_count.csv")

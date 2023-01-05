import pandas

"""using pandas"""
nato_data_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict_pandas = {row.letter: row.code for (index, row) in nato_data_df.iterrows()}

"""using with open"""
#read in nato file
with open("nato_phonetic_alphabet.csv", "r") as file:
    nato_data = file.readlines()

#process nato data
split_list = [data.split(",") for data in nato_data]

#create a new dictionary using dict comprehension
nato_dict = {split_data[0]: split_data[1].strip("\n") for split_data in split_list if split_data[0] != "letter"}

"""rest of code"""
#Create a list of the phonetic code words from a word that the user inputs.

word = input("Type a word ").upper()

# use list comprehension to create list of nato words based on input word
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)

nato_list_pd = [nato_dict_pandas[letter] for letter in word]
print(nato_list_pd)



#absolute file path
with open("/Users/larad/Desktop/my_file.txt") as file:
    contents = file.read()

print(contents)

# relative file path going to the parent folder
with open("../my_file2.txt") as file:
    contents = file.read()

print(contents)

# relative file path going into a child folder
with open("./text_files/my_file_3.txt") as file:
    contents = file.read()

print(contents)

#relative file path going back through a few folders
with open("../../../../../Desktop/my_file.txt") as file:
    contents = file.read()

print(contents)


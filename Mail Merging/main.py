# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt", "w") as letter:
    output = 'Dear [name], \n' + '\n' + 'You are invited to my birthday this Saturday, I hope you can make it!\n'
    output += '\n' + 'It is open bar btw!\n' + '\n' + 'Lara\n'
    letter.write(output)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
with open("./Input/Names/invited_names.txt") as names:
    for pos, name in enumerate(names, 1):
        name = name.strip("\n")  # strip name of \n (new line)

        # open starting letter and read all contents
        with open("./Input/Letters/starting_letter.txt", "r") as letter:
            letter_contents = letter.readlines()

            # use replace function to replace name section of string with actual na,e
            letter_contents[0] = letter_contents[0].replace("[name]", f"{name}")

            # join together list into a string with join func
            str_letter_contents = ''.join(letter_contents)

            # write to new letter text document, naming it with position
            with open(f"./Output/ReadyToSend/letter{pos}.txt", "w") as letter_to_send:
                letter_to_send.write(str_letter_contents)



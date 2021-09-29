PLACEHOLDER = "[name]"

with open(".\Input\invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)


with open("Input\letter\starting_letter.txt") as letter:
    demo_letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = demo_letter.replace(PLACEHOLDER, stripped_name)

        with open(f"Output\Ready_to_send\letter_for_{stripped_name}", "w") as completed_letter:
            completed_letter.write(new_letter)

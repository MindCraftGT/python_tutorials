#I want to create a program that reads, writes and modifies a file.

def read_write_modify_file():
    input_file = input("Enter File Name: ")
    try:
        with open(input_file, "r") as filename:
            content = filename.read()

            #modify the file
            modified_content = content.replace("Hello", "Goodbye")

            #write the modified content back to the file
            with open(input_file, "w") as filename:
                filename.write(modified_content)

            print(f"File '{input_file}' modified successfully.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except IOError:
        print(f"Unable to read or write to file '{input_file}'.")


read_write_modify_file()

    
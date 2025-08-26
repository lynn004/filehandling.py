# my first "full" file handling program in python :)
# it asks for a file, reads it, changes the text, and saves it to another file

filename = input("Enter the filename you want to read: ")

try:
    # try opening the file
    with open(filename, "r") as f:
        data = f.read()

    print("\nOriginal file content:")
    print(data)

    # modify it a bit... (just making uppercase to keep it simple)
    modified = data.upper()

    # write into a new file (output.txt)
    with open("output.txt", "w") as f:
        f.write(modified)

    print("\nThe modified content has been written to 'output.txt' :)")

# handling possible errors
except FileNotFoundError:
    print("Hmm... that file doesn’t exist. Maybe check the spelling?")
except PermissionError:
    print("I don’t have permission to read that file.")
except Exception as e:
    print("Something unexpected went wrong:", e)
finally:
    print("\n--- Program finished ---")

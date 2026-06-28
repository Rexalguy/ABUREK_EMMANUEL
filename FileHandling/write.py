#Writing a file

text = "I like programming"

file_path = "test.txt"

#Modes
# w - Write (overwrites file)
# a - Append (adds to file)
# r - Read (reads file)
# x - Create (creates file if it doesn't exist)
# r+ - Read and write
# w+ - Write and read
# a+ - Append and read

with open(file_path, "w") as file:
    file.write(text)
    print(f"Written to {file_path}")



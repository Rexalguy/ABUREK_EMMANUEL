#Appending to a file

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

with open(file_path, "a") as file:
    file.write("\n"+text)
    print(f"Appended to {file_path}")

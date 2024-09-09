# Python has seceral function for cratinf , reading, writing, deleting files

# File Handling

# Open(filename,mode) - Function

# filename contains the filename
# mode in  which file is open

# four modes
# "r" - Reading mode
# "a" - append mode , create file if doesn't exist
# "w" - write mdoe ,  create file if doesn't exist
# "x" - create the file

# binary mode or text mode
# "b" - for binary
# "t" - for text

try:
    f = open(r"Files\File.txt","rt")
    print("File open succesfully.")
except FileNotFoundError:
    print("No file found.")

# r for read and t for text and they are default values

# for deleting file we use the os module

import os

# delete the file
if os.path.exists('Files/Myfile.txt'):
    os.remove('Files/Myfile.txt')
else:
    print("File not exist.")


# for removing dir

os.rmdir("Files")

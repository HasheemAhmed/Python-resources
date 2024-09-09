# use to create or read the file

# writing in files

# "a" - mode
#write() function
f = open(r"Files\File.txt","a")

f.write("But the C++ is more faster.\n") # writes in one line so use \n for newline
f.write("but you forget the C.")
f.close()

fi = open(r"Files\File.txt","r")
print(fi.read())
fi.close()
# "w" - mode
f = open(r"Files\File.txt","w")
# deletes all content and then write

f.write("Heeeeelo! Python ")
f.close()

fi = open(r"Files\File.txt","r")
print(fi.read())
fi.close()

# "x" create file, gives error if file is already exist
# "a" create file if file doesn't exist
# "w" create file if file doesn't exist

# creating files
try:    
    cre = open(r'Files\Myfile.txt',"x")
except FileExistsError:
    print("File Already Exist.")

# creates a file

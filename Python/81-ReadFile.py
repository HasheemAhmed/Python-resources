# for reading python file we have to first open it

# Opening file

try:
    f = open(r"Files\File.txt","rt")
    print("File open succesfully.")
except FileNotFoundError:
    print("No file found.")

# read(char) - function

print(f.read(50)) # print first 50 chracters

# Note : After reading file the file cursor moves to that point

# read() - function

print(f.read()) # print thr reaming content of file


# readline()

fil = open(r"Files\File.txt","rt")

print(fil.readline()) # read a line from the file
# now cursor moves to the next line so again realine prints nextline

print(fil.readline()) # print next line


# for reading file line by line

fi = open(r"Files\File.txt","r")

for x in fi:
    print(x, end ="") # print line by line
    # note it take \n at the end of file so end = "" removes that

# close()  to close a file

f.close()
fil.close()
fi.close() # close the file and does not crreate error

# readlines function makes an list of all the lines
k = open(r"Files\File.txt","r")

print(k.readlines())
k.close()

# Storing data in the file and taking as a list

lt1 = ['Apple','Banana','Mango']
lt2 = ['Fruits','Dates','Vegetables']

op = open('Files\Data.txt','w')
for x in lt1:
    op.write(x+",")
else:
    op.write('\n')

for x in lt2:
    op.write(x+",")
else:
    op.write('\n')

op.close()

re = open('Files\Data.txt','r')
lt = re.readlines()

for x in lt:
    lr = x.split(",")
    print(lr)
    


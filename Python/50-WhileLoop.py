# While loop in python

# only two loops in python 
# while
# for

i = 1
while True:
    print(i,end = ' ')

    i += 1
    if i == 4:
        break


print()

i = 0
while i < 10:  # print odd numbers
    
    i += 1
    if i % 2 == 0:
        continue

    print( i , end = ' ')  

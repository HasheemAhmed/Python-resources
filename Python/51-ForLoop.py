# for loop in the pyton

# loop for string
string = 'Python'

for x in string:
    print(x,end = ' ') #Print  P y t h o n  on by one

# loop for lists,sets,tuple,dictionary
lists = list(('Apple','Banana','Mango','Dates'))

for x in lists:
    print(x)

dic = {'name':'Python',
       'age' : 2024}

for x,y in dic.items():
    print(x , y)

# Loop for increment

for x in range(0,10,2):
    print(x, end = ' ') # print 0 2 4 6 8

# first eleement in start
# second element is end
# third element is increment


# pass

for x in [1,2,3]:
    pass  # dont do anything

# else in for loop

for x in lists:
    print(x)
else:  # runs when whole for loop runs
    print('printing is done')

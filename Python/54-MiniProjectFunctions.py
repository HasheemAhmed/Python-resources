# Functions

lt = ['Apple','Mango','Banana']

def PrintList(li):
    [print(x) for x in li]

PrintList(lt)

def addNewItem(li,value):
    li.append(value)

addNewItem(lt,'Dates')
PrintList(lt)


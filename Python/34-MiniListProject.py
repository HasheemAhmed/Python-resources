# project to Combine three list random and sort them 

list1 = list((1 ,2 ,3,4,5))
list2 = list(("Apple","Banana","Mango","Cherry"))
list3 = list((True,False,True,True,False))

# combining these list scattering

list4 = list()
import random as r

while list1 or list2 or list3:
    ranNum1 =r.randrange(0,3)

    if ranNum1 is 0 and len(list1):
        ran = r.randrange(0,len(list1))
        list4.append(list1[ran])
        list1.pop(ran)
    elif ranNum1 is 1 and len(list2):
        ran = r.randrange(0,len(list2))
        list4.append(list2[ran])
        list2.pop(ran)
    elif ranNum1 is 2 and len(list3):
        ran = r.randrange(0,len(list3))
        list4.append(list3[ran])
        list3.pop(ran)

print(list4)


def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

sort = True

while sort:
    sort = False
    for x in range(len(list4) - 1):
        if (isinstance(list4[x], (int, float, bool)) and isinstance(list4[x + 1], str)):
            swap(list4, x, x + 1)
            sort = True
        elif (isinstance(list4[x], float) and isinstance(list4[x + 1], int)):
            swap(list4, x, x + 1)
            sort = True
        
        elif isinstance(list4[x], int) and isinstance(list4[x + 1], int):
            if  list4[x] > list4[x + 1] :
                swap(list4, x, x + 1)
                sort = True
            
            if type(list4[x]) == int and type(list4[x+1]) == bool:
                swap(list4, x, x + 1)
                sort = True
        elif isinstance(list4[x], str) and isinstance(list4[x + 1], str):
            if list4[x] > list4[x + 1]:
                swap(list4, x, x + 1)
                sort = True
        elif isinstance(list4[x], float) and isinstance(list4[x + 1], float):
            if list4[x] > list4[x + 1]:
                swap(list4, x, x + 1)
                sort = True

print(list4)


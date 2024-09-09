# iterators are used for looping an array of any type
# every array has an iter() and next() method

lt = ['Apple','Banana','Mango']
myiter = iter(lt)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# every time you use next it will give next object

for x in lt:
    print(x)

# here the for loop creates an iterator object and executes the next item

# for creating an iterator in classes you have to use
# __iter__()
#__next__()

# the __iter__() method is used to initialize the attributes like init 
# but it return the iterator  object

class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a < 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # stop the iertation if limit exceeds
    
obj = MyNumbers()
itr = iter(obj)

print(next(itr))
print(next(itr))


for x in itr:
    print(x)

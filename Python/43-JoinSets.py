# Union()

s1 = {2,3,4,5}
s2 = {4,5,6,7}

s3 = s1.union(s2) # both are same
s4 = s1 | s2
 
print(s3) # get the all items in the two sets
print(s4)

# Intersection()

s3 = s1.intersection(s2)
s4 = s1 & s2

print(s3) # takes commom elements in the sets
print(s4)

# Intersection_update()

s1.intersection_update(s2)

print(s1) # also takes duplicates but update the original set

# difference()

s1 = {2,3,4,5}
s2 = {4,5,6,7}

s3 = s1.difference(s2) # both are same
s4 = s1 - s2

print(s3) # takes item from set 1 that are not in set 2
print(s4)

# symmetric_difference()

s3 = s1.symmetric_difference(s2) # both are same
s4 = s1 ^ s2 
print(s3) # takes all items that are not common from both sets
print(s4)
#
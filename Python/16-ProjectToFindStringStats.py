x = """Python is a beautiful Language, But Its a Snake.

Javascript is also a beatiful language. ala , galag"""

# Total Chracters in string

print("Total Chracters : " , len(x))

# Total Words in String

char = x.split()
print("Total Words : ", len(char))


# Total number of sentences

sen = x.split('.')
count = 0
for z in sen:
    if  z.strip():
        count += 1
print("Total Sentences : ", count)

#Total Paragrapghs

par = x.split("\n\n")
print("Total paragraphs : " , len(par))

# count the words like the, a, is

words = ['the','a','is']
count = [0,0,0]
word = x.split()
index = 0
for w in words:
    for s in word:
        if w == s.lower():
            count[index] += 1

    index += 1

index = 0
for w in words:
    print('"' + w + '"', "comes : ", count[index], "times")
    index += 1

 
 # Average Senetence length

sentence = x.split('.')
sen = list()
senlen = list()
count = 0
summ = 0
for d in sentence:
    if not d.strip():
        continue

    senlen.insert(count,len(d.strip()))
    sen.insert(count,d.strip())
    summ += len(d.strip())
    count += 1
    
        
print("Average Sentence length is : " , int(summ/count))
print("Shortest Sentence is : ", min(senlen), min(sen,key = len))
print("Longest Sentence is : ",max(senlen), max(sen, key = len))


# palindromic words that are same backward and forward

word = x.split()

def reverse(str1):
    str2 = ""
    l = len(str1) - 1
    for s in str1:
        str2 += str1[l]
        l -= 1
    
    return str2
    
    
    
count = 0
palin = list()
for p in word:

    if p == reverse(p) and len(p) > 2:
        palin.insert(count,p)
        count += 1

print("Palindrome words are : ", count )
for p in palin:
    print(p)


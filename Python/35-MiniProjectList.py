# Project to Optimize the string using given data

data = ['Superior','Good','university', 'Bachelors', 'Computer','Science','is','the','it','am','doing']

string = 'Supeor is a univefffsity. It is very good. I am Doing Baelors in Computer Science.'

def findWords(char,newlist):
    lt = []
  
    for x in newlist:
        sort = True
        for y in char:
            if y not in x.lower():
                sort = False
        
        if sort:
            lt.append(x.lower())

    return lt

def lenCheck(len1,len2,diff):
    return abs(len1 - len2) <= diff 
        
    


def CorrectWords(word = str() ):
    
    nl = list()
    nl.append(word)
    word = word.strip().lower()
    for x in data:
        if word == x.lower():
            return nl
    
    w = list()
    newlist = data.copy()
    for x in word:
        w.append(x)

        if findWords(w,newlist) and len(newlist) > 1:
            newlist = findWords(w,newlist)

    return newlist

lt = string.split();
Optimize = str()
for x in lt:
        lr = CorrectWords(x)
        if CorrectWords(x) and lenCheck(len(x),len(lr[0]),3):
            
            print(lr)
            Optimize = Optimize + lr[0]+ " "
        else:
            Optimize = Optimize + x + ' '
        
print(Optimize)
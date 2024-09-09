# JSON - Java Script Object Notation

import json

# json is a module which is use to exchange data from javascript to python and vice versa

# let suppose we have a json data in string

data = '{"Name" : "Python","Work" : 25}'

# json.loads() - Convert from json to python dictionary

ConvertedData = json.loads(data)

print(ConvertedData)
print('Name : ',ConvertedData['Name'], 'Work : ',ConvertedData['Work'])


datalist = '{"info" : ["Apple" , "banana", "Mango"]}'
lt = json.loads(datalist)

[print(x) for x in lt['info']]

# json.dumps() - Convert pyhton t json

data = { 'Name' : 'Python',
        'Competitor' : ['C++','Java'],
        'isGood' : True,
        }

jsondata = json.dumps(data)
print(jsondata)


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent = 4,separators=(". "," = ")))
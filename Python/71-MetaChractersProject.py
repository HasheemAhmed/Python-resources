sample_text = """
Hello,

My name is John Doe, and you can reach me at john.doe@example.com or jane.doe@sample.net. Feel free to call me at 123-456-7890 or 987.654.3210. You can also visit our website at https://www.example.com or http://sample.net for more information.

Our office is located at 1234 Elm Street, Suite 567, Anytown, USA. If you have any questions, don't hesitate to ask.

Best regards, 
pyhton_developer123@Yahoo.pk 
SU92-BSCS-F24-467@superior.edu.pk
 +92 303 0000008 
 03030000008
John 0303_000_0004
 0303-0000008

P.S. Follow us on social media: 
- Facebook: https://www.facebook.com/example
- Twitter: http://twitter.com/example
- LinkedIn: www.linkedin.com/in/johndoe

Some special characters: !@#$%^&*()_+-=[]{}|;:',.<>/?\\"

Python is a good language for data analysis and machine learning. Python is also popular for web development.

Thanks!
"""


import re
# extracting email address
email = re.findall(r"\b[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.\w+\b",sample_text)

# \b means word start 
#  [a-zA-Z0-9._]+ means alphabets and numeric and . , _ 
# @ means word contain @
#\.means a .after gmail,yahoo etc
# \w+ means after . for com,net,pk,etc


print("Email : ")
for x in email:
    print(x)


# extract phone numbers
phone = re.findall(r"\b\d+[-._ ]*\d{2}\d+[-._ ]*\d{3}\d+\b",sample_text)

print("Phone : ")
for x in phone:
    print(x)



# extracting urls 
urls = re.findall(r"http.?://\S+|www\.\S+",sample_text)

print("URLs : ")
profile = ['facebook','twitter','linkedin','instagram',"google"]
nonprofiles = profile.copy()
for x in urls:
    yes = False
    for y in profile:
        if y in x:
            print(y.title()," : ", x)
            yes = True
            nonprofiles.remove(y)


    if not yes:
        print("Others : " , x)

for x in nonprofiles:
    print(x.title()," : None")


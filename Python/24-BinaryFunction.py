# Decimal to binary convertor

# function to convert decimal to binary

def DecToBin(num):
    binary = ""
    while(num):
        rem = num  % 2
        num = int(num / 2)
        binary += str(rem)

    return binary[::-1] # returning after reversing string

print(DecToBin(10))

# str[start : stop : step] slicing
# if step is -1 then it reverse the string
# step is just a increment in string

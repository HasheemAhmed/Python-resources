import openpyxl

workbook = openpyxl.load_workbook("ExcelFile.xlsx")

sheet1 = workbook['Sheet1']

print(sheet1['A2'].value) # print the specific value

print(sheet1.cell(row = 2,column=1).value) # getting value using the extract method

for a,b in sheet1['A1':'B4']:  # to get the more values
    print(a.value,b.value)

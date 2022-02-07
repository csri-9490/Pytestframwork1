import openpyxl
wb=openpyxl.load_workbook("C:\\Users\\srika\\OneDrive\\Desktop\\dt.xlsx")
sheet=wb['Sheet']
data=sheet['B2'].value
data2=wb['Sheet']['B1'].value
# print(data2)
# print(sheet.cell(3,2).value)
wb['Sheet'].title='csrired'
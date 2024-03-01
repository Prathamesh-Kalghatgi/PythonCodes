import openpyxl

# Go to the location of the xl path
book = openpyxl.load_workbook("C:\\Users\\kalgh\\OneDrive\\Desktop\\Team Performance.xlsx")

# To open the xl sheet
sheet = book.active

# To identify the rows and columns in the xl sheet
cell = sheet.cell(row = 2, column = 3)
# To print the values of the cell
print(cell.value)

# unique code error  put double slash

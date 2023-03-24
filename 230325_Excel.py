import pandas
import openpyxl


excel_folder = '/Users/baegono/Desktop/Python/PythonBlog/ExcelFile'

print(pandas.read_excel(excel_folder + '/Programmer.xlsx', sheet_name='Editor'))

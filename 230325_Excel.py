import pandas
import os


excel_folder = '/Users/baegono/Desktop/Python/PythonBlog/ExcelFile'

# print(pandas.read_excel(excel_folder + '/Programmer.xlsx', sheet_name=None).keys())
# print(pandas.read_excel(excel_folder + '/Programmer.xlsx', sheet_name='Editor'))

for path, dirs, files in os.walk(excel_folder):
    for file in files:
        if file.endswith('.xlsx'):
            excel_file = pandas.ExcelFile(path + '/' + file)
            for sheet in excel_file.sheet_names:
                dataframe = excel_file.parse(sheet)
                print(dataframe)
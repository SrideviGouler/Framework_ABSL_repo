from xlrd import open_workbook
file_path=r"C:\Users\sride\PycharmProjects\ABSL_Framework_project\Data\ABSL_data.xls"

def read_locators(sheetname):
    wb = open_workbook(file_path)
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    data = { }
    for i in range(1, used_rows):
        rows = ws.row_values(i)
        data[rows[0]] = (rows[1], rows[2])
    return data

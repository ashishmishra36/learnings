import openpyxl

def get_registration_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    row_dict = {}
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2,values_only=True):
        row_dict = dict(zip(headers,row))
    return row_dict
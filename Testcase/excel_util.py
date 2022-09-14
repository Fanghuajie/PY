import os
from xlutils.copy import copy
import xlrd

from openpyxl import load_workbook

class ExcelUtil:

    row = 1
    def read_excel(self, excel_name):
        book = xlrd.open_workbook(os.getcwd() + "/testcase/testdata/" + excel_name)
        # ExcelUtil.file_path = os.path(excel_name)
        sheet = book.sheets()[0]
        case = []
        for i in range(0, sheet.nrows):
            # 判断过滤掉标注的名称，是名称过滤
            if sheet.row_values(i)[0] == 'URL':
                pass
            else:
                #  如果不是记录出来使用数据
                case.append(sheet.row_values(i))
        # book.save(os.getcwd() + "/testcase/testdata/" + excel_name)
        return case

    def write_excel(self, data):
        row = 1
        old_workbook = xlrd.open_workbook(os.getcwd() + "/testcase/testdata/" + "test_01.xls", 'w+b')
        new_workbook = copy(old_workbook)
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(ExcelUtil.row, 7, data)
        ExcelUtil.row += 1
        new_workbook.save(os.getcwd() + "/testcase/testdata/" + "test_01.xls")

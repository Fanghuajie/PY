import os

import pytest
import requests
# import json
# import xlwt
import xlrd

class Test_get_tq:

    # book = xlrd.open_workbook("D:\\桌面\\Project\\PUNCH\\test data.xls")
    book = xlrd.open_workbook(os.getcwd()+'/testcase/testdata/'+'test data.xls')
    print(os.getcwd())
    def test_g(key, *location):
        url = "https://api.seniverse.com/v3/weather/now.json"
        data = {
            "key": key,
            "location": location
        }
        headers = {
            "Content-Type": "application / json"
        }
        response = requests.request('get', url, params=data, headers=headers)
        return response


    def test_gdata(self):
        sheet1 = Test_get_tq.book.sheets()[0]
        nrs = sheet1.nrows
        ncs = sheet1.ncols
        print(nrs, ncs)
        for i in range(0, nrs):
            for j in range(0, ncs - 1):
                key1 = sheet1.cell(i, j).value
                location1 = sheet1.cell(i, j + 1).value
                con = Test_get_tq.test_g(key1, location1)
                #if con.status_code == 200:
                #print(con.json().get("results")[0].get("location").get("name"))
                #assert con.status_code ==200
                print(con.json())

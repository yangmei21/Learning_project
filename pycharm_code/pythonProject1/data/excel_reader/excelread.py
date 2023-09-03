import xlrd


class excelReader():

    def read(self):
        models = []
        reader = xlrd.open_workbook(r'F:\IDE test文件\account.xlsx')
        print(reader)
        names = reader.sheet_names()
        case_xls = reader.sheet_by_name(names[0])
        list = []
        for i in range(case_xls.nrows):
            smart_list = []
            if i == 0:
                continue
            for j in range(case_xls.ncols):
                smart_list.append(int(case_xls.cell(i, j).value))
            list.append(smart_list)
        print(list)
        return list


e = excelReader()
e.read()

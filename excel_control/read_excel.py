import xlrd

def read_excel(filename):
    book = xlrd.open_workbook(filename)
    sheet1 = book.sheet_by_name("test")
    print(sheet1)
    # 获取行数
    rows = sheet1.nrows
    # 获取列数
    coles =sheet1.ncols
    print("-" * 60)
    # 读取每一列的数据
    # for c in range(coles):
    #     c_values = sheet1.col_values(c)
    #     print(c_values)
    # 读取每一行的数据
    for r in range(rows):
        r_values = sheet1.row_values(r)
        print(r_values)
    # 读取指定单元格数据
    print("-"*60)
    print(sheet1.cell(1,1))
if __name__ == '__main__':
    read_excel("./test.xlsx")
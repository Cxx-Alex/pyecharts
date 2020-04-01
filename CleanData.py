import xlrd

def GetData(file_path):
    WorkBook = xlrd.open_workbook(file_path)
    WorkSheet = WorkBook.sheet_by_name('Sheet1')
    nrows = WorkSheet.nrows
    Excel_Data = []
    for i in range(nrows):
        Excel_Data.append(WorkSheet.row_values(i))
    return Excel_Data

def CleanData():
    Clean_Data = GetData('BI.xlsx')
    CenterName = Clean_Data.pop(0)[2:]
    # TabNames = []
    Data_Dict = {}
    # for item in Clean_Data:
    #     if item[0] not in TabNames:
    #         TabNames.append(item[0])
    for i in range(len(Clean_Data)):
        Data_Dict.setdefault(Clean_Data[i][0],[]).append(Clean_Data[i][1:])
    return CenterName,Data_Dict
    # print(TabName)
    # print(list(Data_Dict.keys()))
    # print(len(Data_Dict))

CleanData()


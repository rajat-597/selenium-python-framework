import openpyxl
from openpyxl.styles import PatternFill

def getRowCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return(sheet.max_row)

def getColumnCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return(sheet.max_column)

def readData(file, sheetName, rownum, columnnum):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(rownum,columnnum).value

def writeData(file, sheetName, rownum, columnnum, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(rownum,columnnum).value = data
    workbook.save(file)

def fillGreenColor(file, sheetName, rownum, columnnum):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    green_fill = PatternFill(start_color="00FF00",end_color="00FF00",fill_type="solid")
    sheet.cell(rownum,columnnum).fill = green_fill
    workbook.save(file)

def fillRedColor(file, sheetName, rownum, columnnum):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    red_fill = PatternFill(start_color="FF0000",end_color="FF0000",fill_type="solid")
    sheet.cell(rownum,columnnum).fill = red_fill
    workbook.save(file)    

import xlwt
#create workbook object
workbook = xlwt.Workbook(encoding="utf-8")
#create worksheet
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')           #write in data
workbook.save('testbook.xls')          #save book
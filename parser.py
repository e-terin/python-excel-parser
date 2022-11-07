from openpyxl import load_workbook
book = load_workbook(filename="book.xlsx")
sheet = book['Лист1']

for i in range (1,4):
    cell = 'A' + str(i)
    print('Значение из ячейки ' + cell + ':' + sheet[cell].value)

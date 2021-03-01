import spreadsheet_maker
import cnf
import contactws_cnf
from pygsheets.datarange import DataRange
from pygsheets.address import Address
from pygsheets.cell import Cell


def findIndexOfEmptyRow(rows):

    # Finding 'i' of row with all cells == ""
    i = 0
    for row in rows:
        for cell in row:
            if(not cell.value == ""):
                break
        else:
            break
        i = i + 1

    return i

# Получает строку и значения каждого столбка в строке
def setRow(row, *cells):

    for i in range(len(row)):
        row[i].value = cells[i]
    return row

# Add any row in any worksheet
# def addRowInWorkSheet(worksheet):
#
#     # All сells
#     rows = DataRange(start='A1',worksheet = worksheet).cells
#     empty_row = rows[findIndexOfEmptyRow(rows)]
#     setRow(empty_row,
#            contactws_cnf.COLUM_ID = id,
#            contactws_cnf.COLUM_PHONE = phone,
#            contactws_cnf.COLUM_DATA_CONTACT = date,
#            contactws_cnf.COLUM_NEW_MSG = msg_last,
#            contactws_cnf.COLUM_DATA_MSG = date_last)

def addShContact(id = "None", phone = "None", date = "None", msg_last = "None", date_last = "None"):

    wrsh = spreadsheet_maker.getWorkSheetbyIndex(cnf.INDEX_CONTACT_WS)

    # All сells
    rows = DataRange(start='A2',worksheet = wrsh).cells
    empty_row = rows[findIndexOfEmptyRow(rows)]
    setRow(empty_row, id, phone, date, msg_last, date_last)

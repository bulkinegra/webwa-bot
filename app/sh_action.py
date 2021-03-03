import spreadsheet_maker
import cnf
import contactws_cnf
from pygsheets.datarange import DataRange
from pygsheets.address import Address
from pygsheets.cell import Cell


def findRowByValueInColum(rows, value, colum):

    for i in range(len(rows)):
        if rows[i][colum].value == value:
            return i

    return -1

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

def setRow(row, *cells):

    if(len(row) < len(cells)):
        for i in range(len(row)):
            row[i].value = cells[i]
    else:
        for i in range(len(cells)):
            row[i].value = cells[i]
    return row

# Add any row in any worksheet
# def addRowInWorkSheet(worksheet):
#
#     # All сells
#     rows = DataRange(start='A1',worksheet = worksheet).cells
#     empty_row = rows[findIndexOfEmptyRow(rows)]
#     setRow(empty_row,
#            contactws_cnf.COLUM_ID = chat_id,
#            contactws_cnf.COLUM_PHONE = phone,
#            contactws_cnf.COLUM_DATA_CONTACT = date,
#            contactws_cnf.COLUM_NEW_MSG = msg_last,
#            contactws_cnf.COLUM_DATA_MSG = date_last)

def addShContact(chat_id = "", phone = "", date = "", msg_last = "", date_last = ""):

    wrsh = spreadsheet_maker.getWorkSheetbyIndex(cnf.INDEX_CONTACT_WS)

    # All сells
    rows = DataRange(start='A2',worksheet = wrsh).cells

    if findRowByValueInColum(rows = rows, value = chat_id, colum = contactws_cnf.COLUM_ID) == -1:
        empty_row = rows[findIndexOfEmptyRow(rows)]
        setRow(empty_row, chat_id, phone, date, msg_last, date_last)
        print("Add contact chat_id = %s, phone = %s, date = %s, msg_last = %s, date_last = %s" % (chat_id, phone, date, msg_last, date_last))
        return True
    else:
        print("contact %s already exists" % chat_id)
        return False

def getMsgFromShBot():

    mesgs = []
    wrsh = spreadsheet_maker.getWorkSheetbyIndex(cnf.INDEX_BOT_WS)
    rows = DataRange(start='A1',worksheet = wrsh).cells
    for row in rows:
        if row[0].value == "TRUE":
            mesgs.append(row[1].value)

    return mesgs

import pygsheets
import numpy as np
import os

name_of_sheet = "Web WA Bot DB"

# Авторизация
try:
    client = pygsheets.authorize(service_file=os.environ["PATH_G_AUTHORIZATION"])
except pygsheets.AuthenticationError:
    client = None
else:

    # Check for exist SpreadSheet
    if(not name_of_sheet in client.spreadsheet_titles):
        # Create new sheet
        client.create(name_of_sheet)
        client
    # Открыли нужный файл
    file_drive = client.open(name_of_sheet)

    contact_sh = file_drive.sheet1  # Лист со списком тех, с кем контактировали
    msg_sh = file_drive.sheet2  # Лист со списком сообщений

def IsContactExisting(contactId):

     # Получаем список контактов

     # Проверяем наличие заданного

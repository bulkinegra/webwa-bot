import pygsheets
import cnf

my_name = cnf.NAME_OF_SPREADSHEET
my_email = cnf.MY_EMAIL
service_file = cnf.SERVICE_FILE

def createWithAccess(client, name_of_sheet, email):

    spsh = client.create(name_of_sheet)

    client.drive.create_permission(
        file_id = spsh.id,
        role = "owner",
        type = "user",
        emailAddress = email,
        transferOwnership = True)

    return spsh

def getClient():

    try:
        return pygsheets.authorize(service_file = service_file)

    except pygsheets.AuthenticationError:
        print("Error of Authentication")
        return None

def getSpreadSheet(client):

    spreadsheet = None

    # Check for exist SpreadSheet
    if(not my_name in client.spreadsheet_titles()):

        print('Tne new spreadsheet - %s was created' % my_name)
        return createWithAccess(client, my_name, my_email)

    else:
        print('%s already exist' % my_name)
        return client.open(my_name)

def getWorkSheetbyIndex(i):
    return getSpreadSheet(getClient()).worksheet(property = 'index', value = i)

import pygsheets
import cnf

my_name = cnf.NAME_OF_SPREADSHEET
my_email = cnf.MY_EMAIL
service_file = cnf.SERVICE_FILE


def create_with_access(client, name_of_sheet, email):
    """

    :param client:
    :param name_of_sheet:
    :param email:
    :return:
    """
    spsh = client.create(name_of_sheet)

    client.drive.create_permission(
        file_id=spsh.id,
        role="owner",
        type="user",
        emailAddress=email,
        transferOwnership=True)

    return spsh


def get_client():
    try:
        return pygsheets.authorize(service_file=service_file)

    except pygsheets.AuthenticationError:
        print("Error of Authentication")
        return None


def get_spread_sheet(client):
    spreadsheet = None

    if my_name in client.spreadsheet_titles():
        print('%s already exist' % my_name)
        return client.open(my_name)
    else:
        print('Tne new spreadsheet - %s was created' % my_name)
        return create_with_access(client, my_name, my_email)


def get_work_sheet_by_index(i, client=get_client()):
    return get_spread_sheet(client).worksheet(property='index', value=i)

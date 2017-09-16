from config import Config
import psycopg2
import psycopg2.extras

def open_database():
    try:
        connection_string = Config.DB_CONNECTION_STR
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print(exception)
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper


@connection_handler
def query_handler(cursor, querystring, escape_tuple=None, result=True):
    cursor.execute(querystring, escape_tuple)
    if result:
        database = cursor.fetchall()
        return database
    else:
        pass


def menu_to_title(titlelist):
    titles = [title.capitalize() for title in titlelist]
    return titles


def header_format(headerlist, zipped=True):
    headers = [header.replace("_", " ").capitalize() for header in headerlist]
    if zipped:
        final_headers = zip(headerlist, headers)
        return final_headers
    return headers

def menu_zip(menulist):
    titles = menu_to_title(menulist)
    menu_titles = zip(menulist, titles)
    return menu_titles
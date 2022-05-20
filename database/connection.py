from mysql import connector

config = {
    'user': 'root',
    'password': PASWORD,
    'host' : HOST',
    'database': 'recipes_db'
}
def create_connection() :
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection fuction: {err.msg}")
    return conn

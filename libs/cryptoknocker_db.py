__author__ = 'trs'

import sqlite3

SQLITE_DB_PATH = "../CryptoKnocker/db.sqlite3"

def get_public_key_path(username):
    '''
    Get public key path of username
    :param username: client username
    :return: public key path
    '''
    QUERY = "SELECT publicKey FROM management_portprofile WHERE userID=?"
    PARAMETERS = (username,)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    result = conn.execute(QUERY, PARAMETERS)
    conn.close()

    return result.fetchone()

def get_user_allowed_ports(username):
    '''
    Get ports assigned to username
    :param username: client username
    :return: list of ports
    '''
    QUERY = "SELECT port FROM management_portprofile WHERE userID=?"
    PARAMETERS = (username,)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    result = conn.execute(QUERY, PARAMETERS)
    conn.close()

    return result.fetchall()

def doesUsernameExist(username):
    '''
    Check if username exist in database
    :param username: client username
    :return: boolean, TRUE or FALSE
    '''

    query = "SELECT EXISTS(select 1 from management_portprofile where userID=? LIMIT 1)"
    parameters = (username,)
    conn = sqlite3.connect(SQLITE_DB_PATH)
    results = conn.execute(query, parameters)

    first_result = results.fetchone()

    if first_result.__contains__(0):
        return False
    else:
        return True

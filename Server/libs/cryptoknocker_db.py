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
    first_result = result.fetchone()
    conn.close()

    return first_result

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
    results = result.fetchall()
    conn.close()

    return results

def get_user_seed(username):
    '''
    Get seed of user name
    :param username: client username
    :return: seed
    '''
    QUERY = "SELECT seed FROM management_portprofile WHERE userID=?"
    PARAMETERS = (username,)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    result = conn.execute(QUERY, PARAMETERS)
    results = result.fetchone()
    conn.close()

    if first_result:
        return first_result[0]
    else:
        return ""

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
    conn.close()

    if first_result.__contains__(0):
        return False
    else:
        return True

def get_port_serviceName(port):
    '''
    Get port's service name
    :param port: int, port number
    :return: String, service name
    '''
    QUERY = "SELECT serviceName from management_portprofile where port=?"
    PARAMETER = (port,)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    result = conn.execute(QUERY,PARAMETER)
    first_result = result.fetchone()
    conn.close()

    if first_result:
        return first_result[0]

def get_port(userID):
    QUERY = "SELECT port from management_portprofile where userID=?"
    PARAMETER = (userID,)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    result = conn.execute(QUERY,PARAMETER)
    first_result = result.fetchone()
    conn.close()

    if first_result:
        return first_result[0]
    else:
        return 8080

def set_port_status(port, status, userID):
    '''
    Set port status to open or close
    :param status: string, status of the port
    :return: boolean, if operation is successful
    '''
    try:
        QUERY = "UPDATE management_portprofile SET status=? where port=? and userID=?"
        PARAMETERS = (status,port, userID)
        conn = sqlite3.connect(SQLITE_DB_PATH)
        conn.execute(QUERY, PARAMETERS)
	conn.commit()
	conn.close()
	
        return True
    except sqlite3.OperationalError as oe:
	print "db problem"
        return False



import socket
import sys
import cPickle as pickle
import time
import random
import os

from libs.crypto import encrypt_RSA, decrypt_RSA, sign_data, verify_sign
from libs.cryptoknocker_db import get_public_key_path, set_port_status, get_user_seed
from libs.port_operations.openServicePort import open_service_port
from libs.port_operations.closeIndividualPort import close_service_port
from libs.logger import PortLog
import netifaces as ni
from libs.pyg2fa import validate

#SERVER = 'localhost'
SERVER = ni.ifaddresses('wlan0')[2][0]['addr']
print SERVER
KNOCK_PORT = 8888

typeOfRequest = ''
user = ''
IPAddrOfClient = ''
otp = ''
nonce = ''
freshNonce = ''

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((SERVER, KNOCK_PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'


def checkAuthencityOfMsg(data_signed, data_enc):
    if (verify_sign(client_public_key, data_signed, data_enc)):
        print "User is authentic"
        #print pickle.loads(data_plain)
        return True
    else:
        print "User is not authentic"
        return False

def checkIPMatches(addr, data):
    if (addr[0] == data[2]):
        print "IP matches"
        return True
    else:
        print "IP do not match: " + addr[0] + " " + data[2]
        return False

def checkOTP(user, otp):
    seed = get_user_seed(user)
    if (validate(seed, int(otp), 4)):
        return True
    else:
        return False

def checkNonceFreshness(nonceA):
    if ( int(time.time()) - nonceA <= 30 ):
        print 'nonce is still fresh'
        return True
    else:
        print 'stale nonce'
        return False

def checkServerNonce(nonceServer, rec_nonceServer):
    if (rec_nonceServer == nonceServer):
        print 'Server nonce is fresh'
        return True
    else:
        print 'Server nonce is stale'
        return False

private_key_file = open("../CryptoKnocker/server_keys/server_private.key", "r")
lines = private_key_file.readlines()
#server_private_key = ""
for line in lines:
	#server_private_key +=line
	pass
#print "\n %s"%(server_private_key)

portlog = PortLog()

while(1) :
    typeOfRequest = ''
    user = ''
    IPAddrOfClient = ''
    otp = ''
    nonce = ''
    serverNonce = ''

    try :
        #first comms
        print "listening for new connections..."
	d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]

        if not data:
            break

        data = pickle.loads(data)
        data_enc = data[0]
        data_signed = data[1]
        data_plain = decrypt_RSA(server_private_key, data_enc)
        data_plain = pickle.loads(data_plain)

        username = data_plain[0]
        client_public_key_path = get_public_key_path(username)[0]
        client_public_key_path = client_public_key_path.encode('utf-8')
        client_public_key_path = '../CryptoKnocker/' + client_public_key_path
        client_public_key_path = os.path.abspath(client_public_key_path)
        client_public_key = open(client_public_key_path, "r").readlines()
	print client_public_key
        isUserAuthentic = checkAuthencityOfMsg(data_signed, data_enc)
        isIPReal = checkIPMatches(addr, data_plain)
        otpclient = data_plain[4]
        isValidOTP = checkOTP(username,otpclient)
        nonceClient = data_plain[5]
        isNonceFresh = checkNonceFreshness(nonceClient)

        #check otp
        if (isUserAuthentic and isIPReal and isNonceFresh):
            #second comms
            #print "second comms"
	    nonceServer = random.randint(100000000, 999999999)
            reply = [nonceClient, nonceServer]
            reply = pickle.dumps(reply)
            reply_enc = encrypt_RSA(client_public_key, reply)
            reply_signed = sign_data(server_private_key, reply_enc)
            reply_payload = [reply_enc, reply_signed]
            reply_payload = pickle.dumps(reply_payload)
            s.sendto(reply_payload , addr)

            #third comms
	    #print "third comms"
            s.settimeout(5.0)
            d = s.recvfrom(1024)
            data = d[0]
            addr = d[1]
            if not data:
                break

            rec_data = pickle.loads(data)
            rec_data_enc = rec_data[0]
            rec_data_signed = rec_data[1]
            rec_data_plain = decrypt_RSA(server_private_key, rec_data_enc)
            rec_data_plain = pickle.loads(rec_data_plain)
            rec_nonceServer = rec_data_plain
            isUserAuthentic = checkAuthencityOfMsg(rec_data_signed, rec_data_enc)
            isServerNonceFresh = checkServerNonce(nonceServer, rec_nonceServer)

            port_operation = data_plain[1]
            client_ip = data_plain[2]
            service_port = data_plain[3]
	    print "client wishes to %s port" %(port_operation)
            if (isUserAuthentic and isServerNonceFresh):
		print "authenticated and fresh nonce"
                if port_operation == "OPEN":
		    print "opening port %s by %s at %s" %(service_port, username, client_ip)
                    open_service_port(client_ip,int(service_port))
                    set_port_status(service_port,"open", username)
                    portlog.log_port_status(service_port, port_operation, username, client_ip)

                elif port_operation == "CLOSE":
		    print "closing port %s by %s at %s" %(service_port, username, client_ip)
                    close_service_port(client_ip, int(service_port))
                    set_port_status(int(service_port),"close", username)
                    portlog.log_port_status(service_port, port_operation, username, client_ip)

                else:
                    print "port operation not found"
                    portlog.log_port_error("port operation not found")

            else:
                print "port not opened" #do nth. silent


    except socket.error, e:
        #sys.exit()
	pass
    '''except TypeError, e:
        #e = sys.exc_info()[0]
        print e
        #print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    except:
        e = sys.exc_info()[0]
        print e
        #print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
'''

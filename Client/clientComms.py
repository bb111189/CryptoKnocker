import time
import cPickle as pickle
import socket

from libs.crypto import encrypt_RSA, decrypt_RSA, sign_data, verify_sign
import ipgetter
from netaddr import *


def checkIPandCovertToPublicIfNeeded(IPAddrOfClient, clientIP, publicIp, serverIP):
    if ((not serverIP.is_private()) and clientIP.is_private()):
        IPAddrOfClient = IPAddress(publicIp)

    return IPAddrOfClient

def checkAuthencityOfMsg(data_signed, data_enc):
    if (verify_sign(server_public_key, data_signed, data_enc)):
        print "Server is authentic"
        return True
    else:
        print "Server is not authentic"
        return False

def checkNonceFreshness(nonce, reply_nonceClient):
    if (reply_nonceClient == nonce):  # not fresh
        print 'nonce is fresh'
        return True
    else:
        return False

def talkToServer(typeOfRequest, user, server, portToOpen, otp, clientPteKeyPath):
    global SERVER, KNOCK_PORT, s, msg, d, data, addr, reply
    SERVER = server
    KNOCK_PORT = 8888
    nonce = int(time.time())
    publicIp = ipgetter.myip()
    IPAddrOfClient = socket.gethostbyname(socket.getfqdn())

    client_private_key = open(clientPteKeyPath, "r").read()

    try:
        clientIP = IPAddress(IPAddrOfClient)
        serverIP = IPAddress(SERVER)
        IPAddrOfClient = checkIPandCovertToPublicIfNeeded(IPAddrOfClient, clientIP, publicIp, serverIP)
    except:
        return False


    # Datagram (udp) socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print 'Socket created'
    except socket.error, msg:
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        #sys.exit()
        return False
    print 'Connecting...'

    try:
        #first comms] C->S
        payload = pickle.dumps([user, typeOfRequest, str(IPAddrOfClient), portToOpen, otp, nonce])
        encrypted_payload = encrypt_RSA(server_public_key, payload)
        signed_payload = sign_data(client_private_key, encrypted_payload)
        final_payload = pickle.dumps([encrypted_payload,signed_payload])
        s.sendto(final_payload, (SERVER, KNOCK_PORT))

        #second comms S-> C
        # receive data from server (data, addr)
        s.settimeout(5.0)
        d = s.recvfrom(1024)

        data = d[0]
        addr = d[1]

        if not data:
            return False

        reply_data = pickle.loads(data)
        reply_data_enc = reply_data[0]
        reply_data_signed = reply_data[1]
        reply_data_plain = decrypt_RSA(client_private_key, reply_data_enc)
        reply_data_plain = pickle.loads(reply_data_plain)
        reply_nonceClient = reply_data_plain[0]
        reply_nonceServer = reply_data_plain[1]

        isServerAuthentic = checkAuthencityOfMsg(reply_data_signed, reply_data_enc)
        isNonceFresh = checkNonceFreshness(nonce, reply_nonceClient)

        if (not (isServerAuthentic and isNonceFresh)):
            print "nonce stale or server not authentic"
            return False

        #third comms C->S
        reply = pickle.dumps(reply_nonceServer)
        reply2_enc = encrypt_RSA(server_public_key, reply)
        reply2_signed = sign_data(client_private_key, reply2_enc)
        reply2_payload = [reply2_enc, reply2_signed ]
        reply2_payload = pickle.dumps(reply2_payload)
        s.sendto(reply2_payload, addr)
        s.close()
        print "connection closed"
        return True

    except socket.timeout, msg:
        print "Connection Timeout"
        return False
    except socket.error, msg:
        print 'Failed during communication. Error Code : ' + str(msg)
        #sys.exit()
        return False


#talkToServer("CLOSED", "JOHN", "127.0.0.1", "21", "123456", "no key") For debugging only.


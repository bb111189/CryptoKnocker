import socket
import sys
import cPickle as pickle
import time
import random
import os

from libs.crypto import encrypt_RSA, decrypt_RSA, sign_data, verify_sign
from libs.cryptoknocker_db import get_public_key_path, set_port_status, get_user_seed, get_port
from libs.port_operations.openServicePort import open_service_port
from libs.port_operations.closeAllPort import block_server_traffic
from libs.port_operations.closeIndividualPort import close_service_port
from libs.logger import PortLog
import netifaces as ni
from libs.pyg2fa import validate
server_private_key = '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAnJdl0MKhHQt8T9h1hefOl+DdBBP1kudIIq+aH7HpBV6aBoIq\nv0MgsNvIzEGtYF52anvAL7A8bWHulcKibP26yx5Jop0liBCZPvl53g4JqSJvhRsc\nVMW0FojpifhJTuiytPbJOACy/Um2DJZVJbnmm+40+QUcW61QLfRAKsNthmKjyeX9\nqAPJhImwie2GHNRDByMCWXDlnb/VS6XTgsZGw+2dqOAX7TRIDGAhumZ6RgJY298f\nxj5XUdQ4vXp9tPc7D1MhIhVR/s/AY/uIVpPgYfbzAZ9jgpMEsLckNcr3n6OstOFy\nMGtPWrRiPzL/SCjl3QkveGuWHAbabu+H9qX7KQIDAQABAoIBAHTlBAl6MUF4YH1O\nbjTe3bc9EmBH8guPAad7BQfiDLyIaVywcO7EUrQT7eqkoKOPAMDuzoILAqD4+Vzs\npcnNA1M7seZlfy36jhuXqqTcP9P1s+BeY6DY0V39KLFpGniAd19l1sIqq3MvQmpV\nEw0NoJwIj5zRduDtGSyk5/3EU498CgKF/06WpkSjWzx2WHA7bqBc/BqV17ZZ5q0Z\n9aZ7zUChYMZRSx+t0R+gzt0gNXvHKt1/UNGJMK1D0AbMfOM39TRiU9cCA6ovI8pm\n/P4DYAVr+yppgf/HbQqdN2C2qQmY2v16zbCOHNxOfv/RNRLyZe4pWksfsIsNiI/p\nn76F+N0CgYEAwVhaBZwiyTsVzBck6Zmj/naaKvcj2fw0nym6VHU519piUu3MfvZQ\nsFGGaiL926UxjoseFC7BeHqV+ou7KF7EoiV3LpyJ+kUkpsW+Rial2dlDLV8wbZHH\naWeRbERS+Whpt3V5qj3Ba19sehtCQWM5j3ENuiO7aWfKZQe7Znh27RcCgYEAz1YB\nx3POWOVrwD0r5GQmFfEzUhfltVEA/+qV/A9jW5tGbrpquEmeWBD94hIpmVEqQX9Z\ntpejtOCWETigL0Uv2RHsWyCHDbZ2M+TbHJnDxBW39di+11U9ggr8kYptCtHqmdCS\niAtM3yZKuxnNtZbS4KQXVflR41vEK8giKIOyAb8CgYEAqxbMqlQs8BbpxezhDBmZ\n5c37xHNndTjZM9LQAHavVdP419t37w11/2BU6kzGiPvYK4PtfPyW1U7cspW9aw7Z\nP4aZvVRmQGG4+h7Xren7Lxgzes3V489xP1OXes/HAM6lZeN9Yuk85A/PxQmkCoqM\nX+Mxu3ptF+vxTI+YBCgrTMcCgYA6bE7WCADWNdd19QbANaQxvKSsdkVpISk5871N\nqHxj3M4s92SJB12SDT+tC1cjd6aDjEIYXIRpvHss4RrqFwHTleRXDURhDdAi8VL4\nrS9nuoL6yJeGD+PkF/pxfGMbkGkd7JLNuPlxS9X1AOFhUN2dJT/aHwX/HeWaPKu7\nZNis+wKBgE5hN04NNSKAia2uJZvEp7ra0/H/6q61egKQ7ru4U/SaqSUy3yC7q6O3\n+7Sf0QQ3+w1cet3ol7zPqzvu0DG/HJYbpu5RThbXS4ePOqLJbfspvShqGCs2F6EG\nQyfAkiOquwyVHQ7ommLC2bQQJORIMHRSCQ+oHIBXKeDbrQvfcXPc\n-----END RSA PRIVATE KEY-----'
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
        if (isUserAuthentic and isIPReal and isNonceFresh and isValidOTP):
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
            service_port = get_port(username)
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

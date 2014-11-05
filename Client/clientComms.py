#Hardcode. client is john
server_public_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnJdl0MKhHQt8T9h1hefO\nl+DdBBP1kudIIq+aH7HpBV6aBoIqv0MgsNvIzEGtYF52anvAL7A8bWHulcKibP26\nyx5Jop0liBCZPvl53g4JqSJvhRscVMW0FojpifhJTuiytPbJOACy/Um2DJZVJbnm\nm+40+QUcW61QLfRAKsNthmKjyeX9qAPJhImwie2GHNRDByMCWXDlnb/VS6XTgsZG\nw+2dqOAX7TRIDGAhumZ6RgJY298fxj5XUdQ4vXp9tPc7D1MhIhVR/s/AY/uIVpPg\nYfbzAZ9jgpMEsLckNcr3n6OstOFyMGtPWrRiPzL/SCjl3QkveGuWHAbabu+H9qX7\nKQIDAQAB\n-----END PUBLIC KEY-----'
client_private_key = '-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAkSq3EDTiGCnHM8nnwagJsmqnqtgzsja8wKX6P2gr2NcfUtnv\nDW5jelmfnTuRLwCYcCQ6gpjo5M8KMeLdcbl6zB+zadTH5FVAj7DJHiHszx8lBGLL\nVOjWtR9OvucF13PCZ18SqCvld1WgxStSQWHtPsoGAbFdMg8UVRjnQW8MM1tNnI8Z\nsyFfzXHQTZr4Jn77rw8CZmMgHT5Bd5quE6An+mw1HFo2Tkao9ED2zIdU9JDNKvKE\nrQrnDOHyrdWLcYZivrPhTYxqFrbkDRhKF93Y20xfLq3vgwWv19saBoNTkMrvBETT\nYCM0bw3Zm6z0PxcKFLgVMJHtuoFmnmgLxQnedwIDAQABAoIBAChV+BvWteQE58bq\nGS1kJZ2fqQr9nA+uye+1rr0jkttjmt6Ik7XlsFp0wLcNsB+hSLoQNvnGxx+cr7aA\n1QsegJJrVIzZhNlbHt9OPfPTdVtvyfdYBCuJru8Qze6ZfrQJBEF411RHLjFkZ5Gh\noe9s6GED/XtG7yBTtFCY5Nj3pCo4jyhV2kNxEqNe3BHTQfZpTMFPhnAGvgd5YKo2\nxcRA7TyGfW6nmyKr1KnlnrPIXzcNRBBvzRz7n5Nq8noA8M4whV6la2Bs4GAYZ+MD\n6JmZp2yCPdrJnchAolmAYw8IFkpXq6z9YeYgroDPcE48aNMkMxjCHhdFuyptEF/L\ngcBnwmECgYEAtxkp+BPJmsa/Y5yfrdT5skFv9TrT1TcN3gwa7KOUY7XYIAKse5UY\nzXZtMNdc2zeRBneOEJDYYAVgYQKdaohYK64B1em+xCw/ZiQrIVnbeRD3d7uYqHof\npvaz191QJNLHutxnBnV5+wC8E2pxn5v3znA7eSct36RMF0wr1j0Qcd8CgYEAyvdG\n127hJTTJboJfwNV0CPoPEh/8v797JeD6M/EBmH+SDwLVYGGjnkkwdvV8+7NSAEJd\nxKcVBoXMODeVqRdF1s5p+1ZqlSxGvPuu1JjAXtw36TTXPqE6PCJCuGYOTaoM51UX\nQgdGf6xCvoyZnkCWcXjVP6eavDzWQ92jWLS+FmkCgYAp8kPhJ3daVAnooisawd3q\nbn9dqPp6sEAnDJLmf5sxNKmsu7AUJ9Yky+q787q8JgC9gIo1VVmctd6cmuLBUzcP\n2q9k+EXR32ku1z5iR5m2JKLs9TdF8aRqtb4ByBviM7+6GWAo5KTrUgHEWPBq5mph\nCuk1GjqyL4uXEsZAMIEh9QKBgHvMVBN3eDCff/W94/XUvI/1Jlgh1qKGgvDZxwMD\nj7uapFYvnkLJi2kyrzMADZnhCLVLxbH7T6HI3oWzsb+PiHO7N32seho/BW6j/UGD\nYmL548iFCH0VDlY7d4LODQ9mF7TKfAM0ONYLFjLvw4t5Tcosr7XB32nNmcuPVuD2\nbbNxAoGAQxRpOv8M88YRYt+UqmIdAs6pq7AKicadfWabotb1VkRC/te6ZJEpT8eq\nqPJSU6TlFaIyJjtMs43vy9EaygCmnSqzrRwhAoX95W4QF0j9mRd69wykRyj/1D6d\nehDEh5j9yWsKDM+oy1Gf4hPJkdCrYn/sRIVQjMDBrG9LiLou7SE=\n-----END RSA PRIVATE KEY-----'

import sys
from crypto import encrypt_RSA, decrypt_RSA, sign_data, verify_sign
import time
import ipgetter
import cPickle as pickle
import ipaddr
import socket, struct
from netaddr import *
from Crypto.PublicKey import RSA

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

    clientIP = IPAddress(IPAddrOfClient)
    serverIP = IPAddress(SERVER)
    IPAddrOfClient = checkIPandCovertToPublicIfNeeded(IPAddrOfClient, clientIP, publicIp, serverIP)

    # Datagram (udp) socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print 'Socket created'
    except socket.error, msg:
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        #sys.exit()
        return False
    print 'Connected'

    #first comms] C->S
    payload = pickle.dumps([user, typeOfRequest, str(IPAddrOfClient), portToOpen, otp, nonce])
    encrypted_payload = encrypt_RSA(server_public_key, payload)
    signed_payload = sign_data(client_private_key, encrypted_payload)
    final_payload = pickle.dumps([encrypted_payload,signed_payload])
    s.sendto(final_payload, (SERVER, KNOCK_PORT))

    #second comms S-> C
    # receive data from server (data, addr)
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

#talkToServer("CLOSED", "JOHN", "127.0.0.1", "21", "123456", "no key") For debugging only.


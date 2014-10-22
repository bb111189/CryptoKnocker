# Open server service
# Require client's ip address, desired port

import sys
import argparse
import iptc

parser = argparse.ArgumentParser(description='open server service.')
parser.add_argument("clientIP", help="client's ip that you want to allow", type=str)
parser.add_argument("servicePort", help="server service that you need access", type=int)
args = parser.parse_args()
print(args.clientIP)
print(args.servicePort)

CLIENT_IP = args.clientIP
SERVICE_PORT = args.servicePort

def hasRuleExistInFilter():
	chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
	for rule in chain.rules:
		ipList = (rule.src).split('/')
		currSrcIP = ipList[0]
		for match in rule.matches:
			currAllowedPort = int(match.dport)
			currTarget = rule.target.name
		if (currSrcIP == CLIENT_IP and currAllowedPort == SERVICE_PORT and currTarget == "ACCEPT"):
			return True
		else:
			return False

def openServicePort():
	if (hasRuleExistInFilter() == True):
		return;
	else:
		rule = iptc.Rule()
		rule.in_interface = "wlan0"
		rule.out_interface = "eth0"
		rule.src = CLIENT_IP
		rule.protocol = "tcp"
		match = iptc.Match(rule, "tcp")
		match.dport = "%d" % SERVICE_PORT
		rule.add_match(match)
		rule.target = iptc.Target(rule, "ACCEPT")
		chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
		chain.insert_rule(rule)
	return;

openServicePort()
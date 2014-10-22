# Pi Router
# Filter all incoming connections

import iptc

EXTERNAL_IN_PORT = 8888
INTERNAL_IN_PORT = 8000

# Add rule to INPUT Filter
def addInputRuleToFilter( rule ):
	chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)
    return;

# Block all incoming from external
def blockExternalInTraffic():
	rule = iptc.Rule()
	rule.in_interface = "wlan0"
	rule.out_interface = "eth0"
	rule.target = iptc.Target(rule, "DROP")
	addInputRuleToFilter(rule)
	return;

# Allow client to send initial packet to server
def allowExternalOnePort():
	rule = iptc.Rule()
	rule.in_interface = "wlan0"
	rule.out_interface = "eth0"
	rule.protocol = "tcp"
	match = iptc.Match(rule, "tcp")
	match.dport = "%d" % EXTERNAL_IN_PORT
	rule.add_match(match)
	rule.target = iptc.Target(rule, "ACCEPT")
	addInputRuleToFilter(rule)
	return;

# Allow loopback
def allowLoopback():
	rule = iptc.Rule()
	rule.in_interface = "lo"
	rule.target = iptc.Target(rule, "ACCEPT")
	addInputRuleToFilter(rule)
	return;

# Allow internal server web UI
def allowServerTraffic():
	rule = iptc.Rule()
	rule.in_interface = "eth0"
	rule.protocol = "tcp"
	match = iptc.Match(rule, "tcp")
	match.dport = "%d" % INTERNAL_IN_PORT
	rule.add_match(match)
	rule.target = iptc.Target(rule, "ACCEPT")
	addInputRuleToFilter(rule)
	return;

blockExternalInTraffic()
allowLoopback()
allowExternalOnePort()
allowServerTraffic()
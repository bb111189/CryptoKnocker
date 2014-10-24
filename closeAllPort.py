# Pi Router
# Filter all incoming connections
import iptc

EXTERNAL_IN_PORT = 8888
INTERNAL_IN_PORT = 8000


# Add rule to INPUT Filter
def add_input_rule_to_filter(rule):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)


# Block all incoming from external
def block_ext_in_traffic():
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "eth0"
    rule.target = iptc.Target(rule, "DROP")
    add_input_rule_to_filter(rule)


# Allow client to send initial packet to server
def allow_ext_single_port():
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "eth0"
    rule.protocol = "tcp"
    match = iptc.Match(rule, "tcp")
    match.dport = "%d" % EXTERNAL_IN_PORT
    rule.add_match(match)
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)


# Allow loopback
def allow_loopback():
    rule = iptc.Rule()
    rule.in_interface = "lo"
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)


# Allow internal server web UI
def allow_server_traffic():
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    rule.protocol = "tcp"
    match = iptc.Match(rule, "tcp")
    match.dport = "%d" % INTERNAL_IN_PORT
    rule.add_match(match)
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)

block_ext_in_traffic()
allow_loopback()
allow_ext_single_port()
allow_server_traffic()
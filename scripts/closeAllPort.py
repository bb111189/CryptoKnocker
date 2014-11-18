# Pi Router
# Filter all incoming connections
import iptc

EXTERNAL_IN_PORT = 8888
INTERNAL_IN_PORT1 = 8000
INTERNAL_IN_PORT2 = 22
INTERNAL_IN_PORT3 = 8080


# Add rule to INPUT Filter
def add_input_rule_to_filter(rule):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)
    return


# Add rule to choice of filter
def add_rule_to_filter(rule, filter_choice):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), filter_choice)
    chain.insert_rule(rule)
    return


# Block all incoming from external
def block_ext_in_traffic():
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "any"
    rule.target = iptc.Target(rule, "DROP")
    add_input_rule_to_filter(rule)
    add_rule_to_filter(rule, "OUTPUT")
    return


# Forward traffic from wlan0 to eth0
def forward_wlan_traffic():
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "eth0"
    rule.target = iptc.Target(rule, "ACCEPT")
    add_rule_to_filter(rule, "FORWARD")
    return


# Allow client to send initial packet to server
def allow_ext_single_port():
    rule = iptc.Rule()
    rule.in_interface = "any"
    rule.out_interface = "any"
    rule.protocol = "udp"
    match = iptc.Match(rule, "udp")
    match.dport = "%d" % EXTERNAL_IN_PORT
    rule.add_match(match)
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)
    add_rule_to_filter(rule, "OUTPUT")
    return


# Allow loopback
def allow_loopback():
    rule = iptc.Rule()
    rule.in_interface = "lo"
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)
    return


# Allow internal server web UI
def allow_server_traffic(internal_port):
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    rule.protocol = "tcp"
    match = iptc.Match(rule, "tcp")
    match.dport = "%d" % internal_port
    rule.add_match(match)
    rule.target = iptc.Target(rule, "ACCEPT")
    add_input_rule_to_filter(rule)
    add_rule_to_filter(rule, "OUTPUT")
    return


block_ext_in_traffic()
#forward_wlan_traffic()
#allow_loopback()
allow_ext_single_port()
allow_server_traffic(INTERNAL_IN_PORT1)
allow_server_traffic(INTERNAL_IN_PORT2)
allow_server_traffic(INTERNAL_IN_PORT3)

# Allows the admin to close individual opened ports from django
# Delete rule from table.filter chain input
# Add the deny rule


import iptc


# Delete the input rule from table
def delete_identical_rule(client_ip, service_port):
    chain_names = ["INPUT", "OUTPUT"]

    for chain_name in chain_names:
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), chain_name)
        for rule in chain.rules:
            ipList = rule.src.split('/')
            currSrcIP = ipList[0]
            for match in rule.matches:
                currAllowedPort = int(match.dport)
                currTarget = rule.target.name
            if currSrcIP == client_ip and currAllowedPort == service_port and currTarget == "ACCEPT":
                chain.delete_rule(rule)


# Delete any forms of drop from input table
def delete_existing_drop(client_ip, service_port):

    chain_names = ["INPUT", "OUTPUT"]

    for chain_name in chain_names:
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), chain_name)
        for rule in chain.rules:
            ipList = rule.src.split('/')
            currSrcIP = ipList[0]
            for match in rule.matches:
                currAllowedPort = int(match.dport)
                currTarget = rule.target.name
            if currSrcIP == client_ip and currAllowedPort == service_port and currTarget == "DROP":
                chain.delete_rule(rule)


def add_deny_rule(client_ip, service_port):
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "eth0"
    rule.src = client_ip
    rule.protocol = "udp"
    match = iptc.Match(rule, "udp")
    match.dport = "%d" % service_port
    rule.add_match(match)
    rule.target = iptc.Target(rule, "DROP")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)

    chain_output = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
    chain_output.insert_rule(rule)
    return


def close_service_port(client_ip, service_port):
    delete_existing_drop(client_ip, service_port)
    delete_identical_rule(client_ip, service_port)
    add_deny_rule(client_ip, service_port)
    return



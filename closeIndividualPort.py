# Allows the admin to close individual opened ports from django
# Delete rule from table.filter chain input
# Add the deny rule


import iptc


# Delete the input rule from table
def delete_identical_rule(client_ip, service_port):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    for rule in chain.rules:
        ipList = rule.src.split('/')
        currSrcIP = ipList[0]
        for match in rule.matches:
            currAllowedPort = int(match.dport)
        if currSrcIP == client_ip and currAllowedPort == service_port:
            chain.delete_rule(rule)


def add_deny_rule(client_ip, service_port):
    rule = iptc.Rule()
    rule.in_interface = "wlan0"
    rule.out_interface = "eth0"
    rule.src = client_ip
    rule.protocol = "tcp"
    match = iptc.Match(rule, "tcp")
    match.dport = "%d" % service_port
    rule.add_match(match)
    rule.target = iptc.Target(rule, "DROP")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)


def close_service_port(client_ip, service_port):
    delete_identical_rule(client_ip, service_port)
    add_deny_rule(client_ip, service_port)



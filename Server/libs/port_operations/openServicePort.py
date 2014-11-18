# Open server service
# Require client's ip address, desired port

# import argparse
import iptc

# parser = argparse.ArgumentParser(description='open server service.')
# parser.add_argument("clientIP", help="client's ip that you want to allow", type=str)
# parser.add_argument("servicePort", help="server service that you need access", type=int)
# args = parser.parse_args()
# print(args.clientIP)
# print(args.servicePort)

# CLIENT_IP = args.clientIP
# SERVICE_PORT = args.servicePort


def delete_drop_rule(client_ip, service_port):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    for rule in chain.rules:
        ipList = rule.src.split('/')
        currSrcIP = ipList[0]
        for match in rule.matches:
            currAllowedPort = int(match.dport)
            currTarget = rule.target.name
        if currSrcIP == client_ip and currAllowedPort == service_port and currTarget == "DROP":
            chain.delete_rule(rule)


def has_rule_exist_in_filter(client_ip, service_port):

    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    for rule in chain.rules:
        ipList = rule.src.split('/')
        currSrcIP = ipList[0]
        for match in rule.matches:
            currAllowedPort = int(match.dport)
            currTarget = rule.target.name
        if currSrcIP == client_ip and currAllowedPort == service_port and currTarget == "ACCEPT":
            return True
        else:
            continue
    return False


def open_service_port(client_ip, service_port):
    isRuleExist = has_rule_exist_in_filter(client_ip, service_port)
    if isRuleExist:
        return
    else:
        delete_drop_rule(client_ip, service_port)
        rule = iptc.Rule()
        rule.in_interface = "wlan0"
        rule.out_interface = "eth0"
        rule.src = client_ip
        rule.protocol = "udp"
        match = iptc.Match(rule, "udp")
        match.dport = "%d" % service_port
        rule.add_match(match)
        rule.target = iptc.Target(rule, "ACCEPT")
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        chain.insert_rule(rule)
    return
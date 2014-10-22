# Pi Router
# Filter all incoming connections

import iptc

# Add rule to INPUT Filter
def addInputRuleToFilter( rule ):
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        chain.insert_rule(rule)
        return;

# Block all incoming
rule = iptc.Rule()
rule.target = iptc.Target(rule, "DROP")
addInputRuleToFilter(rule)

# Allow loopback
rule = iptc.Rule()
rule.in_interface = "lo"
rule.target = iptc.Target(rule, "ACCEPT")
addInputRuleToFilter(rule)

#!/usr/bin/python3

from oc_system import openconfig_system
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

# Config variables
HOSTNAME = 'DC1_SPINE1'
DNS_SERVERS = [
    "1.1.1.1",
    "8.8.8.8"
]
NTP_SERVERS = [
    "time.google.com",
    "time.cloudflare.com"
]

# Object
oc_sys = openconfig_system()

# hostname
oc_sys.system.config.hostname = HOSTNAME
oc_sys.system.config.domain_name = 'aristanetworks.com'

# DNS
for dns_srv in DNS_SERVERS:
    dns_entry = oc_sys.system.dns.servers.server.add(dns_srv)
    dns_entry.config.address = dns_srv

# NTP
for ntp_srv in NTP_SERVERS:
    ntp_entry = oc_sys.system.ntp.servers.server.add(ntp_srv)
    ntp_entry.config.address = ntp_srv
    ntp_entry.config.iburst = True
    if "google" in ntp_srv:
        ntp_entry.config.prefer = True

pp(pybindJSON.dumps(oc_sys))

with open("./{}_config.json".format(HOSTNAME), "w") as fobj:
    fobj.write(pybindJSON.dumps(oc_sys, mode='ietf'))

fobj.close()
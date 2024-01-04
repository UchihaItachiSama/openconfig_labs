#!/usr/bin/python3

from oc_intf import openconfig_interfaces
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

dc1 = {
    "spine1": {
        "Ethernet1": {
            "ipv4": "172.31.255.0",
            "mask": "24",
            "descr": "P2P_LINK_TO_DC1_LEAF1_Ethernet1"
        },
        "Ethernet2": {
            "ipv4": "172.31.255.2",
            "mask": "24",
            "descr": "P2P_LINK_TO_DC1_LEAF2_Ethernet1"
        }
    },
    "leaf1": {
        "Ethernet1": {
            "ipv4": "172.31.255.1",
            "mask": "24",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet1"
        }
    },
    "leaf2": {
        "Ethernet1": {
            "ipv4": "172.31.255.3",
            "mask": "24",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet2"
        }
    }
}

for switch,interfaces in dc1:
    oc = openconfig_interfaces()
    for intf, value in interfaces:
        oc.interfaces.interfaces.add(intf)
        oc.interfaces.interfaces[intf].config.enabled = 'true'
        oc.interfaces.interfaces[intf].config.description = value["descr"]
        oc.interfaces.interfaces[intf].subinterfaces.subinterface.add(0)
        oc.interfaces.interfaces[intf].subinterfaces.subinterface[0].ipv4.config.enabled = 'true'
        oc.interfaces.interfaces[intf].subinterfaces.subinterface[0].ipv4.addresses.address.add(ip=value["ipv4"])
        oc.interfaces.interfaces[intf].subinterfaces.subinterface[0].ipv4.addresses.address[value["ipv4"]].config.ip = 


pp(pybindJSON.dumps(oc_sys))

with open("./{}_hostname.json".format(HOSTNAME), "w") as fobj:
    fobj.write(pybindJSON.dumps(oc_sys, mode="ietf"))

fobj.close()
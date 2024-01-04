#!/usr/bin/python3

from oc_intf import openconfig_interfaces
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

dc1 = {
    "spine1": {
        "Ethernet1": {
            "ipv4": "172.31.255.0",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_LEAF1_Ethernet1"
        },
        "Ethernet2": {
            "ipv4": "172.31.255.2",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_LEAF2_Ethernet1"
        }
    },
    "leaf1": {
        "Ethernet1": {
            "ipv4": "172.31.255.1",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet1"
        }
    },
    "leaf2": {
        "Ethernet1": {
            "ipv4": "172.31.255.3",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet2"
        }
    }
}

for switch,interfaces in dc1.items():
    oc = openconfig_interfaces()
    for intf, value in interfaces.items():
        oc.interfaces.interface.add(intf)
        oc.interfaces.interface[intf].config.enabled = 'true'
        oc.interfaces.interface[intf].config.description = value["descr"]
        oc.interfaces.interface[intf].subinterfaces.subinterface.add(0)
        oc.interfaces.interface[intf].subinterfaces.subinterface[0].ipv4.config.enabled = 'true'
        oc.interfaces.interface[intf].subinterfaces.subinterface[0].ipv4.addresses.address.add(ip=value["ipv4"])
        oc.interfaces.interface[intf].subinterfaces.subinterface[0].ipv4.addresses.address[value["ipv4"]].config.ip = value["ipv4"]
        oc.interfaces.interface[intf].subinterfaces.subinterface[0].ipv4.addresses.address[value["ipv4"]].config.prefix_length = value["mask"]
        #oc.interfaces.interface[intf].subinterfaces.subinterface[0].ipv4.addresses.address[value["ipv4"]].config.type = 'PRIMARY'
    #pp(pybindJSON.dumps(oc))
    with open("./{}_config.json".format(switch), "w") as fobj:
        fobj.write(pybindJSON.dumps(oc, mode="ietf"))
    fobj.close()
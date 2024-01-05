#!/usr/bin/python3

#pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -o ./oc_net_instance.py -p ../yang_modules/ ../yang_modules/openconfig-network-instance*.yang

from oc_net_instance import openconfig_network_instance
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

dc1 = {
    "spine1": {
        "asn": "65001",
        "peers": {
            "172.31.255.1": {
                "peer_as": "65101"
            },
            "172.31.255.3": {
                "peer_as": "65102"
            }
        }
    },
    "leaf1": {
        "asn": "65001",
        "peers": {
            "172.31.255.0": {
                "peer_as": "65001"
            }
        }
    },
    "leaf2": {
        "asn": "65001",
        "peers": {
            "172.31.255.2": {
                "peer_as": "65001"
            }
        }
    }
}

oc = openconfig_network_instance()

vrf = oc.network_instances.network_instance.add('default')
proto = vrf.protocols.protocol.add(identifier='BGP', name='BGP')
proto.bgp.global_.config.as_ = dc1["spine1"]["asn"]
proto.bgp.global_.config.router_id = "192.168.255.1"
neighbor = proto.bgp.neighbors.neighbor.add("172.31.255.1")
neighbor.config.enabled = True
neighbor.config.peer_as = "65101"
neighbor.config.description = "DC1_LEAF1_Ethernet1"
neighbor.config.neighbor_address = "172.31.255.1"

with open("./{}_BGP.json".format('spine1'), "w") as fobj:
    fobj.write(pybindJSON.dumps(oc, mode="ietf"))
fobj.close()
#!/usr/bin/python3

from oc_net_instance import openconfig_network_instance
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

dc1 = {
    "spine1": {
        "asn": "65001",
        "routerId": "192.168.255.1",
        "peers": {
            "172.31.255.1": {
                "peer_as": "65101",
                "descr": "DC1_LEAF1_Ethernet1"
            },
            "172.31.255.3": {
                "peer_as": "65102",
                "descr": "DC1_LEAF2_Ethernet1"
            }
        }
    },
    "leaf1": {
        "asn": "65101",
        "routerId": "192.168.255.2",
        "peers": {
            "172.31.255.0": {
                "peer_as": "65001",
                "descr": "DC1_SPINE1_Ethernet1"
            }
        }
    },
    "leaf2": {
        "asn": "65102",
        "routerId": "192.168.255.3",
        "peers": {
            "172.31.255.2": {
                "peer_as": "65001",
                "descr": "DC1_SPINE1_Ethernet2"
            }
        }
    }
}

for switch, bgp_config in dc1.items():
    oc = openconfig_network_instance()
    vrf = oc.network_instances.network_instance.add('default')
    proto = vrf.protocols.protocol.add(identifier='BGP', name='BGP')
    proto.bgp.global_.config.as_ = dc1[switch]["asn"]
    proto.bgp.global_.config.router_id = dc1[switch]["routerId"]

    for bgp_peer, peer_config in bgp_config["peers"].items():
        neighbor = proto.bgp.neighbors.neighbor.add(bgp_peer)
        neighbor.config.neighbor_address = bgp_peer
        neighbor.config.enabled = True
        neighbor.config.peer_as = peer_config["peer_as"]
        neighbor.config.description = peer_config["descr"]
    with open("./{}_bgp_config.json".format(switch), "w") as fobj:
        fobj.write(pybindJSON.dumps(oc, mode="ietf"))
    fobj.close()
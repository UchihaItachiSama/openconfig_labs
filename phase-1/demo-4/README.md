# Demo-4

In this demo, we will configure BGP peering between the leaf and spine switches in the `ceos-lab` lab.

## Requirements

* Install Pyang and Pyangbind

```shell
python3 -m pip install pyang
python3 -m pip install pyangbind
```

* To confirm if already installed:

```shell
python3 -m pip freeze | egrep "pyang|pyangbind"
```

* `containerlab` and `docker` installed
* Arista cEOS-Lab image installed

```shell
$ docker images | egrep "IMAGE|ceosimage"

REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
ceosimage                4.30.1F      72e796e3929e   3 weeks ago     2.44GB
```

## Steps

### Using JSON and gNMIc

* Start the `ceos-lab` lab

```shell
cd openconfig-labs/phase-1/ceos-lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `demo-4` directory

```shell
cd openconfig-labs/phase-1/demo-4
```

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -o ./oc_net_instance.py -p ../yang_modules/ ../yang_modules/openconfig-network-instance.yang
```

* The above command will generate the Python module `oc_net_instance.py` from the `openconfig-network-instance.yang` file. Run this command to verify the file.

```shell
ls oc_net_instance.py
```

* Next, we will use this Python module to generate the JSON file

```python
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
```

* Execute the above Python file and we can now see the JSON files with the BGP models are generated.

```shell
$ python3 bgp_demo.py

---

leaf1_bgp_config.json
leaf2_bgp_config.json
spine1_bgp_config.json

---

$ cat spine1_bgp_config.json | jq
{
  "openconfig-network-instance:network-instances": {
    "network-instance": [
      {
        "name": "default",
        "protocols": {
          "protocol": [
            {
              "identifier": "BGP",
              "name": "BGP",
              "bgp": {
                "global": {
                  "config": {
                    "as": 65001,
                    "router-id": "192.168.255.1"
                  }
                },
                "neighbors": {
                  "neighbor": [
                    {
                      "neighbor-address": "172.31.255.1",
                      "config": {
                        "neighbor-address": "172.31.255.1",
                        "enabled": true,
                        "peer-as": 65101,
                        "description": "DC1_LEAF1_Ethernet1"
                      }
                    },
                    {
                      "neighbor-address": "172.31.255.3",
                      "config": {
                        "neighbor-address": "172.31.255.3",
                        "enabled": true,
                        "peer-as": 65102,
                        "description": "DC1_LEAF2_Ethernet1"
                      }
                    }
                  ]
                }
              }
            }
          ]
        }
      }
    ]
  }
}
```

* Using gNMIc we will configure the BGP on the leaf and spine devices

```shell
gnmic -a 172.100.100.2:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file spine1_bgp_config.json

gnmic -a 172.100.100.3:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file leaf1_bgp_config.json

gnmic -a 172.100.100.4:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file leaf2_bgp_config.json
```

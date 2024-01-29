# Demo-3

In this demo, we will configure the L3 interfaces on the leaf and spine switches in the `ceos-lab` lab.

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

* Navigate to the `demo-3` directory

```shell
cd openconfig-labs/phase-1/demo-3
```

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_intf.py ../yang_modules/openconfig-interfaces.yang ../yang_modules/openconfig-if-ip.yang
```

* The above command will generate the Python module `oc_intf.py` from the `openconfig-interfaces.yang` file. Run this command to verify the file.

```shell
ls oc_intf.py
```

* Next, we will use this Python module to generate the JSON file

```python
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
        },
        "Loopback1": {
          "ipv4": "192.168.255.1",
          "mask": "32",
          "descr": "EVPN_Overlay_Peering",
        }
    },
    "leaf1": {
        "Ethernet1": {
            "ipv4": "172.31.255.1",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet1"
        },
        "Loopback1": {
          "ipv4": "192.168.255.2",
          "mask": "32",
          "descr": "EVPN_Overlay_Peering",
        }
    },
    "leaf2": {
        "Ethernet1": {
            "ipv4": "172.31.255.3",
            "mask": "31",
            "descr": "P2P_LINK_TO_DC1_SPINE1_Ethernet2"
        },
        "Loopback1": {
          "ipv4": "192.168.255.3",
          "mask": "32",
          "descr": "EVPN_Overlay_Peering",
        }
    }
}

for switch,interfaces in dc1.items():
    oc = openconfig_interfaces()
    for intf, value in interfaces.items():
        oc.interfaces.interface.add(intf)
        eth_intf = oc.interfaces.interface[intf]
        eth_intf.config.enabled = True
        eth_intf.config.description = value["descr"]
        eth_intf.config.name = intf
        eth_intf.subinterfaces.subinterface.add(0)
        sub_intf0 = eth_intf.subinterfaces.subinterface[0]
        sub_intf0.ipv4.config.enabled = True
        sub_intf0.ipv4.addresses.address.add(value["ipv4"])
        sub_intf0.ipv4.addresses.address[value["ipv4"]].config.ip = value["ipv4"]
        sub_intf0.ipv4.addresses.address[value["ipv4"]].config.prefix_length = value["mask"]
    #pp(pybindJSON.dumps(oc))
    with open("./{}_config.json".format(switch), "w") as fobj:
        fobj.write(pybindJSON.dumps(oc, mode="ietf"))
    fobj.close()
```

* Execute the above python file and we can now see the JSON files with the interface models are generated.

```shell
$ python3 interface_demo.py

---

leaf1_config.json
leaf2_config.json
spine1_config.json

---

$ cat spine1_config.json | jq
{
  "openconfig-interfaces:interfaces": {
    "interface": [
      {
        "name": "Ethernet1",
        "config": {
          "name": "Ethernet1",
          "description": "P2P_LINK_TO_DC1_LEAF1_Ethernet1",
          "enabled": true
        },
        "subinterfaces": {
          "subinterface": [
            {
              "index": "0",
              "openconfig-if-ip:ipv4": {
                "addresses": {
                  "address": [
                    {
                      "ip": "172.31.255.0",
                      "config": {
                        "ip": "172.31.255.0",
                        "prefix-length": 31
                      }
                    }
                  ]
                },
                "config": {
                  "enabled": true
                }
              }
            }
          ]
        }
      },
      {
        "name": "Ethernet2",
        "config": {
          "name": "Ethernet2",
          "description": "P2P_LINK_TO_DC1_LEAF2_Ethernet1",
          "enabled": true
        },
        "subinterfaces": {
          "subinterface": [
            {
              "index": "0",
              "openconfig-if-ip:ipv4": {
                "addresses": {
                  "address": [
                    {
                      "ip": "172.31.255.2",
                      "config": {
                        "ip": "172.31.255.2",
                        "prefix-length": 31
                      }
                    }
                  ]
                },
                "config": {
                  "enabled": true
                }
              }
            }
          ]
        }
      },
      {
        "name": "Loopback1",
        "config": {
          "name": "Loopback1",
          "description": "EVPN_Overlay_Peering",
          "enabled": true
        },
        "subinterfaces": {
          "subinterface": [
            {
              "index": "0",
              "openconfig-if-ip:ipv4": {
                "addresses": {
                  "address": [
                    {
                      "ip": "192.168.255.1",
                      "config": {
                        "ip": "192.168.255.1",
                        "prefix-length": 32
                      }
                    }
                  ]
                },
                "config": {
                  "enabled": true
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

* Using gNMIc we will configure the interfaces

```shell
gnmic -a 172.100.100.2:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file spine1_config.json

gnmic -a 172.100.100.3:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file leaf1_config.json

gnmic -a 172.100.100.4:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file leaf2_config.json
```

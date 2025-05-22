# pyangbind demo

- [pyangbind demo](#pyangbind-demo)
  - [Requirements](#requirements)
  - [Generating python classes from YANG module](#generating-python-classes-from-yang-module)
    - [Before configuration](#before-configuration)
    - [Configuration](#configuration)
    - [After configuration](#after-configuration)
    - [Switch CLI](#switch-cli)

In this demo we will be using [Pyangbind](https://github.com/robshakir/pyangbind) to generate a Python class hierarchy from a YANG model and configuring a Arista cEOS-Lab node.

## Requirements

Confirm the following packages are installed, else install them using `pip`

```shell
python3 -m pip freeze | egrep "pyang|pyangbind"
```

Start the [arista-ceos](../../labs/arista-ceos/) lab using containerlab.

## Generating python classes from YANG module

```shell
pyang --plugindir $PYBINDPLUGIN -f pybind -p demos/public-yang -o demos/pyangbind-demo/oc_system.py demos/public-yang/openconfig-system.yang
```

The above command will generate the Python module `oc_system.py` from the [openconfig-system.yang](../public-yang/openconfig-system.yang) file.

Next we will create a data instance using the class object from oc_system in `config-demo.py` below:

```python
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
```

Execute the `config-demo.py` file and we can now see the JSON file is generated.

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-system:system": {
    "config": {
      "hostname": "DC1_SPINE1",
      "domain-name": "aristanetworks.com"
    },
    "dns": {
      "servers": {
        "server": [
          {
            "address": "1.1.1.1",
            "config": {
              "address": "1.1.1.1"
            }
          },
          {
            "address": "8.8.8.8",
            "config": {
              "address": "8.8.8.8"
            }
          }
        ]
      }
    },
    "ntp": {
      "servers": {
        "server": [
          {
            "address": "time.google.com",
            "config": {
              "address": "time.google.com",
              "iburst": true,
              "prefer": true
            }
          },
          {
            "address": "time.cloudflare.com",
            "config": {
              "address": "time.cloudflare.com",
              "iburst": true
            }
          }
        ]
      }
    }
  }
}
```

</p>
</details>
</br>

Using the generated `DC1_SPINE1_config.json` we will configure the hostname, DNS and NTP servers on `spine1` cEOS-Lab node.

### Before configuration

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip get --path '/system/config' --path '/system/ntp' --path '/system/dns'
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897726797084168,
    "time": "2025-05-22T07:08:46.797084168Z",
    "updates": [
      {
        "Path": "system/config",
        "values": {
          "system/config": {
            "openconfig-system:hostname": "spine1"
          }
        }
      }
    ]
  },
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897726797084168,
    "time": "2025-05-22T07:08:46.797084168Z",
    "updates": [
      {
        "Path": "system/ntp",
        "values": {
          "system/ntp": {
            "openconfig-system:servers": {
              "server": []
            },
            "openconfig-system:state": {
              "auth-mismatch": "0"
            }
          }
        }
      }
    ]
  },
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897726797084168,
    "time": "2025-05-22T07:08:46.797084168Z"
  }
]
```

</p>
</details>

### Configuration

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file DC1_SPINE1_config.json
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "source": "clab-arlab-spine1:6030",
  "timestamp": 1747897814774075584,
  "time": "2025-05-22T07:10:14.774075584Z",
  "results": [
    {
      "operation": "UPDATE"
    }
  ]
}
```

</p>
</details>

### After configuration

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip get --path '/system/config' --path '/system/ntp' --path '/system/dns'
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897826995009118,
    "time": "2025-05-22T07:10:26.995009118Z",
    "updates": [
      {
        "Path": "system/config",
        "values": {
          "system/config": {
            "openconfig-system:domain-name": "aristanetworks.com",
            "openconfig-system:hostname": "DC1_SPINE1"
          }
        }
      }
    ]
  },
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897826995009118,
    "time": "2025-05-22T07:10:26.995009118Z",
    "updates": [
      {
        "Path": "system/ntp",
        "values": {
          "system/ntp": {
            "openconfig-system:servers": {
              "server": [
                {
                  "address": "time.cloudflare.com",
                  "config": {
                    "address": "time.cloudflare.com",
                    "iburst": true
                  },
                  "state": {
                    "address": "time.cloudflare.com",
                    "association-type": "SERVER",
                    "iburst": true,
                    "port": 123
                  }
                },
                {
                  "address": "time.google.com",
                  "config": {
                    "address": "time.google.com",
                    "iburst": true,
                    "prefer": true
                  },
                  "state": {
                    "address": "time.google.com",
                    "association-type": "SERVER",
                    "iburst": true,
                    "port": 123,
                    "prefer": true
                  }
                }
              ]
            },
            "openconfig-system:state": {
              "auth-mismatch": "0"
            }
          }
        }
      }
    ]
  },
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747897826995009118,
    "time": "2025-05-22T07:10:26.995009118Z",
    "updates": [
      {
        "Path": "system/dns",
        "values": {
          "system/dns": {
            "openconfig-system:servers": {
              "server": [
                {
                  "address": "1.1.1.1",
                  "config": {
                    "address": "1.1.1.1"
                  },
                  "state": {
                    "address": "1.1.1.1"
                  }
                },
                {
                  "address": "8.8.8.8",
                  "config": {
                    "address": "8.8.8.8"
                  },
                  "state": {
                    "address": "8.8.8.8"
                  }
                }
              ]
            }
          }
        }
      }
    ]
  }
]
```

</p>
</details>

### Switch CLI

```shell
DC1_SPINE1# show running-config | egrep "ntp|hostname|dns|name"
hostname DC1_SPINE1
ip name-server vrf default 1.1.1.1
ip name-server vrf default 8.8.8.8
dns domain aristanetworks.com
ntp server time.cloudflare.com iburst
ntp server time.google.com prefer iburst

--- aaa accounting logs ---

2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=configure session session13265889074581
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=dns domain aristanetworks.com
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=hostname DC1_SPINE1
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=ip name-server vrf default 1.1.1.1
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=ip name-server vrf default 8.8.8.8
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=ntp server vrf default time.google.com prefer iburst
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=ntp server vrf default time.cloudflare.com iburst
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 07:10:15 admin    GNMI        172.100.100.1:62566 stop   service=shell priv-lvl=15 cmd=configure session session13265889074581 commit
```

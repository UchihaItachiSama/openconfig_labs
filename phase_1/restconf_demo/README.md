# RESTCONF Demo

## Overview

In this demo, we will take a look at a few examples related to `RESTCONF`.

## Requirements

Confirm the following packages are installed, if not install them using pip

```shell
python3 -m pip freeze | egrep "pyang|pyangbind|requests"
```

* containerlab and docker installed
* Arista cEOS-Lab image installed

```shell
$ docker images | egrep "IMAGE|ceosimage"

REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
ceosimage                4.30.1F      72e796e3929e   3 weeks ago     2.44GB
```

## Starting the Lab

* Start the `ceos_lab` lab

```shell
cd openconfig_labs/phase_1/ceos_lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `restconf_demo` directory

```shell
cd openconfig_labs/phase_1/restconf_demo
```

## Examples using curl

### Get System State

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/state --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

{
  "openconfig-system:boot-time": "1706854420783309056",
  "openconfig-system:current-datetime": "2024-02-02T09:42:08Z",
  "openconfig-system:hostname": "leaf2",
  "openconfig-system:last-configuration-timestamp": "1706866932953764685",
  "openconfig-system:software-version": "4.30.1F-32308478.4301F (engineering build)"
}
```

### Get interface status

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-interfaces:interfaces/interface=Management1/state --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

{
  "openconfig-interfaces:admin-status": "UP",
  "openconfig-interfaces:counters": {
    "carrier-transitions": "3",
    "in-broadcast-pkts": "0",
    "in-discards": "1720",
    "in-errors": "0",
    "in-fcs-errors": "0",
    "in-multicast-pkts": "0",
    "in-octets": "568382",
    "in-pkts": "3725",
    "in-unicast-pkts": "3725",
    "out-broadcast-pkts": "0",
    "out-discards": "0",
    "out-errors": "0",
    "out-multicast-pkts": "0",
    "out-octets": "352532",
    "out-pkts": "1755",
    "out-unicast-pkts": "1755"
  },
  "openconfig-interfaces:description": "oob_management",
  "openconfig-interfaces:ifindex": 999001,
  "arista-intf-augments:inactive": false,
  "openconfig-interfaces:last-change": "1706854457056334592",
  "openconfig-interfaces:management": true,
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Management1",
  "openconfig-interfaces:oper-status": "UP",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
```

### Configure hostname

#### POST operation

* State before configuration

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

{
  "openconfig-system:hostname": "leaf2"
}
```

* Update the hostname using `hostname.json` file

```json
{
    "openconfig-system:hostname":"DC1_LEAF2"
}
```

* curl using `POST` operation

```shell
curl -sX POST https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d @hostname.json
```

* Let's confirm the hostname got updated

```shell
$ curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

{
  "openconfig-system:hostname": "DC1_LEAF2"
}

----

$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable

DC1_LEAF2#show running-config section hostname
hostname DC1_LEAF2

DC1_LEAF2#show hostname
Hostname: DC1_LEAF2
FQDN:     DC1_LEAF2
```

### Configure DNS Domain

#### POST operation

* Update the DNS domain using the `dns_domain.json` file

```json
{
    "openconfig-system:domain-name":"aristanetworks.com"
}
```

* curl using `POST` operation

```shell
curl -sX POST https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d @dns_domain.json
```

* Let's confirm the dns domain got updated

```shell
$ curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

{
  "openconfig-system:domain-name": "aristanetworks.com",
  "openconfig-system:hostname": "DC1_LEAF2"
}

----

$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable
DC1_LEAF2#
DC1_LEAF2#show hostname
Hostname: DC1_LEAF2
FQDN:     DC1_LEAF2.aristanetworks.com
DC1_LEAF2#
DC1_LEAF2#show running-config | egrep "hostname|dns"
hostname DC1_LEAF2
dns domain aristanetworks.com
```

#### PUT operation

* Doing the same operation with `PUT` we can see the configuration get's replaced.

```shell
curl -sX PUT https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d @dns_domain.json
```

* Checking the configuration we can see the hostname got removed

```shell
$ curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
{
  "openconfig-system:domain-name": "aristanetworks.com"
}

---

$ docker exec -it clab-openconfig-lab-leaf2 Cli
localhost#show hostname
Hostname: localhost
FQDN:     localhost.aristanetworks.com
localhost#
localhost#show running-config | egrep "dns|hostname"
dns domain aristanetworks.com
```

#### DELETE operation

* Using `DELETE` we will remove the dns domain configuration

```shell
curl -sX DELETE https://172.100.100.4:5900/restconf/data/openconfig-system:system/config/domain-name --header 'Accept: application/yang-data+json' -u admin:admin --insecure
```

* Checking the configuration we can see the dns domain has been removed

```shell
$ curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
{
  "openconfig-system:hostname": "DC1_LEAF2"
}

----

$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable
DC1_LEAF2#show hostname
Hostname: DC1_LEAF2
FQDN:     DC1_LEAF2
DC1_LEAF2#
DC1_LEAF2#show running-config | egrep "dns|hostname"
hostname DC1_LEAF2
```

## Examples using python

### GET operation

* Using python `requests` library we will send a `GET` request to query the interface state.

```python
#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint as pp

requests.packages.urllib3.disable_warnings()

headers = {
    'Accept': 'application/yang-data+json'
}

USER="admin"
PASS="admin"

def getState(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state".format(ip, port)
    result = requests.get(url=url, 
                          auth=HTTPBasicAuth(username=USER, password=PASS), 
                          headers=headers, 
                          verify=False)
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())
    
def main():
    getState("172.100.100.4", '5900')

if __name__ == "__main__":
    main()
```

* Executing the script we can see the interface status

```shell
$ python3 interface_demo.py

Result Status Code: 200

Result Content:

{'arista-intf-augments:inactive': False,
 'openconfig-interfaces:admin-status': 'UP',
 'openconfig-interfaces:counters': {'carrier-transitions': '2',
                                    'in-broadcast-pkts': '0',
                                    'in-discards': '0',
                                    'in-errors': '0',
                                    'in-fcs-errors': '0',
                                    'in-multicast-pkts': '13644',
                                    'in-octets': '1746852',
                                    'in-pkts': '13644',
                                    'in-unicast-pkts': '0',
                                    'out-broadcast-pkts': '0',
                                    'out-discards': '0',
                                    'out-errors': '0',
                                    'out-multicast-pkts': '0',
                                    'out-octets': '0',
                                    'out-pkts': '0',
                                    'out-unicast-pkts': '0'},
 'openconfig-interfaces:ifindex': 1,
 'openconfig-interfaces:last-change': '1707201300270076160',
 'openconfig-interfaces:management': False,
 'openconfig-interfaces:mtu': 0,
 'openconfig-interfaces:name': 'Ethernet1',
 'openconfig-interfaces:oper-status': 'UP',
 'openconfig-interfaces:type': 'iana-if-type:ethernetCsmacd',
 'openconfig-platform-port:hardware-port': 'Ethernet1-Port',
 'openconfig-platform-transceiver:transceiver': 'Ethernet1'}
```

### POST Operation

* Now using the python script we will update the interface dscription

```python
def interfaceConfig(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config".format(ip, port)
    config = {
        "openconfig-interfaces:description": "P2P_LINK_TO_DC1_SPINE1_Ethernet2"
    }
    result = requests.post(url=url,
                           auth=HTTPBasicAuth(username=USER, password=PASS),
                           headers=headers,
                           verify=False,
                           json=config
                           )
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())
```

* Execute the script and then let's check the interface configuration

```shell
$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable
DC1_LEAF2#show interfaces description
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC1_SPINE1_Ethernet2
Et2                            up             up
Ma1                            up             up                 oob_management
DC1_LEAF2#show running-config interfaces ethernet 1
interface Ethernet1
   description P2P_LINK_TO_DC1_SPINE1_Ethernet2
```

### DELETE Operation

* Now using the python script we will delete the interface dscription

```python
def deleteIntfConfig(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description".format(ip, port)
    result = requests.delete(url=url,
                             auth=HTTPBasicAuth(username=USER, password=PASS),
                             headers=headers,
                             verify=False)
    print("\nResult Status Code: {}".format(result.status_code))
```

* Execute the script and then let's check the interface configuration

```shell
$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable
DC1_LEAF2#show interfaces description
Interface                      Status         Protocol           Description
Et1                            up             up
Et2                            up             up
Ma1                            up             up                 oob_management
DC1_LEAF2#show running-config interfaces ethernet 1
interface Ethernet1
```

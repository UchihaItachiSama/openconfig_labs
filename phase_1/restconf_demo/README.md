# RESTCONF Demo

## Overview

In this demo, we will take a look at a few examples related to `RESTCONF`.

## Requirements

Confirm the following packages are installed, if not install them using pip

```shell
python3 -m pip freeze | egrep "pyang|pyangbind"
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

```json
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

#### PUT operation

* State before configuration

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config/hostname --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq

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

* curl using `PUT` operation

```shell
curl -sX PUT https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d @hostname.json
```

* Let's confirm the hostname got updated

```shell
$ docker exec -it clab-openconfig-lab-leaf2 Cli
DC1_LEAF2>enable

DC1_LEAF2#show running-config section hostname
hostname DC1_LEAF2

DC1_LEAF2#show hostname
Hostname: DC1_LEAF2
FQDN:     DC1_LEAF2
```


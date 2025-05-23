# RESTCONF Demo

- [RESTCONF Demo](#restconf-demo)
  - [Requirements](#requirements)
  - [cURL Examples](#curl-examples)
    - [Get System State](#get-system-state)
    - [Get interface states](#get-interface-states)
    - [Configure hostname \& domain](#configure-hostname--domain)
      - [Before configuration](#before-configuration)
      - [Configuration](#configuration)
      - [After configuration](#after-configuration)
    - [Configuring domain-name with PUT operation](#configuring-domain-name-with-put-operation)
    - [Removing config using DELETE operation](#removing-config-using-delete-operation)
  - [Python Examples](#python-examples)
    - [GET operation](#get-operation)
    - [POST operation](#post-operation)
    - [DELETE operation](#delete-operation)

In this demo, we will take a look at a few examples related to RESTCONF.

## Requirements

Confirm the following packages are installed, else install them using pip

```shell
python3 -m pip freeze | egrep "pyang|pyangbind|requests"
```

Start the [arista-ceos](../../labs/arista-ceos) lab using containerlab.

## cURL Examples

### Get System State

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/state --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-system:boot-time": "1747909696978395938",
  "openconfig-system:current-datetime": "2025-05-22T10:31:22Z",
  "openconfig-system:hostname": "leaf2",
  "openconfig-system:last-configuration-timestamp": "1747909883508515712",
  "openconfig-system:software-version": "4.34.1F-41757195 (engineering build)"
}
```

</p>
</details>

### Get interface states

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-interfaces:interfaces/interface=Management1/state --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-interfaces:admin-status": "UP",
  "openconfig-interfaces:counters": {
    "carrier-transitions": "3",
    "in-broadcast-pkts": "0",
    "in-discards": "0",
    "in-errors": "0",
    "in-fcs-errors": "0",
    "in-multicast-pkts": "0",
    "in-octets": "26092",
    "in-pkts": "197",
    "in-unicast-pkts": "197",
    "out-broadcast-pkts": "0",
    "out-discards": "0",
    "out-errors": "0",
    "out-multicast-pkts": "0",
    "out-octets": "10302",
    "out-pkts": "58",
    "out-unicast-pkts": "58"
  },
  "openconfig-interfaces:description": "oob_management",
  "openconfig-interfaces:ifindex": 999001,
  "arista-intf-augments:inactive": false,
  "openconfig-interfaces:last-change": "1747909723930136680",
  "openconfig-interfaces:management": true,
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Management1",
  "openconfig-interfaces:oper-status": "UP",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
```

</p>
</details>

### Configure hostname & domain

#### Before configuration

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

Update the hostname and domain using `hostname.json` file

```shell
{
    "openconfig-system:hostname":"DC1_LEAF2",
    "openconfig-system:domain-name":"aristanetworks.com"
}
```

#### Configuration

```shell
curl -sX POST https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d @hostname.json
```

#### After configuration

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-system:domain-name": "aristanetworks.com",
  "openconfig-system:hostname": "DC1_LEAF2"
}
```

</p>
</details></br>

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/state --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-system:boot-time": "1747909696978395938",
  "openconfig-system:current-datetime": "2025-05-22T10:39:32Z",
  "openconfig-system:domain-name": "aristanetworks.com",
  "openconfig-system:hostname": "DC1_LEAF2",
  "openconfig-system:last-configuration-timestamp": "1747910382450388971",
  "openconfig-system:software-version": "4.34.1F-41757195 (engineering build)"
}
```

</p>
</details></br>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF2# show running-config | egrep "hostname|domain"
hostname DC1_LEAF2
dns domain aristanetworks.com

2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session25789566102389
2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=dns domain aristanetworks.com
2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=hostname DC1_LEAF2
2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 10:38:58 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session25789566102389 commit
```

</p>
</details>

### Configuring domain-name with PUT operation

Doing the same operation with `PUT` we can see the configuration get's replaced.

```shell
curl -sX PUT https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure -d '{"openconfig-system:domain-name":"arista.com"}'
```

```shell
curl -sX GET https://172.100.100.4:5900/restconf/data/openconfig-system:system/config --header 'Accept: application/yang-data+json' -u admin:admin --insecure | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "openconfig-system:domain-name": "arista.com"
}
```

</p>
</details></br>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
localhost# show running-config | egrep "hostname|domain"
dns domain arista.com

2025 May 22 10:50:11 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 10:50:12 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session26462850217904
2025 May 22 10:50:12 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=no hostname
2025 May 22 10:50:12 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=dns domain arista.com
2025 May 22 10:50:12 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 10:50:12 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session26462850217904 commit
```

</p>
</details>

### Removing config using DELETE operation

Using `DELETE` we will remove the dns domain configuration

```shell
curl -sX DELETE https://172.100.100.4:5900/restconf/data/openconfig-system:system/config/domain-name --header 'Accept: application/yang-data+json' -u admin:admin --insecure
```

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF2#show running-config | egrep "hostname|domain"
hostname DC1_LEAF2

2025 May 22 11:04:48 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 11:04:48 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session27339676648011
2025 May 22 11:04:48 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=no dns domain
2025 May 22 11:04:48 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 11:04:48 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session27339676648011 commit
```

</p>
</details>

## Python Examples

### GET operation

Using python requests library we will send a `GET` request to query the interface state.

```python
def getState(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state".format(ip, port)
    result = requests.get(url=url, 
                          auth=HTTPBasicAuth(username=USER, password=PASS), 
                          headers=headers, 
                          verify=False)
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())
```

<details>
<summary>Reveal Output</summary>
<p>

```shell

Result Status Code: 200

Result Content:

{'arista-intf-augments:inactive': False,
 'openconfig-interfaces:admin-status': 'UP',
 'openconfig-interfaces:counters': {'carrier-transitions': '2',
                                    'in-broadcast-pkts': '0',
                                    'in-discards': '0',
                                    'in-errors': '0',
                                    'in-fcs-errors': '0',
                                    'in-multicast-pkts': '1239',
                                    'in-octets': '162069',
                                    'in-pkts': '1239',
                                    'in-unicast-pkts': '0',
                                    'out-broadcast-pkts': '0',
                                    'out-discards': '0',
                                    'out-errors': '0',
                                    'out-multicast-pkts': '0',
                                    'out-octets': '0',
                                    'out-pkts': '0',
                                    'out-unicast-pkts': '0'},
 'openconfig-interfaces:ifindex': 1,
 'openconfig-interfaces:last-change': '1747909728176331281',
 'openconfig-interfaces:management': False,
 'openconfig-interfaces:mtu': 0,
 'openconfig-interfaces:name': 'Ethernet1',
 'openconfig-interfaces:oper-status': 'UP',
 'openconfig-interfaces:type': 'iana-if-type:ethernetCsmacd',
 'openconfig-platform-port:hardware-port': 'Ethernet1-Port',
 'openconfig-platform-transceiver:transceiver': 'Ethernet1'}
```

</p>
</details>

### POST operation

Now using the python script we will update the interface dscription

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
                           json=config)
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())
```

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF2# show running-config interfaces Ethernet 1
interface Ethernet1
   description P2P_LINK_TO_DC1_SPINE1_Ethernet2

DC1_LEAF2# show interfaces description 
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC1_SPINE1_Ethernet2
Et2                            up             up                 
Ma1                            up             up                 oob_management
```

</p>
</details>

### DELETE operation

Now using the python script we will delete the interface dscription

```python
def deleteIntfConfig(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description".format(ip, port)
    result = requests.delete(url=url,
                             auth=HTTPBasicAuth(username=USER, password=PASS),
                             headers=headers,
                             verify=False)
    print("\nResult Status Code: {}".format(result.status_code))
```

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF2# show running-config interfaces Ethernet 1
interface Ethernet1

DC1_LEAF2# show interfaces description
Interface                      Status         Protocol           Description
Et1                            up             up                 
Et2                            up             up                 
Ma1                            up             up                 oob_management

2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session27929583487572
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=interface Ethernet1
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=no description
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=exit
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 11:14:38 admin    RESTCONF    172.100.100.1:0 stop   service=shell priv-lvl=15 cmd=configure session session27929583487572 commit
```

</p>
</details>
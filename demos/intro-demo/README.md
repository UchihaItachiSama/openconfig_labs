# Intro Demo

## Starting the lab

- Start the [multi-vendor](../../labs/README.md) lab using containerlab.
- Install [gnmic](https://gnmic.openconfig.net/install/) if not already installed.

## CLI Commands

Nokia SR Linux

```shell
show version
show system lldp neighbor
show network-instance default protocols bgp neighbor
show network-instance default route-table
info flat network-instance default protocols
```

Arista cEOS-Lab

```shell
show version
show lldp neighbors
show ip bgp summary
show ip route
show running-configuration section bgp
```

## JSON-RPC Examples

Nokia SR Linux

```shell
curl -s 'http://admin:NokiaSrl1!@172.100.200.2/jsonrpc' -d @requests/srl-request.json  | jq
```

Arista cEOS-Lab

```shell
curl -sk -X POST https://admin:admin@172.100.200.3/command-api -H "Content-Type: text/json" -d @requests/ceos-request.json | jq
```

## OpenConfig Example

```shell
gnmic -a 172.100.200.3:6030 -u admin -p admin --insecure get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors' | jq
```
